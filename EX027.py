nomeUsuario = str(input("Digite seu nome completo: ")).strip()
nomeFinal = nomeUsuario.split()
print("Seu Primeiro nome é: {}".format(nomeFinal[0]))
print("Seu Ultimo nome é: {}".format(nomeFinal[1]))