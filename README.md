# Sistema de Matrícula TI Cursos

Projeto em Python para gerenciamento de matrículas de alunos em cursos de TI via terminal.

## Visão Geral

O sistema exibe um menu interativo no terminal e permite consultar ou editar alunos salvos em arquivo JSON. Atualmente, a base principal utilizada pelo fluxo ativo está em `data/alunos.json`.

Os arquivos principais do projeto são:

- `main.py`: ponto de entrada e menu principal.
- `menus.py`: funcionalidades de edição e listagens.
- `percistencia.py`: leitura e escrita dos dados em JSON.
- `data/alunos.json`: base de dados usada pelas funções ativas.

## Funcionalidades

| Funcionalidade | Status | Observação |
| --- | --- | --- |
| Menu principal no terminal | Implementado | Exibe as opções do sistema e controla a navegação principal. |
| Edição de aluno | Implementado | Permite alterar nome, sexo, idade, turno e cursos do aluno. |
| Listagem por curso | Implementado | Filtra alunos por `PHP`, `Java` ou `Delphi`. |
| Listagem por sexo | Implementado | Filtra alunos por sexo cadastrado. |
| Leitura de dados em JSON | Implementado | Os dados são carregados de `data/alunos.json`. |
| Escrita de dados em JSON | Implementado | Alterações são salvas em `data/alunos.json`. |
| Cadastro de aluno | Não implementado | A opção existe no menu, mas ainda não chama nenhuma função. |
| Remoção de aluno | Não implementado | A função `remover_aluno()` ainda está vazia. |
| Listagem geral | Não implementado | A opção aparece no menu, mas ainda não foi conectada. |
| Cálculo de mensalidade integrado ao fluxo atual | Não implementado | Existe lógica separada em `logica.py`, mas ela não está ligada ao sistema principal. |

## Estrutura Atual

O projeto aparenta ter uma transição entre duas versões:

- A versão ativa usa `main.py`, `menus.py`, `percistencia.py` e `data/alunos.json`.
- Os arquivos `logica.py`, `dados.json` e `Av2.py` contêm código legado ou experimental que não está totalmente integrado ao fluxo principal.

## Como Executar

```bash
python main.py
```

## Observações

- O sistema ainda está em desenvolvimento.
- Algumas opções do menu já aparecem para o usuário, mas ainda não possuem implementação completa.
- Há inconsistências de estrutura entre arquivos antigos e a versão atual do sistema, o que pode ser ajustado nas próximas etapas.
