from menus import cadastrar_cliente, editar_cliente, remover, listagem_geral, lps, cpf, data_por_vecimento
from logica import calculo,vencimento


def menu():
    while True:
        print("\n Planos \n")
        print("1 - Cadastrar")
        print("2 - Editar")
        print("3 - Remover")
        print("4 - Listagem Geral")
        print("5 - Listagem por Plano")
        print("6 - Buscar pro Cliente(CPF)")
        print("7 - Vencimento")
        print("0 - Sair")

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
        
        #vai funcionar sempre
        calculo()
        vencimento()


menu()
