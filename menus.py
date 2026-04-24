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


cadastrar_cliente()
# def listar_por_curso():
#     alunos = ler_arquivo()

#     print("\nFiltrar por curso:")
#     print("1 - PHP")
#     print("2 - Java")
#     print("3 - Delphi")

#     curso = int(input("Escolha: "))

#     cursos = {1: "PHP", 2: "Java", 3: "Delphi"}
#     curso = cursos[curso]

#     print("\n=== LISTAGEM POR CURSO ===")

#     for matricula, aluno in alunos.items():
#         if curso in aluno["cursos"]:
#             cursos_nome = [c for c in aluno["cursos"]]
#             mensalidade = float(aluno["mensalidade"])

#             print(
#                 f"""
# Matricula: {matricula}
# Nome: {aluno['nome']}
# Sexo: {"F" if aluno['sexo'] == "1" else "M"}
# Idade: {aluno['idade']}
# Cursos: {' / '.join(cursos_nome)}
# Mensalidade: R$ {mensalidade:.2f}
# --------------------------
# """
#             )
#     input("Pressione ENTER para voltar...")


# def listar_por_sexo():
#     alunos = ler_arquivo()

#     print("\nFiltrar por sexo:")
#     print("1 - Feminino")
#     print("2 - Masculino")

#     sexo = int(input("Escolha: "))

#     sexo_list = {1: "F", 2: "M"}
#     sexo = sexo_list[sexo]

#     print("\n=== LISTAGEM POR SEXO ===")

#     for matricula, aluno in alunos.items():
#         if aluno["sexo"] == sexo:
#             cursos_nome = [c for c in aluno["cursos"]]
#             mensalidade = float(aluno["mensalidade"])

#             print(
#                 f"""
# Matricula: {matricula}
# Nome: {aluno['nome']}
# Sexo: {"F" if aluno['sexo'] == "1" else "M"}
# Idade: {aluno['idade']}
# Cursos: {' / '.join(cursos_nome)}
# Mensalidade: R$ {mensalidade:.2f}
# --------------------------
# """
#             )
#     input("Pressione ENTER para voltar...")


# def editar_aluno():
#     alunos = ler_arquivo()
#     matricula = input("\nDigite a matricula do aluno a ser editado: ")

#     if matricula in alunos:
#         aluno = alunos[matricula]

#         nome = input(f"Nome atual: {aluno['nome']}. Digite o novo ou (N): ")
#         if nome.upper() != "N":
#             aluno["nome"] = nome

#         sexo = input(f"Sexo atual: {aluno['sexo']}. Digite o novo ou (N): ")
#         if sexo.upper() != "N":
#             aluno["sexo"] = sexo

#         idade = input(f"Idade atual: {aluno['idade']}. Digite a nova ou (N): ")
#         if idade.upper() != "N":
#             aluno["idade"] = int(idade)

#         turno_atual = aluno["turno"]
#         contraturno = "Manhã" if turno_atual == "Tarde" else "Tarde"

#         mudar_turno = input(
#             f"Turno atual: {turno_atual}. Mudar para {contraturno}? (S/N): "
#         )
#         if mudar_turno.upper() == "S":
#             aluno["turno"] = contraturno

#         while True:
#             print(f"Cursos atuais: {aluno['cursos']}")
#             remover = input("Digite o curso para remover ou (N) para sair: ")
#             if remover.upper() == "N":
#                 break
#             if remover in aluno["cursos"]:
#                 aluno["cursos"].remove(remover)
#             else:
#                 print("Curso não encontrado.")

#         opcoes = {"1": "PHP", "2": "Java", "3": "Delphi"}
#         while True:
#             print("\nCursos disponíveis: (1-PHP / 2-Java / 3-Delphi)")
#             escolha = input(
#                 "Digite o número do curso"
#                 + " que deseja adicionar ou (N) para nenhum: "
#             )

#             if escolha.upper() == "N":
#                 break

#             if escolha in opcoes:
#                 curso_nome = opcoes[escolha]

#                 if curso_nome not in aluno["cursos"]:
#                     aluno["cursos"].append(curso_nome)
#                     print(f"Curso {curso_nome} adicionado!")
#                 else:
#                     print(f"O aluno já está matriculado em {curso_nome}.")
#             else:
#                 print("Opção inválida!")

#             continuar = input("\nDeseja cadastrar um outro curso (S ou N): ")
#             if continuar.upper() != "S":
#                 break

#         editar_arquivo(alunos)
#         print("Alterações realizadas com sucesso!")
#     else:
#         print(
#             f"O aluno cuja a matricula é {matricula},"
#             + " não está cadastrado no sistema."
#         )


# def remover_aluno():
#     pass
