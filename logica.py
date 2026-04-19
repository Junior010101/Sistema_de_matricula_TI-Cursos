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
        "aluno_teste" : {"matricula": "matricula teste","sexo": "sexo teste","idade": "50","turno": "manha","curso": "PHP", "quant_curso": "2" },
        "aluno_teste2" : {"matricula": "matricula teste2","sexo": "sexo teste2","idade": "30","turno": "noite","curso": "java","quant_curso": "1"},
        "aluno_teste3" : {"matricula": "matricula teste2","sexo": "sexo teste2","idade": "20","turno": "noite","curso": "PHP", "quant_curso": "3"}
    }
else:
    cadastros_pa = js.loads(arquivo1)
def salvar():
    arquivo = open("dados.json", "w")
    js.dump(cadastros_pa, arquivo, indent=4)
    arquivo.close()
salvar()
# Lista com os cursos   
cursos = {"PHP": {"manha": 210.0, "noite": 260.0}, "Java": {"manha": 320.0, "noite": 390.0}, "Python": {"manha": 290.0, "noite": 310.0}}
alunos = []
cadastros_pa["aluno_teste"]["matricula"]
for chave, item in cadastros_pa.items():
    
    if item["curso"] == "PHP":
        if item["turno"] == "manha":
            if int(item["idade"]) > 45:
                if int(item["quant_curso"]) > 1:
                    item["valor_mensalidade"] = 210.0 - (210* 0.45)
        elif item["turno"] == "noite":
            if int(item["idade"]) > 45:
                if int(item["quant_curso"]) > 1:
                    item["valor_mensalidade"] = 260.0 - (260* 0.45)             
            elif int(item["idade"]) < 45:
                if int(item["quant_curso"]) > 1:
                    item["valor_mensalidade"] = 260.0 - (260* 0.30)
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
    