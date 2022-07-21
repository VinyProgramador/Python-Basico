distancia = int(input("Digite a ditancia da viagem: "))

if distancia <=200:
    print("Voce pagara {}".format(distancia*0.50))
else:
    print("Voce pagara {}".format(distancia*0.45))
