from json import dump,loads
from pathlib import Path

CAMINHO_JSON = Path.cwd() / "dados" / "clientes.json"



clientes = {
    "titular": True,
    "cpf": "12345678900",
    "nome": "João da Silva",
    "sexo": "masc",
    "email": "joao.silva@example.com",
    "data_nascimento": "20-05-1995",
    "telefone": "(81) 98888-7777",
    "terceiros": [
      {
        "cpf": "987.654.321-99",
        "nome": "Ana Silva",
        "data_nascimento": "15-03-2010"
      }
    ],
    "plano_saude": {
      "valor": 350.75,
      "data_vencimento": "10-05-2026"
    }
  }


def salvar_arquivo(novos_dados):
    pasta = CAMINHO_JSON.parent
    pasta.mkdir(parents=True, exist_ok=True)

    with open(CAMINHO_JSON, "w") as arquivo:
        dump(novos_dados, arquivo, indent=4)

salvar_arquivo(clientes)
# Para @Reimarcosneto3 fazer:
def ler_arquivo():
    if CAMINHO_JSON.exists():
        arquivo = open(CAMINHO_JSON, "r")
        arquivo1 = arquivo.read()
        dicionario = loads(arquivo1) #pra facilitar a manipulação de dados dps
        print(arquivo1)
    else:
        print("Arquivo NÃO existe")
ler_arquivo()
