from os import name, system

from menus import (
    cadastrar_cliente,
    cpf,
    data_por_vecimento,
    editar_cliente,
    listagem_geral,
    lps,
    remover,
)


def limpar_tela():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def menu():
    while True:

        print("=" * 80)
        print(f"\n{"Planos":^80}\n")
        print("=" * 80)
        print(
            f"\n{"1 - Cadastrar":^40}¦{"5 - Listagem por Plano":^39}\n"
            + f"{"2 - Editar":^40}¦{"6 - Buscar pro Cliente(CPF)":^39}\n"
            + f"{"3 - Remover":^40}¦{"7 - listagem por Vencimento":^39}\n"
            + f"{"4 - Listagem Geral":^40}¦{"0 - Sair":^39}\n"
        )
        print("=" * 80)

        opcao = input("Escolha: ")
        if opcao == "1":
            limpar_tela()
            cadastrar_cliente()

        elif opcao == "2":
            limpar_tela()
            editar_cliente()

        elif opcao == "3":
            limpar_tela()
            remover()

        elif opcao == "4":
            limpar_tela()
            listagem_geral()

        elif opcao == "5":
            limpar_tela()
            lps()

        elif opcao == "6":
            limpar_tela()
            cpf()

        elif opcao == "7":
            limpar_tela()
            data_por_vecimento()

        elif opcao == "0":
            limpar_tela()
            print("Saindo...")
            break

        else:
            print("Opção invalida!")


menu()
