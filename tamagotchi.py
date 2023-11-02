from tamagotchi1 import *

while True:
    pessoa1=Pessoa("João",50,20)
    print("""Menu: 
          [1] Dormir
          [2] Acordar 
          [3] Comer
          [4] Parar de comer
          [5] Andar
          [6] Parar de andar
          [7] Sair""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        pessoa1.dormir()
    elif opcao == "2":
        pessoa1.acordar()
    elif opcao == "3":
        comida = input("Digite o que você vai comer: ")
        pessoa1.comer(comida)
    elif opcao == "4":
        pessoa1.parardecomer()
    elif opcao == "5":
        pessoa1.andar()
    elif opcao == "6":
        pessoa1.parardeandar()
    elif opcao == "7":
        break
        #falta fazer com que ele consulte a resposta anterior

print("Programa finalizado")
