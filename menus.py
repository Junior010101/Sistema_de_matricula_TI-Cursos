from logica import validar_cpf, validar_data_nascimento
from percistencia import ler_arquivo, salvar_arquivo


def cadastrar_cliente():
    clientes = ler_arquivo()
    breakpoint()

    print("1 - Titular\n2 - Dependente\n")
    pergunta = input("Você deseja se cadastrar como titular ou dependente: ")

    match pergunta:
        case "1":
            cpf = input("\nDigite seu CPF (000.000.000-00): ")
            cpf, mensagem = validar_cpf(cpf)

            if cpf is None:
                print(mensagem)
                return

            nome = input("Digite seu nome: ")

            sexo = input("Digite seu sexo (1-fem, 2-masc): ")

            if sexo not in ["1", "2"]:
                print("Opção de sexo invalida.\n")
                return

            sexos = {"1": "fem", "2": "masc"}
            sexo = sexos[sexo]

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

            email = input("Digite seu e-mail: ")
            telefone = input("Digite seu numero de telefone: ")

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

            escolha = input("Você possui algum dependente? (S/N): ")

            if escolha.upper() == "S":
                while True:
                    cpf_dep = input("\nDigite seu CPF (000.000.000-00): ")
                    cpf_dep, mensagem = validar_cpf(cpf_dep)

                    if cpf_dep is None:
                        print(mensagem)
                        return

            # valor, data_vencimento = calculo_de_mensalidade(sexo, idade, num_dependentes)

        case "2":
            pass

        case _:
            print("Opção invalida.\n")

#thiago
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
            case "3":
                editar[cpf]["email"] = input("Informe o novo E-mail: ")
            case "4":
                editar[cpf]["data_nascimento"] = input("Informe a nova data de nascimento: ")
            case "5":
                editar[cpf]["telefone"] = input("Informe o novo telefone: ")
            case "6":
                quero_editar2= input("Informe o CPF do dependente que você quer editar: ")
                editar[cpf]["terceiros"][quero_editar2]["nome"] = input("Informe o novo nome do dependente: ")
            case "7":
                quero_editar2= input("Informe o CPF do dependente que você quer editar: ")
                editar[cpf]["terceiros"][quero_editar2]["data_nascimento"] = input("Informe a nova data de nascimento: ")
        return salvar_arquivo(editar)        
    else:
        print("Desculpe, o CPF informado não foi encontrado!")
