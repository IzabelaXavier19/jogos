# Mostre os números pares da lista
def numerosPares(numeros):
    print("Os números pares são: ")
    for numero in numeros:
        if numero % 2 == 0:
            print(numero, end=" ")

# Mostre os números impares da lista
def numerosImpares(numeros):
    print("Os números ímpares são: ")
    for numero in numeros:
        if numero % 2 != 0:
            print(numero, end=" ")

# Mostre os números Positivos da lista
def numerosPositivos(numeros):
    print("Os números Positivos são: ")
    for numero in numeros:
        if numero > 0:
            print(numero, end=" ")
# Mostre os números Negativos da lista
def numerosNegativos(numeros):
    print("Os números Negativos são: ")
    for numero in numeros:
        if numero < 0:
            print(numero, end=" ")
# Mostre os números Zeros da lista
def numerosZeros(numeros):
    print("Os números Zeros são: ")
    for numero in numeros:
        if numero == 0:
            print(numero, end=" ")


numeros=[0,0,0,0,0,0,0,0,0,0]
# Peça ao usuário para inserir 10 números
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros[i]=numero
while True:
    print  ("""
                Opções:  
                [1] Todos os números Ímpares 
                [2] Todos os números Pares 
                [3] Todos os números Positivos
                [4] Todos os números Negativos
                [5] Todos os números Zeros
                [6] Sair
                """)

    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        numerosImpares(numeros)
    elif opcao == 2:
        numerosPares(numeros)
    elif opcao == 3:
        numerosPositivos(numeros)
    elif opcao == 4:
        numerosNegativos(numeros)
    elif opcao == 5:
            numerosZeros(numeros)
    else:
        break

