# Sistema de Planos de Saude

Projeto em Python para cadastro e gerenciamento de clientes de um plano de saude via terminal, com persistencia em arquivo JSON.

## Visao Geral

O sistema foi organizado para operar em modo texto e atualmente trabalha com clientes titulares e dependentes. Os dados ficam salvos em `dados/clientes.json`, permitindo manter o cadastro entre execucoes.

O fluxo principal do programa fica no menu exibido por `main.py`, que chama as funcoes de cadastro, edicao, remocao e listagem definidas em `menus.py`.

## Funcionalidades Atuais

- Cadastro de cliente titular.
- Cadastro de dependentes no momento da criacao do titular.
- Cadastro de novo dependente para um titular ja existente.
- Validacao basica de CPF no formato `000.000.000-00`.
- Validacao de data de nascimento no formato `DD-MM-AAAA`.
- Escolha entre os planos `Prata`, `Ouro`, `Diamante` e `Esmeralda`.
- Calculo do valor do plano com base em regras implementadas em `logica.py`.
- Geracao de data de vencimento do plano.
- Edicao de dados principais do cliente e de alguns dados de dependentes.
- Remocao de cliente titular ou de dependente.
- Listagem geral.
- Listagem por tipo de plano.
- Busca de cliente por CPF.
- Listagem por vencimento.

## Estrutura do Projeto

- `main.py`: ponto de entrada do sistema e exibicao do menu principal.
- `menus.py`: fluxo interativo de cadastro, edicao, remocao e consultas.
- `logica.py`: validacoes, calculo de valor do plano e definicao do vencimento.
- `percistencia.py`: leitura e escrita dos dados em `dados/clientes.json`.
- `dados/clientes.json`: base de dados persistida pelo sistema.

## Estrutura dos Dados

Cada cliente titular e salvo com CPF como chave principal. O cadastro inclui campos como:

- `nome`
- `sexo`
- `data_nascimento`
- `email`
- `telefone`
- `plano_saude`
- `terceiros`

Os dependentes ficam armazenados dentro de `terceiros`, vinculados ao CPF do titular.

## Menu Principal

Ao executar o sistema, o usuario encontra as seguintes opcoes:

1. Cadastrar
2. Editar
3. Remover
4. Listagem Geral
5. Listagem por Plano
6. Buscar cliente por CPF
7. Listagem por Vencimento
0. Sair

## Como Executar

Use Python 3:

```bash
python main.py
```

## Regras de Negocio

- Apenas titulares com 18 anos ou mais podem ser cadastrados.
- O CPF e normalizado para apenas numeros antes de ser salvo.
- O valor do plano e recalculado apos alteracoes relevantes.
- A data de vencimento e gerada com base no dia atual e no mes seguinte.
