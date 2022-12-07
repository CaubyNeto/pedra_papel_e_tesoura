import random

opcoes = ["pedra", "papel", "tesoura"]
ganhos_do_computador = 0
ganhos_do_usuario = 0

while True:
    computador = random.choice(opcoes)
    usuario = input("Digite pedra/papel/tesoura ou sair para sair ")
    if usuario == "sair":
        if ganhos_do_computador > 0 or ganhos_do_usuario > 0:
            print("Você ganhou ", ganhos_do_usuario, " vezes")
            print("O computador ganhou ", ganhos_do_computador, " vezes")
        print("Adeus!")
        break

    print("O computador escolheu ", computador, ".")
    if usuario != computador:
        if usuario == "pedra" and computador == "tesoura":
            print("Você ganhou!")
            ganhos_do_usuario += 1
            continue
        elif usuario == "papel" and computador == "pedra":
            print("Você ganhou!")
            ganhos_do_usuario += 1
            continue
        elif usuario == "tesoura" and computador == "papel":
            print("Você ganhou!")
            ganhos_do_usuario += 1
            continue
        else:
            print("Você perdeu!")
            ganhos_do_computador += 1
            continue
    else:
        print("Igual!")


