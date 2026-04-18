def listar_por_curso():
    alunos = ler_arquivo()

    print("\nFiltrar por curso:")
    print("1 - PHP")
    print("2 - Java")
    print("3 - Python")

    curso = input("Escolha: ")

    print("\n=== LISTAGEM POR CURSO ===")

    for aluno in alunos:
        if curso in aluno["cursos"]:
            cursos_nome = [nome_curso(c) for c in aluno["cursos"]]
            mensalidade = calcular_mensalidade(aluno)

            

            print(f"""
Matricula: {aluno['matricula']}
Nome: {aluno['nome']}
Sexo: {"F" if aluno['sexo'] == "1" else "M"}
Idade: {aluno['idade']}
Cursos: {' / '.join(cursos_nome)}
Mensalidade: R$ {mensalidade:.2f}
--------------------------
""")

    input("Pressione ENTER para voltar...")

def listar_por_sexo():
    alunos = ler_arquivo()

    print("\nFiltrar por sexo:")
    print("1 - Feminino")
    print("2 - Masculino")

    sexo = input("Escolha: ")

    print("\n=== LISTAGEM POR SEXO ===")

    for aluno in alunos:
        if aluno["sexo"] == sexo:
            cursos_nome = [nome_curso(c) for c in aluno["cursos"]]
            mensalidade = calcular_mensalidade(aluno)

            print(f"""
Matricula: {aluno['matricula']}
Nome: {aluno['nome']}
Sexo: {"F" if aluno['sexo'] == "1" else "M"}
Idade: {aluno['idade']}
Cursos: {' / '.join(cursos_nome)}
Mensalidade: R$ {mensalidade:.2f}
--------------------------
""")

    input("Pressione ENTER para voltar...")