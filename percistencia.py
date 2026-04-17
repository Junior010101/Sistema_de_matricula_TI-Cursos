import json as js

# =-=-=-=-=-=-= cria (se n tiver) e abre em dicionario ou abre em formato de dicionario =-=-=-=-=-=- 
# Nota: esse não pode ser def por outros termos dependerem dele (no caso, dependem do dicionario que será trabalhado durante todo o processo)
arquivo = open("dados.json", "a")
arquivo.close()
arquivo = open("dados.json", "r")
arquivo1 = arquivo.read()
arquivo.close()
if arquivo1 == "":
    cadastros = {
        "Nome": "teste nome",
        "matricula": "teste matricula",
        "sexo": "sexo teste",
        "idade":"idade texte",
        "turno":"turno texte",
        "curso":"curso texte",
    }
else:
    cadastros = js.loads(arquivo1)

def salvar(): #=-=-=-=-=-=-=-=pega o dicionario de antes e trasforma em str e salva no arquivo Json =-=-=-=-=-=-=-=-=-=-=-=-=-=-
    arquivo = open("dados.json", "a")
    js.dump(cadastros, arquivo, indent=4)
    arquivo.close()
    print(cadastros)