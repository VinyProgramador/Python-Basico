from numpy import var

velocidadeCarro = int(input("Qual é a velocidade que estava seu carro? "))
if velocidadeCarro > 80:
    print("Voce ultrapassou a velocidade permitida e pagara um multa de: {}R$".format((velocidadeCarro-80)*7))
print("Ok, tenha um bom dia e dirija com segurança")