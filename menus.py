from logica import validar_cpf, validar_data_nascimento, calculo, vencimento
from percistencia import ler_arquivo, salvar_arquivo


def cadastrar_cliente():
    clientes = ler_arquivo()

    print("1 - Titular\n2 - Dependente\n")
    pergunta = input("Você deseja se cadastrar como titular ou dependente: ")

    match pergunta:
        case "1":
            cpf = input("\nDigite seu CPF (000.000.000-00): ")
            cpf, mensagem = validar_cpf(cpf)

            if cpf is None:
                print(mensagem)
                return

            if cpf in clientes:
                print("O cliente já está cadastrado!")
                return

            clientes[cpf] = {
                "titular": True,
                "terceiros": {},
                "plano_saude": {},
            }

            nome = input("Digite seu nome: ")
            clientes[cpf]["nome"] = nome

            sexo = input("Digite seu sexo (1-fem, 2-masc): ")

            if sexo not in ["1", "2"]:
                print("Opção de sexo invalida.\n")
                return

            sexos = {"1": "fem", "2": "masc"}
            sexo = sexos[sexo]
            clientes[cpf]["sexo"] = sexo

            data_nascimento = input(
                "Digite sua data de nascimento (00-00-0000): ",
            )

            data_nascimento, info = validar_data_nascimento(data_nascimento)

            if data_nascimento is None:
                print(info)
                return

            if info < 18:
                print(
                    "Para fazer o cadastro como titular"
                    + " o cliente deve ter mais de 18 anos."
                )
                return

            clientes[cpf]["data_nascimento"] = data_nascimento

            email = input("Digite seu e-mail: ")
            clientes[cpf]["email"] = email

            telefone = input("Digite seu numero de telefone: ")
            clientes[cpf]["telefone"] = telefone

            print(
                "Qual plano deseja cadastrar:"
                + "\n1 - Prata"
                + "\n2 - Ouro"
                + "\n3 - Diamante"
                + "\n4 - Esmeralda"
            )

            opcao = input("Informe o numero: ")

            opcoes = {
                "1": "Prata",
                "2": "Ouro",
                "3": "Diamante",
                "4": "Esmeralda",
            }

            if opcao not in ["1", "2", "3", "4"]:
                print("Opção de plano invalida.\n")
                return

            opcao = opcoes[opcao]
            clientes[cpf]["plano_saude"]["plano"] = opcao

            escolha = input("Você possui algum dependente? (S/N): ")

            if escolha.upper() == "S":
                while True:
                    cpf_dep = input("\nDigite o CPF dele (000.000.000-00): ")
                    cpf_dep, mensagem = validar_cpf(cpf_dep)

                    if cpf_dep is None:
                        print(mensagem)
                        continue

                    clientes[cpf]["terceiros"][cpf_dep] = {}

                    nome_dep = input("Digite o nome dele: ")

                    data_nascimento_dep = input(
                        "Digite a data de nascimento dele (00-00-0000): "
                    )

                    data_nascimento_dep, info = validar_data_nascimento(
                        data_nascimento_dep
                    )

                    if data_nascimento_dep is None:
                        print(info)
                        continue

                    clientes[cpf]["terceiros"][cpf_dep]["nome"] = nome_dep

                    clientes[cpf]["terceiros"][cpf_dep][
                        "data_nascimento"
                    ] = data_nascimento_dep

                    print(
                        "Qual plano deseja cadastrar:"
                        + "\n1 - Prata"
                        + "\n2 - Ouro"
                        + "\n3 - Diamante"
                        + "\n4 - Esmeralda"
                    )

                    opcao = input("Informe o numero: ")

                    opcoes = {
                        "1": "Prata",
                        "2": "Ouro",
                        "3": "Diamante",
                        "4": "Esmeralda",
                    }

                    if opcao not in ["1", "2", "3", "4"]:
                        print("Opção de plano invalida.\n")
                        return

                    opcao = opcoes[opcao]
                    clientes[cpf]["terceiros"][cpf_dep]["plano"] = opcao

                    escolha = input(
                        "Você possui algum outro dependente? (S/N): ",
                    )

                    if escolha.upper() == "S":
                        continue
                    break

            calculo(clientes)
            vencimento(clientes)

            salvar_arquivo(clientes)

        case "2":
            cpf = input("\nDigite o CPF do seu titular (000.000.000-00): ")
            cpf, mensagem = validar_cpf(cpf)

            if cpf is None:
                print(mensagem)
                return

            if cpf not in clientes:
                print("O cliente não está cadastrado!")
                return

            print("Para cadastrar um novo dependente no seu plano:")

            while True:
                cpf_dep = input("\nDigite o CPF dele (000.000.000-00): ")
                cpf_dep, mensagem = validar_cpf(cpf_dep)

                if cpf_dep is None:
                    print(mensagem)
                    continue

                clientes[cpf]["terceiros"][cpf_dep] = {}

                nome_dep = input("Digite o nome dele: ")

                data_nascimento_dep = input(
                    "Digite a data de nascimento dele (00-00-0000): "
                )

                data_nascimento_dep, info = validar_data_nascimento(
                    data_nascimento_dep,
                )

                if data_nascimento_dep is None:
                    print(info)
                    continue

                clientes[cpf]["terceiros"][cpf_dep]["nome"] = nome_dep

                clientes[cpf]["terceiros"][cpf_dep][
                    "data_nascimento"
                ] = data_nascimento_dep

                print(
                    "Qual plano deseja cadastrar:"
                    + "\n1 - Prata"
                    + "\n2 - Ouro"
                    + "\n3 - Diamante"
                    + "\n4 - Esmeralda"
                )

                opcao = input("Informe o numero: ")

                opcoes = {
                    "1": "Prata",
                    "2": "Ouro",
                    "3": "Diamante",
                    "4": "Esmeralda",
                }

                if opcao not in ["1", "2", "3", "4"]:
                    print("Opção de plano invalida.\n")
                    return

                opcao = opcoes[opcao]
                clientes[cpf]["terceiros"][cpf_dep]["plano"] = opcao

                escolha = input(
                    "Você possui algum outro dependente? (S/N): ",
                )

                if escolha.upper() == "S":
                    continue
                break

            calculo(clientes)
            vencimento(clientes)

            salvar_arquivo(clientes)

        case _:
            print("Opção invalida.\n")


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
                if apenasletras.isalpha():
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
                apenasletras = input("Informe o novo nome do dependente: ")
                if apenasletras.isalpha():
                    editar[cpf]["terceiros"][quero_editar2]["nome"] = apenasletras
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
                data, erro = validar_data_nascimento(apenasnumeros)
                if data is None:
                    print(erro)
                    return
                editar[cpf]["terceiros"][quero_editar2]["data_nascimento"] = data
                print("Alteração feita com sucesso!")

            case _:
                print("Opção Invalida.\n")
                return

        salvar_arquivo(editar)

    else:
        print("Desculpe, o CPF informado não foi encontrado!")


# Marcos
def remover():
    dados = ler_arquivo()
    esc1 = input("1 - Excluir um cliente\n2 - Excluir um Terceiro de um cliente")
    if esc1 == "1":
        cpf = input("Informe o cpf do cliente que deseja excluir: ")
        if cpf in dados:
            del dados[cpf]
        else:
            print("vc digitou um cpf inexistente ")
    elif esc1 == "2":
        cpf = input("Informe o cpf do cliente que deseja excluir o terceiro: ")
        if cpf in dados:
            cpft = input("Informe o cpf do terceiro que deseja excluir: ")
            if cpft in dados[cpf]["terceiros"]:
                del dados[cpf]["terceiros"][cpft]
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
    plano = input("Informe o plano de saúde que deseja listar os clientes: \n1 - Diamante\n2 - Ouro\n3 - Prata\n4 - Esmeralda\n")
    esc = (1 if plano == "1" else 2 if plano == "2" else 3 if plano == "3" else 4 if plano == "4" else 0)

    if esc == 0:
        print("você digitou algo de errado")
        return

    elif esc == 1:
        print("Diamante")
        print(f"{"CPF":<14}¦ {"Nome":<12}¦ {"Sexo":<5}¦ {"E-mail":<20}¦ {"Data Nasc.":<10}¦ {"Telefone":<10}¦ {"Plano":<10}¦ {"Valor":<10}\n-------------------------------------------------------------------------")

        for chave, item in dados.items():
            if item["plano_saude"]["plano"] == "Diamante":
                print(f"{chave:<14}¦ {item['nome']:<12}¦ {item['sexo']:<5}¦ {item['email']:<20}¦ {item['data_nascimento']:<10}¦ {item['telefone']:<10}¦ {item['plano_saude']['plano']:<10}¦ {item['plano_saude']['valor']:<10.2f}")
    elif esc == 2:
        print("Ouro")
        print(f"{"CPF":<14}¦ {"Nome":<12}¦ {"Sexo":<5}¦ {"E-mail":<20}¦ {"Data Nasc.":<10}¦ {"Telefone":<10}¦ {"Plano":<10}¦ {"Valor":<10}\n-------------------------------------------------------------------------")
        for chave, item in dados.items():
            if item["plano_saude"]["plano"] == "Ouro":
                print(
                    f"{chave:<14} ¦ {item['nome']:<12} ¦ {item['sexo']:<5} ¦ {item['email']:<20} ¦ {item['data_nascimento']:<10} ¦ {item['telefone']:<10} ¦ {item['plano_saude']['plano']:<10} ¦ {item['plano_saude']['valor']:<10.2f}"
                )
    elif esc == 3:
        print("Prata")
        print(f"{"CPF":<14}¦ {"Nome":<12}¦ {"Sexo":<5}¦ {"E-mail":<20}¦ {"Data Nasc.":<10}¦ {"Telefone":<10}¦ {"Plano":<10}¦ {"Valor":<10}\n-------------------------------------------------------------------------")

        for chave, item in dados.items():
            if item["plano_saude"]["plano"] == "Prata":
                print(
                    f"{chave:<14} ¦ {item['nome']:<12} ¦ {item['sexo']:<5} ¦ {item['email']:<20} ¦ {item['data_nascimento']:<10} ¦ {item}{['telefone']:<10} ¦ {item['plano_saude']['plano']:<10} ¦ {item['plano_saude']['valor']:<10.2f}"
                )
    elif esc == 4:
        print("Esmeralda")
        print(f"{"CPF":<14}¦ {"Nome":<12}¦ {"Sexo":<5}¦ {"E-mail":<20}¦ {"Data Nasc.":<10}¦ {"Telefone":<10}¦ {"Plano":<10}¦ {"Valor":<10}\n-------------------------------------------------------------------------")

        for chave, item in dados.items():
            if item["plano_saude"]["plano"] == "Esmeralda":
                print(
                    f"{chave:<14} ¦ {item['nome']:<12} ¦ {item['sexo']:<5} ¦ {item['email']:<20} ¦ {item['data_nascimento']:<10} ¦ {item['telefone']:<10} ¦ {item['plano_saude']['plano']:<10} ¦ {item['plano_saude']['valor']:<10.2f}"
                )


def listagem_geral():
    dados = ler_arquivo()
    print(f"{"CPF":<14}¦ {"Nome":<12}¦ {"Sexo":<5}¦ {"E-mail":<20}¦ {"Data Nasc.":<10}¦ {"Telefone":<10}¦ {"Plano":<10}¦ {"Valor":<10}\n-------------------------------------------------------------------------")

    for chave, item in dados.items():
        if item["plano_saude"]["plano"] == "Diamante":
            print(
                f"{chave:<14} ¦ {item['nome']:<12} ¦ {item['sexo']:<5} ¦ {item['email']:<20} ¦ {item['data_nascimento']:<10} ¦ {item['telefone']:<10} ¦ {item['plano_saude']['plano']:<10} ¦ {item['plano_saude']['valor']:<10.2f}"
            )


def data_por_vecimento():
    dados = ler_arquivo()
    print(f"{"CPF":<14}¦ {"Nome":<12}¦ {"Sexo":<5}¦ {"E-mail":<20}¦ {"Data venc.":<10}¦ {"Telefone":<10}¦ {"Plano":<10}¦ {"Valor":<10}\n-------------------------------------------------------------------------")

    for chave, item in dados.items():
        lista = item["plano_saude"]["data_vencimento"].split("-")
        (
            print(f"{chave:<14} ¦ {item['nome']:<12} ¦ {item['sexo']:<5} ¦ {item['email']:<20} ¦ {item['plano_saude']["data_vencimento"]:<10} ¦ {item['telefone']:<10} ¦ {item['plano_saude']['plano']:<10} ¦ {item['plano_saude']['valor']:<10.2f}")
            if int(lista[1]) <= 5
            else None
        )


def cpf():
    dados = ler_arquivo()
    cpf = input("Digite seu CPF: ")
    cpf, err = validar_cpf(cpf)

    if cpf is None:
        print(err)
        return

    print(f"{"Nome":<12}¦ {"Sexo":<5}¦ {"E-mail":<20}¦ {"Data nasc.":<12}¦ {"Telefone":<10}¦ {"Plano":<10}¦ {"Valor":<10}¦ {"Data venc.":<10}\n-------------------------------------------------------------------------")

    for chave, item in dados.items():
        if chave == cpf:
            print(
                f"{item['nome']:<12} ¦ {item['sexo']:<5} ¦ {item['email']:<20} ¦ {item['data_nascimento']:<12} ¦ {item['telefone']:<10} ¦ {item['plano_saude']['plano']:<10} ¦  {item['plano_saude']['valor']:<10} ¦ {item['plano_saude']['data_vencimento']}"
            )
