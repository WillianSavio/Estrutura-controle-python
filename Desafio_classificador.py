'''
1.Pedir ao jogador quantos pontos de experiência ele tem (XP):
 
Menos de 100 → "Iniciante"
 
Entre 100 e 500 → "Intermediário"
 
Mais de 500 → "Veterano"
 
Use if/elif/else para essa classificação.
 
2. Depois, o programa deve perguntar qual ação o jogador deseja executar (usar match case):
 
"A" → Atacar
 
"D" → Defender
 
"F" → Fugir
 
Qualquer outra tecla → "Ação inválida"
 
Mostre uma mensagem apropriada para cada ação, como:
 
"Você avançou para o ataque!"
 
"Você levantou o escudo!"
 
"Você fugiu da batalha!"

'''
print(" BEM VINDO AO JOGO")

#Vaviaveis
experiencia = int(input (" Digite a sua pontuação de experiência de jogo: "))



match experiencia:
    case experiencia:
          
        if experiencia <=99:
            print(" === Você é um jogador INICIANTE ===")
        elif experiencia <=499:
            print(" === Você é um jogador INTERMEDIARIO ===")
        else:
            print(" === Você é um jogador VETERANO ===")

#variaveis
ação = print("Qual ação você deseja executar?:")
print("A - ATACAR")
print("D - DEFENDER")
print("F - FUGIR")

ação = input("escolha uma opção:")


match ação:
    case "A":
        print("=== VOCê AVANÇOU PARA O ATAQUE!! ===")
    case "D":
        print("=== VOCÊ LEVANTOU O ESCUDO ===")
    case "F":
        print("=== VOCÊ FUGIU DA BATALHA ===")
    case _:
        print("=== AÇÃO INVALIDA ===")









