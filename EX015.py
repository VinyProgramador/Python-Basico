dias = float(input('Quantos dias o Carro ficou ficou alugado?:'))
km = float(input('Quantos Km o carro percorreu?:'))
pago = (dias* 60) +(km*0.15)
input('O valor a pagar é R${:.2f}'.format(pago))