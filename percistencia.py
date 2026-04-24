from json import dump, loads
from pathlib import Path

CAMINHO_JSON = Path.cwd() / "dados" / "clientes.json"


clientes = {
    "12345678900": {
        "titular": True,
        "nome": "Jo\u00e3o da Silva",
        "sexo": "masc",
        "email": "joao.silva@example.com",
        "data_nascimento": "20-05-1995",
        "telefone": "(81) 98888-7777",
        "terceiros": {
            "98765432199": {
                "nome": "Ana Silva",
                "data_nascimento": "15-03-2010",
            },
        },
        "plano_saude": {
            "valor": 350.75,
            "data_vencimento": "10-05-2026",
        },
    }
}


def salvar_arquivo(novos_dados):
    pasta = CAMINHO_JSON.parent
    pasta.mkdir(parents=True, exist_ok=True)

    with open(CAMINHO_JSON, "w") as arquivo:
        dump(novos_dados, arquivo, indent=4)


def ler_arquivo():
    if CAMINHO_JSON.exists():
        with open(CAMINHO_JSON, "r") as arquivo:
            dicionario = loads(arquivo.read())
            return dicionario
    else:
        return {}
