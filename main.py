from menus import (
    cadastrar_cliente,
    editar_cliente,
    remover,
    listagem_geral,
    lps,
    cpf,
    data_por_vecimento,
)
import os

def limpar_tela():
   
    if os.name == 'nt':
        os.system('cls')
 
    else:
        os.system('clear')


def menu():
    while True:
        
        print(" "+"="*100,F"\n{"Planos":^100}\n","="*100,f"\n{"1 - Cadastrar":^50}¦{"2 - Editar":^49}\n{"3 - Remover":^50}¦{"4 - Listagem Geral":^49}\n{"5 - Listagem por Plano":^50}¦{"6 - Buscar pro Cliente(CPF)":^49}\n{"7 - listagem por Vencimento":^50}¦{"0 - Sair":^49}\n","="*100)
        

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
            print("Opção ainda não implementada!")


menu()
