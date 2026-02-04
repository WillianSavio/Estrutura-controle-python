
# VARIAVEIS

primeira_opção = ("FALAR COM ATENDENTE")
segunda_opção = (" SEGUNDA VIA BO BOLETO ")
terceira_opção = (" CANCELAR SERVIÇO ")
quarta_opção = (" INFORMAÇÕES SOBRE PLANOS ")
quinta_opção = (" SAIR ")
opção_desejada = (" DIGITE A OPÇÃO DESEJADA: ")





print(" === BEM VINDO A SESSÃO DE ATENDIMENTO ===")

print(" === ESCOLHA A OPÇÃO DESEJADA:")

print (" 1 - FALAR COM ATENDENTE ")
print (" 2 - SEGUNDA VIA DE BOLETO ")
print (" 3 - CANCELAR SERVIÇO ")
print (" 4 - INFORMAÇÕES SOBRE PLANOS ")
print (" 5 - SAIR ")

opção_desejada = input (" DIGITE A OPÇÃO DESEJADA: ")

match opção_desejada:
    case "1":
        print(" === AGUARDE, O ATENDENTE ESTARÁ DISPONÍVEL EM BREVE === ")
    case "2":
        print(" === SEU BOLETO SERÁ ENCAMINHADO POR E-MAIL === ")
    case "3":
        print(" === SEU SERVIÇO ESTÁ SENDO CANCELADO === ")
    case "4":
        print(" === AUMENTO NA FATURA === ")
    case "5":
        print(" === OBRIGADO, ATÉ BREVE === ")
    case _:
        print(" === OPÇÃO INVALIDA ===")
        

    

