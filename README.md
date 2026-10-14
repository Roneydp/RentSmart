RentSmart — Sistema de Orçamento de Locação

    1. Sobre o projeto

O RentSmart é um sistema desenvolvido em Python para automatizar a elaboração de orçamentos de locação de imóveis da empresa fictícia R.M Imóveis.

O sistema permite selecionar o tipo de imóvel, informar suas características, calcular o valor mensal do aluguel, aplicar os adicionais e descontos previstos nas regras de negócio e apresentar a taxa contratual separadamente.

Além disso, o programa gera automaticamente um arquivo CSV com a projeção financeira dos primeiros 12 meses da locação.

    2. Objetivo

Desenvolver uma aplicação que facilite o cálculo dos valores de locação, reduza erros de cálculo manual e apresente as informações financeiras de maneira organizada e transparente.

O projeto também aplica conceitos de programação orientada a objetos (POO), utilizando classes, atributos e métodos para organizar as responsabilidades do sistema.

    3. Funcionalidades

Seleção do tipo de imóvel: apartamento, casa ou estúdio.

Cálculo do aluguel-base de acordo com a categoria escolhida.

Acréscimo por segundo quarto em apartamentos e casas.

Adicional de garagem para apartamentos e casas.

Pacote inicial de duas vagas de estacionamento para estúdios e contratação de vagas extras.

Aplicação de desconto de 5% para apartamentos quando o cliente não possui filhos.

Cálculo da taxa contratual de R$ 2.000,00, com possibilidade de pagamento em até cinco parcelas.

Validação das entradas fornecidas pelo usuário.

Exibição de um resumo detalhado do orçamento.

Geração automática de um arquivo CSV com a projeção financeira de 12 meses.

    4. Regras de negócio

Valores-base dos imóveis

Tipo de imóvel

Valor mensal

Apartamento de 1 quarto

R$ 700,00

Casa de 1 quarto

R$ 900,00

Estúdio

R$ 1.200,00

Adicionais

Descrição

Valor

Segundo quarto em apartamento

R$ 200,00

Segundo quarto em casa

R$ 250,00

Garagem para apartamento ou casa

R$ 300,00

Pacote inicial de duas vagas para estúdio

R$ 250,00

Cada vaga extra para estúdio

R$ 60,00

Desconto e taxa contratual

Apartamentos: desconto de 5% sobre o subtotal do aluguel, após os adicionais, quando o cliente não possui filhos.

Taxa contratual: R$ 2.000,00, paga em até cinco parcelas.

A taxa contratual é apresentada separadamente do aluguel mensal.

    5. Tecnologias utilizadas

Python: linguagem utilizada no desenvolvimento.

Programação Orientada a Objetos (POO): organização do sistema em classes e métodos.

Módulo decimal: cálculos monetários com controle de precisão decimal.

Módulo csv: criação do arquivo de projeção financeira.

Módulo pathlib: definição do caminho do arquivo gerado.

Módulo unittest: execução de testes automatizados.

    6. Organização do código

O sistema é organizado pelas seguintes classes:

Imovel

Armazena as características do imóvel e calcula o aluguel-base e os adicionais aplicáveis.

Orcamento

Calcula o subtotal, o desconto, o aluguel mensal, as parcelas da taxa contratual e os totais mensais previstos. Também apresenta o resumo do orçamento.

ProjecaoCSV

Gera o arquivo CSV com os valores previstos para cada um dos 12 meses.

O programa também possui funções auxiliares para validação das entradas, formatação monetária e coleta das informações fornecidas pelo usuário.

    7. Como executar o projeto

Pré-requisitos

Python 3 instalado.

Arquivo principal main.py.

Terminal do sistema ou terminal integrado do Visual Studio Code.

O projeto utiliza módulos da biblioteca padrão do Python, sem necessidade de instalar pacotes externos para executar o programa.

Passo a passo

Baixe ou clone o repositório do projeto.

Abra a pasta do projeto no Visual Studio Code ou no terminal.

Execute o programa com o comando:

python main.py

No Windows, se necessário, utilize:

py main.py

Siga as perguntas exibidas no terminal para informar as características do imóvel e a quantidade de parcelas.

Consulte o resumo do orçamento apresentado.

Verifique o arquivo projecao_12_meses.csv, criado na mesma pasta do arquivo principal.

    8. Arquivo CSV — Projeção de 12 meses

O sistema gera automaticamente o arquivo projecao_12_meses.csv na mesma pasta do arquivo main.py.

A projeção apresenta os valores previstos para 12 meses, com os meses identificados pelos seus nomes em português.

O arquivo contém as seguintes colunas:

- Mês da Projeção: nome do mês correspondente.
  
- Aluguel Bruto (R$): valor do aluguel com os adicionais, antes da aplicação do desconto.
  
- Desconto Aplicado (R$): valor do desconto concedido, quando aplicável.
  
- Aluguel Mensal Final (R$): valor do aluguel após a aplicação do desconto.
  
- Parcela da Taxa Contratual (R$): valor da parcela da taxa contratual no mês correspondente.
  
- Taxa Contratual Total (R$): valor total da taxa contratual, de R$2.000,00.
  
- Total Previsto no Mês (R$): soma do aluguel mensal final com a parcela da taxa contratual daquele mês.

O arquivo utiliza ponto e vírgula como separador e codificação UTF-8 com BOM, facilitando sua abertura em programas de planilhas, como o Microsoft Excel.

    9. Testes

O projeto possui testes automatizados desenvolvidos com o módulo unittest, para verificar cálculos de aluguel, adicionais, descontos, parcelas, validação de entradas e geração do CSV.

Para executar os testes, mantenha o arquivo test_rentsmart.py na mesma pasta de main.py e utilize:

python -m unittest -v test_rentsmart.py

No Windows, se necessário:

py -m unittest -v test_rentsmart.py

Os testes devem terminar sem falhas para que os cenários avaliados sejam considerados aprovados.

    10. Considerações finais

O RentSmart demonstra a aplicação de conceitos fundamentais de Python e programação orientada a objetos na resolução de um problema de negócio.

A automatização dos cálculos, a validação das entradas, a apresentação detalhada do orçamento e a geração da projeção financeira contribuem para uma solução organizada, reutilizável e de fácil execução.

    11. Autor

Projeto acadêmico desenvolvido para a disciplina de programação, com foco em lógica de programação, organização de código e programação orientada a objetos.