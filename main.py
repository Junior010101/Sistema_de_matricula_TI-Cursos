from menus import (
    cadastrar_cliente,
    editar_cliente,
    remover,
    listagem_geral,
    lps,
    cpf,
    data_por_vecimento,
)


def menu():
    while True:
        print("=" * 92)
        print(f"|{'Planos':^90}|")
        print("=" * 92)
        print(f"|{'1 - Cadastrar':^45}|{'5 - Listagem por Plano':^44}|")
        print(f"|{'2 - Editar':^45}|{'6 - Buscar por Cliente(CPF)':^44}|")
        print(f"|{'3 - Remover':^45}|{'7 - Listagem por Vencimento':^44}|")
        print(f"|{'4 - Listagem Geral':^45}|{'0 - Sair':^44}|")
        print("=" * 92)

        opcao = input("Escolha: ")
        if opcao == "1":
            cadastrar_cliente()

        elif opcao == "2":
            editar_cliente()

        elif opcao == "3":
            remover()

        elif opcao == "4":
            listagem_geral()

        elif opcao == "5":
            lps()

        elif opcao == "6":
            cpf()

        elif opcao == "7":
            data_por_vecimento()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção ainda não implementada!")


menu()
