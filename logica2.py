from percistencia import salvar_arquivo, ler_arquivo
#• Clientes do sexo feminino maior/igual de 13 anos e menor de 35 anos, acrescentar no valor
#total do plano de saúde 30% a ser pago.
#• Clientes que possuem mais de 1 (hum) dependente cadastrado tem 20% de desconto no valor
#TOTAL a ser pago. Sendo assim, o sistema deve permitir que o cliente possa ter mais de um
#dependente cadastrado.
#• Clientes menor que 13 anos, tem 30% de desconto no valor total a ser pago.
#• Clientes maior/igual de 60 anos, acrescentar no valor base do plano de saúde 40% no valor
#total a ser pago.
#• Editar
#• Remover
#• Listar Geral: neste módulo será feita a listagem de todos os clientes com suas respectivas
#informações, conforme tela apresentada abaixo.

def calculo():
    dados = ler_arquivo()
    for chave, item in dados.items():
        idade = dados[chave]["data_nascimento"].split("-")
        if dados[chave]["plano_saude"]["plano"] == "Diamante":
            if dados[chave]["sexo"] == "fem" and (int(idade[2]) > (2026 - int(idade[2])) >= 13) and ((2026 - int(idade[2])) <= 35):
                dados[chave]["plano_saude"]["valor"] = 400 + (400 * 0.3) 
            if len(dados[chave]["terceiros"]) > 1:
                dados[chave]["plano_saude"]["valor"] = 800 - (800 * 0.2) 
            if (2026 - int(idade[2])) < 13:
                dados[chave]["plano_saude"]["valor"] = 400 - (400 * 0.3) 
            if (2026 - int(idade[2])) >= 60:
                dados[chave]["plano_saude"]["valor"] = 400 - (400 * 0.4) 
                
calculo()

