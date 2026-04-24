from calendar import monthrange
from datetime import datetime


def validar_cpf(cpf):
    if len(cpf) == 14 and cpf[3] == "." and cpf[7] == "." and cpf[11] == "-":
        nums = cpf.replace(".", "").replace("-", "")

        if not nums.isdigit() or len(nums) != 11:
            return None, f"O cpf {cpf} possui caracteres inválidos."

        return str(nums), None

    else:
        return None, f"O formato do cpf: {cpf}, é invalido."


def validar_data_nascimento(data_nascimento):
    if (
        len(data_nascimento) != 10
        or data_nascimento[2] != "-"
        or data_nascimento[5] != "-"
    ):
        return None, "Formato da data de nascimento inválido. Use DD-MM-AAAA."

    dia_str, mes_str, ano_str = data_nascimento.split("-")

    if not (dia_str.isdigit() and mes_str.isdigit() and ano_str.isdigit()):
        return None, "A data de nascimento contém caracteres inválidos."

    dia = int(dia_str)
    mes = int(mes_str)
    ano = int(ano_str)

    if not (1 <= mes <= 12):
        return None, f"A data {data_nascimento} é inválida (mês inexistente)."

    data_hoje = datetime.now()
    dia_atual = data_hoje.day
    mes_atual = data_hoje.month
    ano_atual = data_hoje.year

    if not (ano <= ano_atual):
        return (
            None,
            f"A data {data_nascimento} é inválida "
            + f"(o ano deve ser menor ou igual ao atual: {ano_atual}).",
        )

    _, dias_no_mes = monthrange(ano, mes)
    if not (1 <= dia <= dias_no_mes):
        return None, f"A data {data_nascimento} é inválida (dia inexistente)."

    idade = ano_atual - ano

    if (mes_atual < mes) or (mes_atual == mes and dia_atual < dia):
        idade -= 1

    return data_nascimento, idade
