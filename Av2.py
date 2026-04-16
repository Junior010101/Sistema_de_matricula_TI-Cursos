cadastros = {"teste": {"matricula": "12345678", "sexo": "masculino", "idade": "17", "turno": "manhã","curso": "PHP"}}
while True:
    #-=-=-=-=-=- tela inicial =-=-=-=-=
    print("\nTI Cursos\n1 - Cadastrar Aluno\n2 – Editar Aluno\n3 – Remover Aluno\n4 - Listagem Geral\n5 – Listagem por Curso\n6 – Listagem por sexo\n0 – Sair")
    try:
        esco1 = int(input('Selecione ação: '))
    except ValueError:
            print("Digite um número válido!")
            continue
#=-=-=-=-=-=-= Escolha 1 =-=-=-=-=-=
    if esco1 == 1:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("\n\nCadastro\n")
        nome = input("Nome: ") # Nota: se o nome do aluno for igual a outro ele sobreescreve se alguem puder ajeitar agradeço
        cadastros[nome] = []
        cadastros[nome]["matricula"] = input("Matricula:")
        cadastros[nome]["sexo"] = input("Sexo(1-fem/2-mas):")
        cadastros[nome]["idade"] = input("Idade:")
        cadastros[nome]["turno"] = input("Turno(1-manha/2-noite):")
        cadastros[nome]["curso"] = input("Curso(1-PHP/2-Java/3-Delphi):")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    elif esco1 == 2:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("\n\nEdição de cadastro\n\n")
        nome = input("Qual o nome do Aluno ?")
        cadastros[nome]["matricula"] = input("Matricula:")
        sexo = input("Sexo(1-fem/2-mas):")
        cadastros[nome]["sexo"] = "feminino" if sexo == "1" else "masculino"
        cadastros[nome]["idade"] = input("Idade:")
        turno = input("Turno(1-manha/2-noite):")
        cadastros[nome]["turno"] = "Manhã" if turno == "1" else "noite"
        curso = input("Curso(1-PHP/2-Java/3-Delphi):")
        cadastros[nome]["curso"] = "PHP" if curso == "1" else "java" if curso == "2" else "Delphi"
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    elif esco1 == 3:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("\n\nExcluir cadastro\n\n")
        nome = input("Qual o nome do Aluno ?")
        if nome in cadastros:
            del cadastros[nome]
        else:
            print("Nome não encontrado!")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    elif esco1 == 4:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("\n\nlistagem geral\n\n")
        matriz_relatorio = []
        for chaves in cadastros:

            matriz_relatorio.append([chaves,cadastros[chaves]["matricula"],cadastros[chaves]["sexo"],cadastros[chaves]["idade"],cadastros[chaves]["turno"],cadastros[chaves]["curso"]])
        print(matriz_relatorio)