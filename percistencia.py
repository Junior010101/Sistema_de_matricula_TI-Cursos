from json import dump
from pathlib import Path

CAMINHO_JSON = Path.cwd() / "dados" / "clientes.json"

# Estrutura padronizada do Json:
# {
#     "clientes": [
#         {
#             "titular": true,
#             "cpf": "12345678900",
#             "nome": "João da Silva",
#             "sexo": "masc",
#             "email": "joao.silva@example.com",
#             "data_nascimento": "20-05-1995",
#             "telefone": "(81) 98888-7777",
#             "terceiros": [
#                 "98765432199"
#             ],
#             "plano_saude": {
#                 "tipo": "Diamante",
#                 "valor": 350.75,
#                 "data_vencimento": "10-05-2026"
#             }
#         },
#         {
#             "titular": false,
#             "cpf": "98765432199",
#             "nome": "Ana Silva",
#             "sexo": "fem",
#             "data_nascimento": "15-03-2010"
#         }
#     ]
# }


def salvar_arquivo(novos_dados):
    pasta = CAMINHO_JSON.parent
    pasta.mkdir(parents=True, exist_ok=True)

    with open(CAMINHO_JSON, "w") as arquivo:
        dump(novos_dados, arquivo, indent=4)


# Para @Reimarcosneto3 fazer:
def ler_arquivo():
    pass
