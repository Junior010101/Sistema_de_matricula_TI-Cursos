from pathlib import Path

ROOT = Path.cwd()

df = open(ROOT / "basededados.csv", "r")
print(df)

while True:
    # -=-=-=-=-=- tela inicial =-=-=-=-=
    print(
        "\nTI Cursos\n1 - Cadastrar Aluno\n2 – Editar Aluno\n3 – Remover Aluno\n4 - Listagem Geral\n5 – Listagem por Curso\n6 – Listagem por sexo\n0 – Sair"
    )
    try:
        esco1 = int(input("Selecione ação: "))
    except ValueError:
        print("Digite um número válido!")
        continue
    # =-=-=-=-=-=-= Escolha 1 =-=-=-=-=-=
    if esco1 == 1:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("\n\nCadastro\n")
        nome = input(
            "Nome: "
        )  # Nota: se o nome do aluno for igual a outro ele sobreescreve se alguem puder ajeitar agradeço
        matricula = input("matricula:")
        sexo = input("Sexo(1-fem/2-mas):")
        idade = input("idade:")
        turno = input("Turno(1-manha/2-noite):")
        curso = input("Curso(1-PHP/2-Java/3-Delphi):")
        df.loc[len(df)] = {
            "Nome": nome,
            "matricula": matricula,
            "sexo": "feminino" if sexo == "1" else "masculino",
            "idade": idade,
            "turno": "Manhã" if turno == "1" else "noite",
            "curso": "PHP" if curso == "1" else "Java" if curso == "2" else "Delphi",
        }
        print(df)
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
