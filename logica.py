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

# Lista com os cursos   
cursos = {"PHP": {"manha": 210.0, "noite": 260.0}, "Java": {"manha": 320.0, "noite": 390.0}, "Python": {"manha": 290.0, "noite": 310.0}}
alunos = []

# Armazenamento dos alunos
def calculo_da_mensalidade(curso, turno, idade, quantidade_de_cursos):
    preco = cursos[curso][turno]
    desconto = 0

# Condição para os descontos
    if quantidade_de_cursos > 1:
        desconto = 0.30
    elif idade > 45:
        desconto = 0.15
    valor_com_desconto = preco - (preco * desconto)
    return valor_com_desconto
    