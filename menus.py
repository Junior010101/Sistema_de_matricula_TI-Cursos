from logica import validar_cpf, validar_data_nascimento
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

                    escolha = input(
                        "Você possui algum outro dependente? (S/N): ",
                    )

                    if escolha.upper() == "S":
                        continue

                    break

            num_dependentes = len(clientes[cpf]["terceiros"])
            # valor, data_vencimento = calcular_mensalidade(
            #   sexo,
            #   idade,
            #   num_dependentes,
            # )

            # valor e data_vencimento decorativos:
            valor = 350.75 * (num_dependentes * 0.2)
            data_vencimento = "10-05-2026"

            clientes[cpf]["plano_saude"]["valor"] = valor
            clientes[cpf]["plano_saude"]["data_vencimento"] = data_vencimento

            salvar_arquivo(clientes)

        case "2":
            cpf = input("\nDigite seu CPF (000.000.000-00): ")
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

                escolha = input(
                    "Você possui algum outro dependente? (S/N): ",
                )

                if escolha.upper() == "S":
                    continue

                break

            num_dependentes = len(clientes[cpf]["terceiros"])

            _, idade = validar_data_nascimento(
                clientes[cpf]["data_nascimento"],
            )

            # valor, data_vencimento = calcular_mensalidade(
            #   clientes[cpf]["sexo"],
            #   idade,
            #   num_dependentes,
            # )

            valor = 350.75 * (num_dependentes * 0.2)
            data_vencimento = "10-05-2026"

            clientes[cpf]["plano_saude"]["valor"] = valor
            clientes[cpf]["plano_saude"]["data_vencimento"] = data_vencimento

            salvar_arquivo(clientes)

        case _:
            print("Opção invalida.\n")


# thiago
def editar_cliente():
    editar = ler_arquivo()

    cpf = input("Informe o CPF que deseja alterar: ")

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
                editar[cpf]["nome"] = input("Informe o novo nome: ")

            case "2":
                editar[cpf]["sexo"] = input("Informe o novo sexo: ")
                # Lembrete de marcondes para layme: Quando santos fizer o
                # calcular_mensalidade você deve atualizar o valor e a data de
                # vencimento dentro de plano_saude

            case "3":
                editar[cpf]["email"] = input("Informe o novo E-mail: ")

            case "4":
                editar[cpf]["data_nascimento"] = input(
                    "Informe a nova data de nascimento: "
                )
                # Lembrete de marcondes para layme: Quando santos fizer o
                # calcular_mensalidade você deve atualizar o valor e a data de
                # vencimento dentro de plano_saude

            case "5":
                editar[cpf]["telefone"] = input("Informe o novo telefone: ")

            case "6":
                quero_editar2 = input(
                    "Informe o CPF do dependente que você quer editar: "
                )
                editar[cpf]["terceiros"][quero_editar2]["nome"] = input(
                    "Informe o novo nome do dependente: "
                )

            case "7":
                quero_editar2 = input(
                    "Informe o CPF do dependente que você quer editar: "
                )
                editar[cpf]["terceiros"][quero_editar2]["data_nascimento"] = (
                    input("Informe a nova data de nascimento: "),
                )

            case _:
                print("Opção Invalida.\n")
                return

        return salvar_arquivo(editar)

    else:
        print("Desculpe, o CPF informado não foi encontrado!")

#Marcos
def remover():
    dados = ler_arquivo()
    esc1 = input("1 - Excluir um cliente\n2 - Excluir um Terceiro de um cliente")
    if esc1 == "1":
        cpf = input("Iforme o cpf do cliente que deseja exculir")
        if cpf in dados:
            del dados[cpf]
        else: 
            print("vc digitou um cpf inexistente ")
    elif esc1 == "2":
        cpf = input("Iforme o cpf do cliente que deseja exculir o terceiro")
        cpft = input("Iforme o cpf do terceiro que deseja exculir")
        if cpf in dados:
            if cpft in dados[cpf]["terceiros"]:
                del dados[cpf]["terceiros"][cpft]
        else: 
            print("vc digitou um cpf inexistente ")
    else:
        print("você digitou algo de errado")
