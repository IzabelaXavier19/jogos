from time import sleep
for x in range(3):
    print  ("""Opções:  
            [1] Pedra 
            [2] Papel 
            [3] Tesoura 
            """)
    jogador1 = int(input("1 jogador, escolha uma opção: "))
    jogador2 = int(input("2 jogador, escolha uma opção: "))
    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!")
    if jogador1 == jogador2:
        print("EMPATE")
    elif jogador1 == 1: #Pedra
        if jogador2 == 2:
            print("2 JOGADOR VENCEU!!!")
        elif jogador2 == 3:
            print("1 JOGADOR VENCEU!!!")
        else:
            print("Jogada invalida.")
    elif jogador1 == 2:  # Papel
        if jogador2 == 1:
            print("1 JOGADOR VENCEU!!!")
        elif jogador2 == 3:
            print("2 JOGADOR VENCEU!!!")
        else:
            print("Jogada invalida.")
    elif jogador1 == 3:  # Tesoura
        if jogador2 == 1:
            print("1 JOGADOR VENCEU!!!")
        elif jogador2 == 2:
            print("2 JOGADOR VENCEU!!!")
        else:
            print("Jogada invalida.")
    else:
        print("Jogada invalida.")



