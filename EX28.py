import random

numeroAleatorio = random.randint(0, 5)
print("Que tal joguarmos um pouco? Consegue descobrir o numero que estou pensando?")


numeroEscolhidoPeloUsuario = int(input("Diga o numero que estou pensando: "))

if numeroAleatorio == numeroEscolhidoPeloUsuario:
    print("Voce acertou, parabens!!")
else:
    print("Errou jogue novamente! Eu estava pensando em {}".format(numeroAleatorio))    


