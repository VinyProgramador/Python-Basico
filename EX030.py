numeroDigitado = int(input("Digite um numero para saber se ele é impar ou par:"))
resultado = numeroDigitado % 2 
if resultado == 0:
    print("Numero par!")
else:
    print("Numero ímmpar!")