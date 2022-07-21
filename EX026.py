frase = str (input("Digite a frase: ")).upper().strip()
print("A letra aparece {}x na frase! ".format(frase.count("A")))
print("A primeira letra foi encontrada na posicão: {}".format(frase.find("A")+1))
print("E a ultima letra A esta na posição: {}".format(frase.rfind("A")+1))