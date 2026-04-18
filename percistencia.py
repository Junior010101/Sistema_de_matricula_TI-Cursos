import json as js

# =-=-=-=-=-=-= cria (se n tiver) e abre em dicionario ou abre em formato de dicionario =-=-=-=-=-=- 
# Nota: esse não pode ser def por outros termos dependerem dele (no caso, dependem do dicionario que será trabalhado durante todo o processo)
arquivo = open("dados.json", "a")
arquivo.close()
arquivo = open("dados.json", "r")
arquivo1 = arquivo.read()
arquivo.close()
if arquivo1 == "":
    cadastros_pa = { 
        "aluno_teste" : {"matricula": "matricula teste","sexo": "sexo teste","idade": "idade teste","turno": "turno teste","curso": "PHP",},
        "aluno_teste2" : {"matricula": "matricula teste2","sexo": "sexo teste2","idade": "idade teste2","turno": "turno teste","curso": "java",},
        "aluno_teste3" : {"matricula": "matricula teste2","sexo": "sexo teste2","idade": "idade teste2","turno": "turno teste","curso": "PHP",}
    }
else:
    cadastros_pa = js.loads(arquivo1)


def salvar(): #=-=-=-=-=-=-=-=pega o msm dicionario de antes e trasforma em str e salva no arquivo Json =-=-=-=-=-=-=-=-=-=-=-=-=-=-
    arquivo = open("dados.json", "w")
    js.dump(cadastros_pa, arquivo, indent=4)
    arquivo.close()
salvar()