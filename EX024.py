#Exemplo abaixo feiro por mim usando a função split()

#palavra = str(input("informe tres palavras: "))
#print("A primeira palavra é: {}".format(palavra.split()[0]))
#print("A segunda palavra é: {}".format(palavra.split()[1]))
#print("A terceira palavra é: {}".format(palavra.split()[2]))


#a função strip() elimina os espaços

cidade = str(input("Informe a cidade que voce nasceu: ")).strip()
print(cidade[:3].upper() == 'SAO')
