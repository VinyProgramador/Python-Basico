#Passo a Passo
#1- importar a base de Dados
#2-Vizualizar a base Dados 
#3- Tratamento da base de Dados ,arrumar as cagadas no arquivo.
#4-Analise inicial "ver o pq dos cancelamentos"
#5-Olhar a caracteristica do cliente , e ver o porque do Cancelamento.
#===========================================================================#

#passo-1
import how
from displayfunction import display
import pandas as pd
tabela = pd.read_csv("telecom_users.csv")

#passo-2 
display(tabela)

#passo-3 
tabela =tabela.drop('Unnamed: 0', axis=1)
print(tabela.info())

tabela['TotalGasto '] = pd.to_numeric(tabela,['TotalGasto '], errors="coerce")
print(tabela.info())
tabela =tabela.drop(how='all',axis=1)
tabela =tabela.drop(how='any',axis=0)
print(tabela.info())

#passo4
display(tabela["Churn"].value_counts())
display(tabela['Churn'].value_counts(normalize=True))
 
#passo5
import plotly.express as px 
grafico =px.histogram(tabela,x="MesesComoCliente",color='Churn')
grafico.show



