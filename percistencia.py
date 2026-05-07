from json import dump, loads
from pathlib import Path

CAMINHO_JSON = Path.cwd() / "dados" / "clientes.json"

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
