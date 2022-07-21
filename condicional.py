import math

#nome = str(input("Digite seu nome: ")).upper()
#if nome == "VINICIUS":
#   print("Nome bonito!")
#else :
#    print("Voce não é oo Viny!")

#exemplo 02

n1 = float(input("Digite sua Primeira nota: "))
n2 = float(input("Digite sua Segunda nota: "))
n3 = float(input("Digite sua Terceira nota: "))

mediaFinal = (n1+n2+n3)/3

if mediaFinal >=6:
    print("Paasou de ano! Com a media de {:.2f}".format(mediaFinal))
else :
    print("Infelizmente vai ter que refazer o semestre!! Sua media foi de {:.2f}".format(mediaFinal))    