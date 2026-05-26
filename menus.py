from logica import calculo, validar_cpf, validar_data_nascimento, vencimento
from percistencia import ler_arquivo, salvar_arquivo


def gerar_menu_pergunta(pergunta, opcoes=None):
    AMARELO = "\033[33m"
    CIANO = "\033[36m"
    RESET = "\033[0m"

    print(f"{AMARELO}┌" + "─" * 82 + "┐")

    if opcoes is None:
        print(f"{AMARELO}│{RESET}{'':5}{pergunta:<77}{AMARELO}│")
    else:
        opt1 = opcoes[0] if len(opcoes) > 0 else ""
        print(
            f"{AMARELO}│{RESET}{'':5}"
            f"{CIANO}{opt1:<20}{AMARELO}·{RESET}{'':4}"
            f"{pergunta:<52}{AMARELO}│"
        )

        for opcao in opcoes[1:]:
            print(
                f"{AMARELO}│{RESET}{'':5}"
                f"{CIANO}{opcao:<20}{AMARELO}·{RESET}{'':56}{AMARELO}│"
            )

    print(f"{AMARELO}└" + "─" * 82 + f"┘{RESET}")

    return input(f" {CIANO}=>{RESET} {'Escolha' if opcoes else 'Digite'}: ")


def cadastrar_cliente():
    clientes = ler_arquivo()

    pergunta = gerar_menu_pergunta(
        "Você deseja se cadastrar como titular ou dependente?",
        ["1 - Titular", "2 - Dependente"],
    )

    match pergunta:
        case "1":
            cpf = gerar_menu_pergunta(
                "Insira o CPF do cliente nesse formato: (000.000.000-00)"
            )
            cpf, mensagem = validar_cpf(cpf)

            if cpf is None:
                print("\033[31m" + mensagem)
                input(
                    "\n\033[38;2;143;0;255m"
                    + "Pressione enter para continuar..."
                    + "\033[0m"
                )
                return

            if cpf in clientes:
                print("\033[31mO cliente já está cadastrado!")
                input(
                    "\n\033[38;2;143;0;255m"
                    + "Pressione enter para continuar..."
                    + "\033[0m"
                )
                return

            for cliente in clientes.values():
                for cpf_dep in cliente["terceiros"]:
                    if cpf == cpf_dep:
                        print(
                            "\n\033[38;2;255;0;0m"
                            + "Este cliente já está cadastrado como "
                            + "dependente no nome de outro cliente."
                            + "\033[0m"
                        )
                        input(
                            "\n\033[38;2;143;0;255m"
                            + "Pressione enter para continuar..."
                            + "\033[0m"
                        )
                        return

            clientes[cpf] = {
                "titular": True,
                "terceiros": {},
                "plano_saude": {},
            }

            nome = gerar_menu_pergunta("Digite seu nome.")

            if nome.strip() == "":
                print("\033[31mNome vazio ou só com espaços!")
                input(
                    "\n\033[38;2;143;0;255m"
                    + "Pressione enter para continuar..."
                    + "\033[0m"
                )
                return
            clientes[cpf]["nome"] = nome

            sexo = gerar_menu_pergunta(
                "Qual seu sexo?",
                ["1 - fem", "2 - masc"],
            )

            if sexo not in ["1", "2"]:
                print("\033[31mOpção de sexo invalida.")
                input(
                    "\n\033[38;2;143;0;255m"
                    + "Pressione enter para continuar..."
                    + "\033[0m"
                )
                return

            sexos = {"1": "fem", "2": "masc"}
            sexo = sexos[sexo]
            clientes[cpf]["sexo"] = sexo

            data_nascimento = gerar_menu_pergunta(
                "Digite sua data de nascimento nesse formato: (00-00-0000)"
            )

            data_nascimento, info = validar_data_nascimento(data_nascimento)

            if data_nascimento is None:
                print("\033[31m" + info)
                input(
                    "\n\033[38;2;143;0;255m"
                    + "Pressione enter para continuar..."
                    + "\033[0m"
                )
                return

            if info < 18:
                print(
                    "\033[31mPara fazer o cadastro como titular"
                    + " o cliente deve ter mais de 18 anos."
                )
                input(
                    "\n\033[38;2;143;0;255m"
                    + "Pressione enter para continuar..."
                    + "\033[0m"
                )
                return

            clientes[cpf]["data_nascimento"] = data_nascimento

            email = gerar_menu_pergunta("Digite seu e-mail.")
            clientes[cpf]["email"] = email

            telefone = gerar_menu_pergunta("Digite seu numero de telefone.")
            clientes[cpf]["telefone"] = telefone

            opcao = gerar_menu_pergunta(
                "Qual plano deseja cadastrar?",
                [
                    "1 - Prata",
                    "2 - Ouro",
                    "3 - Diamante",
                    "4 - Esmeralda",
                ],
            )

            opcoes = {
                "1": "Prata",
                "2": "Ouro",
                "3": "Diamante",
                "4": "Esmeralda",
            }

            if opcao not in ["1", "2", "3", "4"]:
                print("\033[31mOpção de plano invalida...")
                input(
                    "\n\033[38;2;143;0;255m"
                    + "Pressione enter para continuar..."
                    + "\033[0m"
                )
                return

            opcao = opcoes[opcao]
            clientes[cpf]["plano_saude"]["plano"] = opcao

            escolha = gerar_menu_pergunta(
                "Você possui algum dependente? Sim: (S) ou Não: (N)"
            )

            if escolha.upper() not in ["S", "N", "SIM", "NAO", "NÃO"]:
                print("\033[38;2;255;0;0mOpção invalida...\033[0m")
                input(
                    "\n\033[38;2;143;0;255m"
                    + "Pressione enter para continuar..."
                    + "\033[0m"
                )
                return

            if escolha.upper() in ["S", "SIM"]:
                while True:
                    cpf_dep = gerar_menu_pergunta(
                        "Digite o CPF de seu dependente nesse formato: "
                        + "(000.000.000-00)"
                    )
                    cpf_dep, mensagem = validar_cpf(cpf_dep)

                    if cpf_dep is None:
                        print("\n\033[38;2;255;0;0m" + mensagem + "\033[0m")
                        continue

                    if cpf_dep in clientes:
                        print(
                            "\n\033[38;2;255;0;0m"
                            + "Este dependente já está cadastrado como cliente"
                            + "\033[0m"
                        )
                        continue

                    ja_existe = False
                    for cliente in clientes.values():
                        if cpf_dep in cliente["terceiros"]:
                            ja_existe = True
                            break

                    if ja_existe:
                        print(
                            "\n\033[38;2;255;0;0m"
                            + "Este dependente já está cadastrado "
                            + "no nome de outro cliente."
                            + "\033[0m"
                        )
                        continue

                    clientes[cpf]["terceiros"][cpf_dep] = {}

                    nome_dep = gerar_menu_pergunta("Digite seu nome.")

                    sexo = gerar_menu_pergunta(
                        "Qual seu sexo?",
                        ["1 - fem", "2 - masc"],
                    )

                    if sexo not in ["1", "2"]:
                        print("\033[31mOpção de sexo invalida.")
                        input(
                            "\n\033[38;2;143;0;255m"
                            + "Pressione enter para continuar..."
                            + "\033[0m"
                        )
                        continue

                    sexos = {"1": "fem", "2": "masc"}
                    sexo = sexos[sexo]

                    data_nascimento_dep = gerar_menu_pergunta(
                        "Digite a sua data de nascimento nesse formato: "
                        + "(00-00-0000)"
                    )

                    data_nascimento_dep, info = validar_data_nascimento(
                        data_nascimento_dep
                    )

                    if data_nascimento_dep is None:
                        print("\n\033[38;2;255;0;0m" + info + "\033[0m")
                        continue

                    clientes[cpf]["terceiros"][cpf_dep]["nome"] = nome_dep

                    clientes[cpf]["terceiros"][cpf_dep]["sexo"] = sexo

                    clientes[cpf]["terceiros"][cpf_dep][
                        "data_nascimento"
                    ] = data_nascimento_dep

                    opcao = gerar_menu_pergunta(
                        "Qual plano deseja cadastrar?",
                        [
                            "1 - Prata",
                            "2 - Ouro",
                            "3 - Diamante",
                            "4 - Esmeralda",
                        ],
                    )

                    opcoes = {
                        "1": "Prata",
                        "2": "Ouro",
                        "3": "Diamante",
                        "4": "Esmeralda",
                    }

                    if opcao not in ["1", "2", "3", "4"]:
                        print(
                            "\n\033[38;2;255;0;0m"
                            + "Opção de plano invalida."
                            + "\033[0m",
                        )
                        continue

                    opcao = opcoes[opcao]
                    clientes[cpf]["terceiros"][cpf_dep]["plano"] = opcao
                    print("\033[32mDependente adicionado com sucesso!\033[0m")

                    outro = ""
                    while outro not in ["S", "SIM", "N", "NAO", "NÃO"]:
                        outro = gerar_menu_pergunta(
                            "Deseja cadastrar outro dependente? (S/N)"
                        ).upper()
                        if outro not in ["S", "SIM", "N", "NAO", "NÃO"]:
                            print("\033[38;2;255;0;0mOpção inválida...\033[0m")

                    if outro in ["N", "NAO", "NÃO"]:
                        break

            calculo(clientes)
            vencimento(clientes)

            salvar_arquivo(clientes)

            print("\033[32mCadastro feito com sucesso!")
            input(
                "\n\033[38;2;143;0;255m"
                + "Pressione enter para continuar..."
                + "\033[0m"
            )

        case "2":
            cpf = gerar_menu_pergunta(
                ""
                + "Digite o CPF"
                + " de seu titular nesse formato: "
                + "(000.000.000-00)"
            )
            cpf, mensagem = validar_cpf(cpf)

            if cpf is None:
                print("\033[38;2;255;0;0m" + mensagem)
                input(
                    "\n\033[38;2;143;0;255m"
                    + "Pressione enter para continuar..."
                    + "\033[0m"
                )
                return

            if cpf not in clientes:
                print("\033[38;2;255;0;0m" + "O cliente não está cadastrado!")
                input(
                    "\n\033[38;2;143;0;255m"
                    + "Pressione enter para continuar..."
                    + "\033[0m"
                )
                return

            print("Para cadastrar um novo dependente no seu plano:")

            while True:
                cpf_dep = gerar_menu_pergunta(
                    ""
                    + "Digite o CPF do dependente nesse formato: "
                    + "(000.000.000-00)"
                )
                cpf_dep, mensagem = validar_cpf(cpf_dep)

                if cpf_dep is None:
                    print(mensagem)
                    continue

                if cpf_dep in clientes:
                    print(
                        "\n\033[38;2;255;0;0m"
                        + "Este dependente já está cadastrado como cliente"
                        + "\033[0m"
                    )
                    continue

                ja_existe = False
                for cliente in clientes.values():
                    if cpf_dep in cliente["terceiros"]:
                        ja_existe = True
                        break

                if ja_existe:
                    print(
                        "\n\033[38;2;255;0;0m"
                        + "Este dependente já está cadastrado "
                        + "no nome de outro cliente."
                        + "\033[0m"
                    )
                    continue

                clientes[cpf]["terceiros"][cpf_dep] = {}

                nome_dep = gerar_menu_pergunta("Digite seu nome.")

                sexo = gerar_menu_pergunta(
                    "Qual seu sexo?",
                    ["1 - fem", "2 - masc"],
                )

                if sexo not in ["1", "2"]:
                    print("\033[31mOpção de sexo invalida.")
                    input(
                        "\n\033[38;2;143;0;255m"
                        + "Pressione enter para continuar..."
                        + "\033[0m"
                    )
                    continue

                sexos = {"1": "fem", "2": "masc"}
                sexo = sexos[sexo]

                data_nascimento_dep = gerar_menu_pergunta(
                    ""
                    + "Digite a sua data de nascimento nesse formato: "
                    + "(00-00-0000)"
                )
                data_nascimento_dep, info = validar_data_nascimento(
                    data_nascimento_dep,
                )

                if data_nascimento_dep is None:
                    print(info)
                    continue

                clientes[cpf]["terceiros"][cpf_dep]["nome"] = nome_dep

                clientes[cpf]["terceiros"][cpf_dep]["sexo"] = sexo

                clientes[cpf]["terceiros"][cpf_dep][
                    "data_nascimento"
                ] = data_nascimento_dep

                opcao = gerar_menu_pergunta(
                    "Qual plano deseja cadastrar?",
                    [
                        "1 - Prata",
                        "2 - Ouro",
                        "3 - Diamante",
                        "4 - Esmeralda",
                    ],
                )

                opcoes = {
                    "1": "Prata",
                    "2": "Ouro",
                    "3": "Diamante",
                    "4": "Esmeralda",
                }

                if opcao not in ["1", "2", "3", "4"]:
                    print(
                        "\n"
                        + "\033[38;2;255;0;0m"
                        + "Opção de plano invalida."
                        + "\033[0m",
                    )
                    continue

                opcao = opcoes[opcao]
                clientes[cpf]["terceiros"][cpf_dep]["plano"] = opcao
                print("\033[32mDependente adicionado com sucesso!\033[0m")

                outro = ""
                while outro not in ["S", "SIM", "N", "NAO", "NÃO"]:
                    outro = gerar_menu_pergunta(
                        "Deseja cadastrar outro dependente? (S/N)"
                    ).upper()
                    if outro not in ["S", "SIM", "N", "NAO", "NÃO"]:
                        print("\033[38;2;255;0;0mOpção inválida...\033[0m")

                if outro in ["N", "NAO", "NÃO"]:
                    break

            calculo(clientes)
            vencimento(clientes)

            salvar_arquivo(clientes)

            print("\033[92mCadastro feito com sucesso!\033[0m")
            input(
                "\n\033[38;2;143;0;255m"
                + "Pressione enter para continuar..."
                + "\033[0m"
            )

        case _:
            print("\033[31mOpção invalida...")
            input(
                "\n\033[38;2;143;0;255m"
                + "Pressione enter para continuar..."
                + "\033[0m"
            )


# thiago laymeaaaa
def editar_cliente():
    editar = ler_arquivo()

    cpf = input("Informe o CPF que deseja alterar (000.000.000-00): ")
    cpf, erro = validar_cpf(cpf)
    if cpf is None:
        print(erro)
        return
    if cpf in editar:
        print(
            "1 - Nome"
            + "\n2 - Sexo"
            + "\n3 - E-mail"
            + "\n4 - Data de Nascimento"
            + "\n5 - Telefone"
            + "\n6 - Nome de terceiros"
            + "\n7 - Data de nascimento de terceiros"
        )
        quero_editar = input("Informe o número do dado que você quer editar: ")

        match quero_editar:
            case "1":
                apenasletras = input("Informe o novo nome: ")

                if apenasletras.replace(" ", "").isalpha():
                    editar[cpf]["nome"] = apenasletras
                    print("Alteração feita com sucesso!")
                else:
                    print("Erro! Caracter Inválido")

            case "2":
                mudarsexo = input("Digite 1- Fem ou 2- Masc: ")

                if mudarsexo == "1":
                    editar[cpf]["sexo"] = "fem"
                    print("Alteração feita com sucesso!")
                elif mudarsexo == "2":
                    editar[cpf]["sexo"] = "masc"
                    print("Alteração feita com sucesso!")
                else:
                    print("Opção Inválida!")

                calculo(editar)
                vencimento(editar)

            case "3":
                editar[cpf]["email"] = input("Informe o novo E-mail: ")
                print("Alteração feita com sucesso!")

            case "4":
                apenasnumeros = input(
                    "Informe a nova data de nascimento (dd-mm-aaaa): "
                )

                if apenasnumeros.isdigit():
                    editar[cpf]["data_nascimento"] = apenasnumeros
                    print("Alteração feita com sucesso!")
                else:
                    print("Erro! Caracter Inválido")

                calculo(editar)
                vencimento(editar)

            case "5":
                apenasnumeros = input("Informe o novo telefone: ")

                if apenasnumeros.isdigit():
                    editar[cpf]["telefone"] = apenasnumeros
                    print("Alteração feita com sucesso!")
                else:
                    print("Erro! Caracter Inválido")

            case "6":
                quero_editar2 = input(
                    "Informe o CPF do dependente que você quer editar: "
                )
                nome_com_apenas_letras = input(
                    "Informe o novo nome do dependente: ",
                )

                if nome_com_apenas_letras.isalpha():
                    editar[cpf]["terceiros"][quero_editar2][
                        "nome"
                    ] = nome_com_apenas_letras
                    print("Alteração feita com sucesso!")
                else:
                    print("Erro! Caracter Inválido")

            case "7":
                quero_editar2 = input(
                    "Informe o CPF do dependente que você quer editar: "
                )
                apenasnumeros = input(
                    "Informe a nova data de nascimento (dd-mm-aaaa): "
                )
                data_nascimento, erro = validar_data_nascimento(apenasnumeros)

                if data_nascimento is None:
                    print(erro)
                    return

                editar[cpf]["terceiros"][quero_editar2][
                    "data_nascimento"
                ] = data_nascimento
                print("Alteração feita com sucesso!")

            case _:
                print("Opção Invalida.\n")
                return

        salvar_arquivo(editar)

    else:
        print("Desculpe, o CPF informado não foi encontrado!")


#        lista[0]+ lista[1]+ list[0] + list [1]
# Marcos 100.000.000-00
def remover():
    dados = ler_arquivo()
    while True:
        esc1 = input(
            "1 - Excluir um Cliente" + "\n"
            "2 - Excluir um Dependente" + "\n"
            "Resposta: "
        )
        if esc1 == "1":
            cpf = input("Informe o cpf do Cliente que deseja excluir: ")
            if "." in list(cpf) and "-" in list(cpf):
                a = cpf.split(".")
                b = a[2].split("-")
                cpf = a[0] + a[1] + b[0] + b[1]
            else:
                print("use o formato 000.000.000-00")
            if cpf in dados:
                del dados[cpf]
                print("Cliente excluido com sucesso!")
                break
            else:
                print("vc digitou um cpf inexistente ")
        elif esc1 == "2":
            cpf = input(
                "Informe o cpf do cliente que deseja excluir o Dependente: ",
            )
            if "." in list(cpf) and "-" in list(cpf):
                a = cpf.split(".")
                b = a[2].split("-")
                cpf = a[0] + a[1] + b[0] + b[1]
            else:
                print("use o formato 000.000.000-00")
            if cpf in dados:
                cpft = input(
                    "Informe o cpf do Dependente que deseja excluir: ",
                )

                if "." in list(cpft) and "-" in list(cpft):
                    a = cpft.split(".")
                    b = a[2].split("-")
                    cpft = a[0] + a[1] + b[0] + b[1]
                else:
                    print("use o formato 000.000.000-00")
                if cpft in dados[cpf]["terceiros"]:
                    del dados[cpf]["terceiros"][cpft]
                    print("Dependente excluido com sucesso!")
                    break
                else:
                    print("você digitou um cpf inexistente ")
            else:
                print("você digitou um cpf inexistente ")
        else:
            print("você digitou algo de errado")
    salvar_arquivo(dados)


# Ximenes
def lps():
    dados = ler_arquivo()
    plano = input(
        "Informe o plano de saúde que deseja listar os clientes: "
        "\n1 - Diamante"
        "\n2 - Ouro"
        "\n3 - Prata"
        "\n4 - Esmeralda\n"
        "\n\nEscolha: "
    )
    planos = {"1": 1, "2": 2, "3": 3, "4": 4}
    esc = planos[plano]

    if plano not in planos:
        print("você digitou algo de errado")
        return

    elif esc == 1:
        count = 0

        for _, item in dados.items():
            if item["plano_saude"]["plano"] == "Diamante":
                count += 1

        if count == 0:
            print(
                "\033[38;2;255;0;0m"
                + "Não tem nenhum cliente com esse plano meu manito!!!"
                + "\033[0m"
            )
            input(
                "\n\033[38;2;143;0;255m"
                + "Pressione enter para continuar..."
                + "\033[0m"
            )
            return

        print("Diamante")
        print(
            f"{"CPF":<14}¦ "
            + f"{"Nome":<20}¦ "
            + f"{"Sexo":<6}¦ "
            + f"{"idade":<6}¦ "
            + f"{"E-mail":<20}¦ "
            + f"{"Data Nasc.":<11}¦ "
            + f"{"Telefone":<10}¦ "
            + f"{"Plano":<10}¦ "
            + f"{"Valor":<10}"
            + f"{"Data venc.":<11}"
        )
        print("-" * 111)

        for chave, item in dados.items():
            data_n = str(item["data_nascimento"])
            data_n = data_n[6:8] + "-" + data_n[4:6] + "-" + data_n[0:4]
            _, idade = validar_data_nascimento(data_n)

            data_v = str(item["plano_saude"]["data_vencimento"])
            data_v = data_v[6:8] + "-" + data_v[4:6] + "-" + data_v[0:4]

            if item["plano_saude"]["plano"] == "Diamante":
                print(
                    f"{chave:<14}¦ "
                    + f"{item['nome']:<20}¦ "
                    + f"{item['sexo']:<6}¦ "
                    + f"{str(idade):<5} ¦ "
                    + f"{item['email']:<20}¦ "
                    + f"{str(data_n):<11}¦ "
                    + f"{item['telefone']:<10}¦ "
                    + f"{item['plano_saude']['plano']:<10}¦ "
                    + f"{item['plano_saude']['valor']:<10.2f}"
                    + f"{str(data_v):<10}"
                )
        input("\n\033[38;2;143;0;255mPressione enter para continuar...\033[0m")

    elif esc == 2:
        count = 0

        for _, item in dados.items():
            if item["plano_saude"]["plano"] == "Ouro":
                count += 1

        if count == 0:
            print(
                "\033[38;2;255;0;0m"
                + "Não tem nenhum cliente com esse plano meu manito!!!"
                + "\033[0m"
            )
            input(
                "\n\033[38;2;143;0;255m"
                + "Pressione enter para continuar..."
                + "\033[0m"
            )
            return

        print("Ouro")
        print(
            f"{"CPF":<14}¦ "
            + f"{"Nome":<20}¦ "
            + f"{"Sexo":<6}¦ "
            + f"{"idade":<6}¦ "
            + f"{"E-mail":<20}¦ "
            + f"{"Data Nasc.":<11}¦ "
            + f"{"Telefone":<10}¦ "
            + f"{"Plano":<10}¦ "
            + f"{"Valor":<10}"
            + f"{"Data venc.":<11}"
        )
        print("-" * 116)

        for chave, item in dados.items():
            data_n = str(item["data_nascimento"])
            data_n = data_n[6:8] + "-" + data_n[4:6] + "-" + data_n[0:4]
            _, idade = validar_data_nascimento(data_n)

            data_v = str(item["plano_saude"]["data_vencimento"])
            data_v = data_v[6:8] + "-" + data_v[4:6] + "-" + data_v[0:4]

            if item["plano_saude"]["plano"] == "Ouro":
                print(
                    f"{chave:<14}¦ "
                    + f"{item['nome']:<20}¦ "
                    + f"{item['sexo']:<6}¦ "
                    + f"{str(idade):<5} ¦ "
                    + f"{item['email']:<20}¦ "
                    + f"{str(data_n):<11}¦ "
                    + f"{item['telefone']:<10}¦ "
                    + f"{item['plano_saude']['plano']:<10}¦ "
                    + f"{item['plano_saude']['valor']:<10.2f}"
                    + f"{str(data_v):<10}"
                )
        input(
            "\n"
            + "\033[38;2;143;0;255m"
            + "Pressione enter para continuar..."
            + "\033[0m"
        )

    elif esc == 3:
        count = 0

        for _, item in dados.items():
            if item["plano_saude"]["plano"] == "Prata":
                count += 1

        if count == 0:
            print(
                "\033[38;2;255;0;0m"
                + "Não tem nenhum cliente com esse plano meu manito!!!"
                + "\033[0m"
            )
            input(
                "\n\033[38;2;143;0;255m"
                + "Pressione enter para continuar..."
                + "\033[0m"
            )
            return

        print("Prata")
        print(
            f"{"CPF":<14}¦ "
            + f"{"Nome":<20}¦ "
            + f"{"Sexo":<6}¦ "
            + f"{"idade":<6}¦ "
            + f"{"E-mail":<20}¦ "
            + f"{"Data Nasc.":<11}¦ "
            + f"{"Telefone":<10}¦ "
            + f"{"Plano":<10}¦ "
            + f"{"Valor":<10}"
            + f"{"Data venc.":<11}"
        )
        print("-" * 111)

        for chave, item in dados.items():
            data_n = str(item["data_nascimento"])
            data_n = data_n[6:8] + "-" + data_n[4:6] + "-" + data_n[0:4]
            _, idade = validar_data_nascimento(data_n)

            data_v = str(item["plano_saude"]["data_vencimento"])
            data_v = data_v[6:8] + "-" + data_v[4:6] + "-" + data_v[0:4]

            if item["plano_saude"]["plano"] == "Prata":
                print(
                    f"{chave:<14}¦ "
                    + f"{item['nome']:<20}¦ "
                    + f"{item['sexo']:<6}¦ "
                    + f"{str(idade):<5} ¦ "
                    + f"{item['email']:<20}¦ "
                    + f"{str(data_n):<11}¦ "
                    + f"{item['telefone']:<10}¦ "
                    + f"{item['plano_saude']['plano']:<10}¦ "
                    + f"{item['plano_saude']['valor']:<10.2f}"
                    + f"{str(data_v):<10}"
                )
        input("\n\033[38;2;143;0;255mPressione enter para continuar...\033[0m")

    elif esc == 4:
        count = 0

        for _, item in dados.items():
            if item["plano_saude"]["plano"] == "Esmeralda":
                count += 1

        if count == 0:
            print(
                "\033[38;2;255;0;0m"
                + "Não tem nenhum cliente com esse plano meu manito!!!"
                + "\033[0m"
            )
            input(
                "\n\033[38;2;143;0;255m"
                + "Pressione enter para continuar..."
                + "\033[0m"
            )
            return

        print("Esmeralda")
        print(
            f"{"CPF":<14}¦ "
            + f"{"Nome":<20}¦ "
            + f"{"Sexo":<6}¦ "
            + f"{"idade":<6}¦ "
            + f"{"E-mail":<20}¦ "
            + f"{"Data Nasc.":<11}¦ "
            + f"{"Telefone":<10}¦ "
            + f"{"Plano":<10}¦ "
            + f"{"Valor":<10}"
            + f"{"Data venc.":<11}"
        )
        print("-" * 111)

        for chave, item in dados.items():
            data_n = str(item["data_nascimento"])
            data_n = data_n[6:8] + "-" + data_n[4:6] + "-" + data_n[0:4]
            _, idade = validar_data_nascimento(data_n)

            data_v = str(item["plano_saude"]["data_vencimento"])
            data_v = data_v[6:8] + "-" + data_v[4:6] + "-" + data_v[0:4]

            if item["plano_saude"]["plano"] == "Esmeralda":
                print(
                    f"{chave:<14}¦ "
                    + f"{item['nome']:<20}¦ "
                    + f"{item['sexo']:<6}¦ "
                    + f"{str(idade):<5} ¦ "
                    + f"{item['email']:<20}¦ "
                    + f"{str(data_n):<11}¦ "
                    + f"{item['telefone']:<10}¦ "
                    + f"{item['plano_saude']['plano']:<10}¦ "
                    + f"{item['plano_saude']['valor']:<10.2f}"
                    + f"{str(data_v):<10}"
                )
        input("\n\033[38;2;143;0;255mPressione enter para continuar...\033[0m")


def listagem_geral():
    dados = ler_arquivo()

    if not dados:
        print("\033[38;2;255;0;0mNão tem nada aqui não!!!\033[0m")
        input("\n\033[38;2;143;0;255mPressione enter para continuar...\033[0m")
        return

    print(
        f"{"Tipos":<12}¦ "
        + f"{"CPF":<15}¦ "
        + f"{"Nome":<21}¦ "
        + f"{"Sexo":<6}¦ "
        + f"{"idade":<6}¦ "
        + f"{"E-mail":<21}¦ "
        + f"{"Data Nasc.":<11}¦ "
        + f"{"Telefone":<11}¦ "
        + f"{"Plano":<11}¦ "
        + f"{"Valor":<10}¦ "
        + f"{"Data venc.":<11}"
    )
    print("-" * 160)

    for chave, item in dados.items():
        data_v = str(item["plano_saude"]["data_vencimento"])
        data_n = str(item["data_nascimento"])
        data_n = f"{data_n[6:8] + "-" + data_n[4:6] + "-" + data_n[0:4]}"
        _, idade = validar_data_nascimento(data_n)
        titular = "Titular" if item["titular"] else "Dependente"

        print(
            f"{titular:<12}¦ "
            + f"{chave:<14} ¦ "
            + f"{item['nome']:<20} ¦ "
            + f"{item['sexo']:<5} ¦ "
            + f"{str(idade):<5} ¦ "
            + f"{item['email']:<20} ¦ "
            + f"{data_n:<10} ¦ "
            + f"{item['telefone']:<10} ¦ "
            + f"{item['plano_saude']['plano']:<10} ¦ "
            + f"{item['plano_saude']['valor']:<10.2f} ¦"
            + f"{data_v[6:8] + "-" + data_v[4:6] + "-" + data_v[0:4]:<10}"
        )
        for cpf_dep, dep in item["terceiros"].items():
            data_dep = str(dep["data_nascimento"])
            data_dep = f"{data_dep[6:8]}-{data_dep[4:6]}-{data_dep[0:4]}"
            _, idade_dep = validar_data_nascimento(data_dep)

            print(
                f"{'Dependente':<12}¦ "
                + f"{cpf_dep:<14} ¦ "
                + f"{dep['nome']:<20} ¦ "
                + f"{dep['sexo']:<5} ¦ "
                + f"{str(idade_dep):<5} ¦ "
                + f"{'----':<20} ¦ "
                + f"{data_dep:<10} ¦ "
                + f"{'----':<10} ¦ "
                + f"{dep['plano']:<10} ¦ "
                + f"{item['plano_saude']['valor']:<10.2f} ¦ "
                + f"{data_v[6:8] + '-' + data_v[4:6] + '-' + data_v[0:4]:<10}"
            )

            print("-" * 160)

    input("\n\033[38;2;143;0;255mPressione enter para continuar...\033[0m")


def data_por_vecimento():
    dados = ler_arquivo()

    if not dados:
        print("\033[38;2;255;0;0mNão tem nada aqui não!!!\033[0m")
        input("\n\033[38;2;143;0;255mPressione enter para continuar...\033[0m")
        return

    dados = dict(
        sorted(
            dados.items(),
            key=lambda x: x[1]["plano_saude"]["data_vencimento"],
        )
    )

    print(
        f"{"CPF":<17}¦ "
        + f"{"Nome":<21}¦ "
        + f"{"Sexo":<6}¦ "
        + f"{"idade":<6}¦ "
        + f"{"E-mail":<21}¦ "
        + f"{"Data venc.":<11}¦ "
        + f"{"Telefone":<11}¦ "
        + f"{"Plano":<11}¦"
        + f"{"Valor":<11}"
    )
    print("-" * 128)

    for chave, item in dados.items():
        data_v = str(item["plano_saude"]["data_vencimento"])
        data_n = str(item["data_nascimento"])
        data_n = f"{data_n[6:8] + "-" + data_n[4:6] + "-" + data_n[0:4]}"
        _, idade = validar_data_nascimento(data_n)

        print(
            f"{chave:<16} ¦ "
            + f"{item['nome']:<20} ¦ "
            + f"{item['sexo']:<5} ¦ "
            + f"{str(idade):<5} ¦ "
            + f"{item['email']:<20} ¦ "
            + f"{data_v[6:8] + "-" + data_v[4:6] + "-" + data_v[0:4]:<10} ¦ "
            + f"{item['telefone']:<10} ¦ "
            + f"{item['plano_saude']['plano']:<10} ¦ "
            + f"{item['plano_saude']['valor']:<10.2f}"
        )
    input("\n\033[38;2;143;0;255mPressione enter para continuar...\033[0m")


def cpf():
    dados = ler_arquivo()

    if not dados:
        print("\033[38;2;255;0;0mNão tem nada aqui não!!!\033[0m")
        input("\n\033[38;2;143;0;255mPressione enter para continuar...\033[0m")
        return

    cpf = input("Digite seu CPF (000.000.000-00): ")
    cpf, err = validar_cpf(cpf)

    if cpf is None:
        print(err)
        return

    print(
        f"{"Nome":<20}¦ "
        + f"{"Sexo":<6}¦ "
        + f"{"idade":<6}¦ "
        + f"{"E-mail":<21}¦ "
        + f"{"Data nasc.":<13}¦ "
        + f"{"Telefone":<11}¦ "
        + f"{"Plano":<11}¦ "
        + f"{"Valor":<11}¦ "
        + f"{"Data venc.":<11}"
    )
    print("-" * 116)

    for chave, item in dados.items():
        data_v = str(item["plano_saude"]["data_vencimento"])
        data_n = str(item["data_nascimento"])
        data_n = f"{data_n[6:8] + "-" + data_n[4:6] + "-" + data_n[0:4]}"
        _, idade = validar_data_nascimento(data_n)
        titular = "Titular" if item["titular"] else "Dependente"

        if chave == cpf:
            print(

                f"{'titular':<20}¦ "
                + f"{item['sexo']:<5} ¦ "
                + f"{str(idade):<5} ¦ "
                + f"{item['email']:<20} ¦ "
                + f"{data_n[6:8] + "-" + data_n[4:6] + "-" + data_n[0:4]:<12} ¦ "
                + f"{item['telefone']:<10} ¦ "
                + f"{item['plano_saude']['plano']:<10} ¦  "
                + f"{item['plano_saude']['valor']:<10} ¦ "
                + f"{data_v[6:8] + "-" + data_v[4:6] + "-" + data_v[0:4]:<10}"
            )
            for cpf_dep, dep in item["terceiros"].items():
                data_dep = str(dep["data_nascimento"])
                data_dep = f"{data_dep[6:8]}-{data_dep[4:6]}-{data_dep[0:4]}"
                _, idade_dep = validar_data_nascimento(data_dep)

            print(
                f"{dep['nome']:<19} ¦ "
                + f"{dep['sexo']:<5} ¦ "
                + f"{str(idade_dep):<5} ¦ "
                + f"{'----':<20} ¦ "
                + f"{data_dep:<12} ¦ "
                + f"{'----':<10} ¦ "
                + f"{dep['plano']:<10} ¦ "
                + f"{item['plano_saude']['valor']:<10.2f}"
                + f"{data_v[6:8] + '-' + data_v[4:6] + '-' + data_v[0:4]:<10}"
            )

            print("-" * 111)

        input("\n\033[38;2;143;0;255mPressione enter para continuar...\033[0m")
