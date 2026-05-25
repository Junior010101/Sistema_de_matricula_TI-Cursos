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
    AMARELO = "\033[33m"
    MAGENTA = "\033[35m"
    CIANO = "\033[36m"
    BRANCO = "\033[0m"
    BARRA = AMARELO + "║" + BRANCO

    TITULO = f"""
{AMARELO}░▒▓{CIANO}  █████▄ ▄▄     ▄▄▄  ▄▄  ▄▄  ▄▄▄    ▄▄▄▄  ▄▄▄▄▄   ▄█████  ▄▄▄  ▄▄ ▄▄ ▄▄▄▄  ▄▄▄▄▄
{AMARELO}░▒▓{CIANO}  ██▄▄█▀ ██    ██▀██ ███▄██ ██▀██   ██▀██ ██▄▄    ▀▀▀▄▄▄ ██▀██ ██ ██ ██▀██ ██▄▄
{AMARELO}░▒▓{CIANO}  ██     ██▄▄▄ ██▀██ ██ ▀██ ▀███▀   ████▀ ██▄▄▄   █████▀ ██▀██ ▀███▀ ████▀ ██▄▄▄
"""

    def opcao(num, esp=4):
        return " " * esp + "[" + MAGENTA + f"{num}" + BRANCO + "]"

    while True:
        print(TITULO + BRANCO)
        print(AMARELO + "\n╔═[ NÚCLEO SAÚDE v1.0 ]" + "═" * 60 + "╗")
        print("║" + " ".center(82) + BARRA)
        print(
            ""
            + f"{BARRA}{opcao(1)} Cadastrar Novo Cliente      {opcao(5, 5)} Listagem por Tipo de Plano{" " * 11 + BARRA}\n"
            + f"{BARRA}{opcao(2)} Editar Dados Cadastrais     {opcao(6, 5)} Buscar por CPF{" " * 23 + BARRA}\n"
            + f"{BARRA}{opcao(3)} Remover Cliente do Sistema  {opcao(7, 5)} Listar Clientes por Vencimento{" " * 7 + BARRA}\n"
            + f"{BARRA}{opcao(4)} Relatório Geral de Clientes {opcao(0, 5)} Sair do Sistema{" " * 22 + BARRA}"
        )
        print(AMARELO + "║" + " ".center(82) + BARRA)
        print(AMARELO + "╚" + "═" * 82 + "╝")

        opcao = input(BRANCO + "=> Escolha: ")
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
            limpar_tela()
            print("Opção invalida!")


menu()
