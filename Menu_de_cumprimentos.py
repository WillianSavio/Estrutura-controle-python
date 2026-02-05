'''
Você foi contrato para criar um menu interativo de mensagens de cumprimento.
 
Se o usuário entrar com a letra M ou palavra Manhã, deve mostrar a mensagem "Bom dia e o nome da pessoa!"
Se o usuário entrar com a letra T ou palavra Tarde, deve mostrar a mensagem "Boa tarde e o nome da pessoa!"
Se o usuãrio entrar com a letra N ou palavra Noite, deve mostrar a mensagem "Boa noite eo nome da pessoa!"Docstring for Menu_de_cumprimentos


'''
'''
usuario = nome da pessoa
periodo = Periodo que a pessoa está ( manhã, tarde, noite )

'''
# ENTRADA DE INFORMAÇÃO
usuario = input(" Digite o seu nome: ")
periodo = input(" Digite o periodo: ")


match periodo:
    case "M" | "Manhã":
        print(" Bom dia, seu", usuario)
    case "T" | "Tarde":
        print(" Boa tarde, seu", usuario)
    case "N" | "Noite":
        print(" Boa noite seu", usuario)
    case _:
        print(" Periodo desconhecido!!")
        

        




