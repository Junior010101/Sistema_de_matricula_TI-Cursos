from menus import editar_aluno, listar_por_curso, listar_por_sexo, remover_aluno


def menu():
    while True:
        print("\nTI Cursos\n")
        print("1 - Cadastrar Aluno")
        print("2 - Editar Aluno")
        print("3 - Remover Aluno")
        print("4 - Listagem Geral")
        print("5 - Listagem por Curso")
        print("6 - Listagem por Sexo")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "2":
            editar_aluno()

        elif opcao == "3":
            remover_aluno()

        elif opcao == "5":
            listar_por_curso()

        elif opcao == "6":
            listar_por_sexo()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção ainda não implementada!")


menu()
