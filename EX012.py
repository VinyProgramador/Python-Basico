produto = float(input('Digite o Valor do produto para Ter um desconto de 5%: '))
desconto = produto - (produto* 5 /100)
print ('O valor do seu produto era de {}R$, E com desconto o valor passa a ser {}R$.'.format(produto,desconto))