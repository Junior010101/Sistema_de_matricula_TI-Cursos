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
{AMARELO}░▒▓{CIANO}                                                                 ▄▀
{AMARELO}░▒▓{CIANO}  █████▄ ▄▄     ▄▄▄  ▄▄  ▄▄  ▄▄▄    ▄▄▄▄  ▄▄▄▄▄   ▄█████  ▄▄▄  ▄▄ ▄▄ ▄▄▄▄  ▄▄▄▄▄
{AMARELO}░▒▓{CIANO}  ██▄▄█▀ ██    ██▀██ ███▄██ ██▀██   ██▀██ ██▄▄    ▀▀▀▄▄▄ ██▀██ ██ ██ ██▀██ ██▄▄
{AMARELO}░▒▓{CIANO}  ██     ██▄▄▄ ██▀██ ██ ▀██ ▀███▀   ████▀ ██▄▄▄   █████▀ ██▀██ ▀███▀ ████▀ ██▄▄▄
{AMARELO}░▒▓{CIANO}
"""  # noqa

    while True:

        def opcao(num, esp=4):
            string = " " * esp + "[" + MAGENTA + f"{num}" + BRANCO + "]"
            return string

        print(TITULO + BRANCO)
        print(AMARELO + "\n╔═[ NÚCLEO SAÚDE v1.0 ]" + "═" * 60 + "╗")
        print("║" + " ".center(82) + BARRA)
        print(
            ""
            + f"{BARRA}{opcao(1)} Cadastrar Novo Cliente      {opcao(5, 5)} Listagem por Tipo de Plano{" " * 11 + BARRA}\n"  # noqa
            + f"{BARRA}{opcao(2)} Editar Dados Cadastrais     {opcao(6, 5)} Buscar por CPF{" " * 23 + BARRA}\n"  # noqa
            + f"{BARRA}{opcao(3)} Remover Cliente do Sistema  {opcao(7, 5)} Listar Clientes por Vencimento{" " * 7 + BARRA}\n"  # noqa
            + f"{BARRA}{opcao(4)} Relatório Geral de Clientes {opcao(0, 5)} Sair do Sistema{" " * 22 + BARRA}"  # noqa
        )
        print(AMARELO + "║" + " ".center(82) + BARRA)
        print(AMARELO + "╚" + "═" * 82 + "╝")

        opcao = input(BRANCO + "=> Escolha: ")
        if opcao == "1":
            cadastrar_cliente()
            limpar_tela()

        elif opcao == "2":
            limpar_tela()
            editar_cliente()

        elif opcao == "3":
            limpar_tela()
            remover()

        elif opcao == "4":
            listagem_geral()
            limpar_tela()

        elif opcao == "5":
            lps()
            limpar_tela()

        elif opcao == "6":
            cpf()
            limpar_tela()

        elif opcao == "7":
            data_por_vecimento()
            limpar_tela()

        elif opcao == "0":
            limpar_tela()
            print("Saindo...")
            break

        else:
            limpar_tela()
            print("\033[31mOpção invalida!\033[0m")


menu()
