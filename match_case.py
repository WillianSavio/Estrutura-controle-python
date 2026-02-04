
# Calculadora simples

'''
Qual é a lógica da calculadora?

Precisa de valores ( números)

1. ETAPA - Entrada:
O usuário precida digitar no mínimo dois numeros ou mais

O usuário precida falar qual operação irá usar

2. ETAPA - Processamento:
Realizar as operações matemáticas ( +, -, *, / )


3. ETAPA - Saída:
Exibir o resultado da operação

STRING = "TEXTO"
INT = 10, 17, 20
FLOAT = 12.12, 10.50
BOOLEAN = TRUE OU FALSE
'''
print(" === Bem vindo!! Calculadora do Senac === ")

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))
operador = input("Digite o operador: ")

match operador: 
    case "+":
        print(" O resultado é:", (primeiro_numero) + (segundo_numero))
    case "-":
        print(" O resultado é", (primeiro_numero) - (segundo_numero))
    case "*":
        print(" O resultado é", (primeiro_numero) * (segundo_numero))
    case "/":
        if segundo_numero == 0:
            print (" === ISSO NÃO PODE === ")
        else:
            print(" O resultado é:", (primeiro_numero) / (segundo_numero))
    case _:
        print(" Operação invalida")
    
        

