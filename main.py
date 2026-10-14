import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


# VALORES BASE DOS IMÓVEIS
ALUGUEL_APARTAMENTO_1_QUARTO = Decimal("700.00")
ALUGUEL_CASA_1_QUARTO = Decimal("900.00")
ALUGUEL_ESTUDIO = Decimal("1200.00")

# ACRÉSCIMOS
ADICIONAL_APARTAMENTO_2_QUARTOS = Decimal("200.00")
ADICIONAL_CASA_2_QUARTOS = Decimal("250.00")
VALOR_GARAGEM_APARTAMENTO_CASA = Decimal("300.00")

# VAGAS DE ESTACIONAMENTO PARA ESTÚDIO
PACOTE_INICIAL_VAGAS_ESTUDIO = Decimal("250.00")
VALOR_VAGA_EXTRA_ESTUDIO = Decimal("60.00")

# TAXA E DESCONTO
TAXA_CONTRATUAL = Decimal("2000.00")
MAXIMO_PARCELAS = 5
PERCENTUAL_DESCONTO_APARTAMENTO = Decimal("0.05")

# PROJEÇÃO FINANCEIRA
MESES_PROJECAO = 12

class Imovel:
    def __init__(
        self,
        categoria,
        quartos=None,
        possui_garagem=False,
        possui_criancas=None,
        possui_pacote_vagas=False,
        vagas_extras_estudio=0
    ):
        self.categoria = categoria
        self.quartos = quartos
        self.possui_garagem = possui_garagem
        self.possui_criancas = possui_criancas
        self.possui_pacote_vagas = possui_pacote_vagas
        self.vagas_extras_estudio = vagas_extras_estudio

    def calcular_aluguel_base(self):
        if self.categoria == "Apartamento":
            return ALUGUEL_APARTAMENTO_1_QUARTO

        elif self.categoria == "Casa":
            return ALUGUEL_CASA_1_QUARTO

        elif self.categoria == "Estúdio":
            return ALUGUEL_ESTUDIO

        return Decimal("0.00")

    def calcular_adicional_quartos(self):
        if self.categoria == "Apartamento" and self.quartos == 2:
            return ADICIONAL_APARTAMENTO_2_QUARTOS

        elif self.categoria == "Casa" and self.quartos == 2:
            return ADICIONAL_CASA_2_QUARTOS

        return Decimal("0.00")

    def calcular_adicional_garagem(self):
        if (
            self.categoria in ("Apartamento", "Casa")
            and self.possui_garagem
        ):
            return VALOR_GARAGEM_APARTAMENTO_CASA

        return Decimal("0.00")

    def calcular_adicional_vagas_estudio(self):
        if self.categoria != "Estúdio":
            return Decimal("0.00")

        if not self.possui_pacote_vagas:
            return Decimal("0.00")

        valor_extras = (
            VALOR_VAGA_EXTRA_ESTUDIO
            * self.vagas_extras_estudio
        )

        return PACOTE_INICIAL_VAGAS_ESTUDIO + valor_extras

    def calcular_total_adicionais(self):
        return (
            self.calcular_adicional_quartos()
            + self.calcular_adicional_garagem()
            + self.calcular_adicional_vagas_estudio()
        )

class Orcamento:
    def __init__(self, imovel, quantidade_parcelas):
        self.imovel = imovel
        self.quantidade_parcelas = quantidade_parcelas

        self.aluguel_base = imovel.calcular_aluguel_base()
        self.adicional_quartos = (
            imovel.calcular_adicional_quartos()
        )
        self.adicional_garagem = (
            imovel.calcular_adicional_garagem()
        )
        self.adicional_vagas_estudio = (
            imovel.calcular_adicional_vagas_estudio()
        )

        self.total_adicionais = (
    imovel.calcular_total_adicionais()
)

        self.subtotal = (
            self.aluguel_base + self.total_adicionais
        )

        self.desconto = self.calcular_desconto()

        self.aluguel_mensal = (
            self.subtotal - self.desconto
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )

    def calcular_desconto(self):
        if (
            self.imovel.categoria == "Apartamento"
            and self.imovel.possui_criancas is False
        ):
            return (
                self.subtotal
                * PERCENTUAL_DESCONTO_APARTAMENTO
            ).quantize(
                Decimal("0.01"),
                rounding=ROUND_HALF_UP
            )

        return Decimal("0.00")

    def calcular_valor_parcela(self, numero_parcela):
        if not 1 <= numero_parcela <= self.quantidade_parcelas:
            return Decimal("0.00")

        valor_padrao = (
            TAXA_CONTRATUAL
            / self.quantidade_parcelas
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )

        if numero_parcela < self.quantidade_parcelas:
            return valor_padrao

        # Ajusta a última parcela para fechar os R$ 2.000,00.
        parcelas_anteriores = (
            valor_padrao * (self.quantidade_parcelas - 1)
        )

        return TAXA_CONTRATUAL - parcelas_anteriores

    def calcular_total_mes(self, mes):
        parcela_contratual = Decimal("0.00")

        if mes <= self.quantidade_parcelas:
            parcela_contratual = self.calcular_valor_parcela(mes)

        return self.aluguel_mensal + parcela_contratual

    def exibir_resumo(self):
        print("\n" + "=" * 45)
        print("          RESUMO DO ORÇAMENTO RENTSMART")
        print("=" * 45)

        print(f"Categoria: {self.imovel.categoria}")

        if self.imovel.quartos is not None:
            print(f"Quartos: {self.imovel.quartos}")

        print(
            f"Aluguel base: "
            f"{formatar_reais(self.aluguel_base)}"
        )
        print(
            f"Adicional de quartos: "
            f"{formatar_reais(self.adicional_quartos)}"
        )
        print(
            f"Adicional de garagem: "
            f"{formatar_reais(self.adicional_garagem)}"
        )
        print(
            f"Adicional de vagas do estúdio: "
            f"{formatar_reais(self.adicional_vagas_estudio)}"
        )
        print(
            f"Subtotal antes do desconto: "
            f"{formatar_reais(self.subtotal)}"
        )
        print(
            f"Desconto: {formatar_reais(self.desconto)}"
        )
        print("-" * 45)
        print(
            f"ALUGUEL MENSAL: "
            f"{formatar_reais(self.aluguel_mensal)}"
        )
        print(
            f"Taxa contratual total: "
            f"{formatar_reais(TAXA_CONTRATUAL)}"
        )
        print(
            f"Quantidade de parcelas: "
            f"{self.quantidade_parcelas}"
        )

        for numero in range(
            1, self.quantidade_parcelas + 1
        ):
            valor = self.calcular_valor_parcela(numero)
            print(
                f"Parcela {numero}: "
                f"{formatar_reais(valor)}"
            )

        print("=" * 45)
        print(
            "A taxa contratual é separada do aluguel mensal."
        )

def formatar_reais(valor):
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = (
        valor_formatado
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

    return f"R$ {valor_formatado}"


def formatar_decimal_csv(valor):
    return f"{valor:.2f}".replace(".", ",")


def ler_opcao(pergunta, opcoes_validas):
    while True:
        resposta = input(pergunta).strip()

        if resposta in opcoes_validas:
            return resposta

        print(
            "Opção inválida. "
            f"Digite uma destas opções: {', '.join(opcoes_validas)}"
        )


def ler_inteiro(pergunta, minimo, maximo=None):
    while True:
        try:
            valor = int(input(pergunta))

            if valor < minimo:
                print(f"Digite um número igual ou maior que {minimo}.")
                continue

            if maximo is not None and valor > maximo:
                print(f"Digite um número igual ou menor que {maximo}.")
                continue

            return valor

        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def ler_sim_nao(pergunta):
    while True:
        resposta = input(pergunta).strip().lower()

        if resposta in ("s", "sim"):
            return True

        if resposta in ("n", "nao", "não"):
            return False

        print("Resposta inválida. Digite S para sim ou N para não.")

class ProjecaoCSV:
    def __init__(self, orcamento):
        self.orcamento = orcamento

    def gerar_csv(self):
        caminho_arquivo = (
            Path(__file__).resolve().parent
            / "projecao_12_meses.csv"
        )

        nomes_meses = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"
        ]

        with open(
            caminho_arquivo,
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as arquivo:

            campos = [
                "Mês da Projeção",
                "Aluguel Bruto (R$)",
                "Desconto Aplicado (R$)",
                "Aluguel Mensal Final (R$)",
                "Parcela da Taxa Contratual (R$)",
                "Taxa Contratual Total (R$)",
                "Total Previsto no Mês (R$)"
            ]

            escritor = csv.DictWriter(
                arquivo,
                fieldnames=campos,
                delimiter=";"
            )

            escritor.writeheader()

            for mes in range(1, MESES_PROJECAO + 1):
                nome_mes = nomes_meses[mes - 1]

                aluguel_bruto = self.orcamento.subtotal
                desconto = self.orcamento.desconto
                aluguel_final = self.orcamento.aluguel_mensal

                parcela = (
                    self.orcamento.calcular_valor_parcela(mes)
                    if mes <= self.orcamento.quantidade_parcelas
                    else Decimal("0.00")
                )

                total_mes = self.orcamento.calcular_total_mes(mes)

                escritor.writerow({
                    "Mês da Projeção": nome_mes,
                    "Aluguel Bruto (R$)": formatar_decimal_csv(
                        aluguel_bruto
                    ),
                    "Desconto Aplicado (R$)": formatar_decimal_csv(
                        desconto
                    ),
                    "Aluguel Mensal Final (R$)": formatar_decimal_csv(
                        aluguel_final
                    ),
                    "Parcela da Taxa Contratual (R$)": formatar_decimal_csv(
                        parcela
                    ),
                    "Taxa Contratual Total (R$)": formatar_decimal_csv(
                        TAXA_CONTRATUAL
                    ),
                    "Total Previsto no Mês (R$)": formatar_decimal_csv(
                        total_mes
                    )
                })

        print("\nArquivo CSV gerado com sucesso!")
        print(f"Local do arquivo: {caminho_arquivo}")

def coletar_dados_imovel():
    print("\n" + "=" * 45)
    print("        RENTSMART - ORÇAMENTO DE LOCAÇÃO")
    print("=" * 45)

    print("\nEscolha a categoria do imóvel:")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estúdio")

    opcao = ler_opcao(
        "Digite a opção desejada: ",
        ["1", "2", "3"]
    )

    categorias = {
        "1": "Apartamento",
        "2": "Casa",
        "3": "Estúdio"
    }

    categoria = categorias[opcao]

    quartos = None
    possui_garagem = False
    possui_criancas = None
    possui_pacote_vagas = False
    vagas_extras_estudio = 0

    if categoria in ("Apartamento", "Casa"):
        quartos = ler_inteiro(
            "Quantidade de quartos (1 ou 2): ",
            1,
            2
        )

        possui_garagem = ler_sim_nao(
            "O imóvel possui garagem? (S/N): "
        )

    if categoria == "Apartamento":
        possui_criancas = ler_sim_nao(
            "O cliente possui filhos? (S/N): "
        )

    if categoria == "Estúdio":
        possui_pacote_vagas = ler_sim_nao(
            "Deseja contratar o pacote inicial de duas vagas "
            "por R$ 250,00? (S/N): "
        )

        if possui_pacote_vagas:
            vagas_extras_estudio = ler_inteiro(
                "Quantas vagas extras deseja contratar? ",
                0
            )

    imovel = Imovel(
        categoria=categoria,
        quartos=quartos,
        possui_garagem=possui_garagem,
        possui_criancas=possui_criancas,
        possui_pacote_vagas=possui_pacote_vagas,
        vagas_extras_estudio=vagas_extras_estudio
    )

    return imovel


def coletar_quantidade_parcelas():
    print("\nTaxa contratual: R$ 2.000,00")
    print("É possível parcelar em até 5 vezes.")

    return ler_inteiro(
        "Em quantas parcelas deseja pagar a taxa? ",
        1,
        MAXIMO_PARCELAS
    )

def main():
    print("Bem-vindo ao sistema RentSmart!")

    imovel = coletar_dados_imovel()

    quantidade_parcelas = coletar_quantidade_parcelas()

    orcamento = Orcamento(
        imovel,
        quantidade_parcelas
    )

    orcamento.exibir_resumo()

    projecao = ProjecaoCSV(orcamento)
    projecao.gerar_csv()

    print("\nProcesso finalizado.")


if __name__ == "__main__":
    main()
