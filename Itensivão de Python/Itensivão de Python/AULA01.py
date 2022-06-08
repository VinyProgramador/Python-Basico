import displayfunction
from sys import displayhook
import pandas as pd
import pyautogui
import time
import pyperclip
#Passo 01
#abrir a aba no navegador 

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.press('chrome')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 't')
link = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga"
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(5)

#Passo 02
#entrar no link sistema
time.sleep(3)
pyautogui.click( 119, 270 ,clicks=2)



#Passo 3

pyautogui.click(386, 476) #clicar no arquivo
pyautogui.click(93, 264) #fazer download

time.sleep(10)


#calcular a planilha
import pandas as pd
tabela = pd.read_excel("C:\Users\Vini\Downloads\Vendas - Dez.xlsx")
faturamento = tabela ['Valor final'].sum()#soma da coluna valor final 
quantidade =tabela['Quantidade'].sum() #Soma da coluna Quantidade
displayfunction.display(tabela)


#enviar email
pyautogui.hotkey('ctrl','t')
#entrar no gmail
link = 'mail.google.com'
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(15)

#clicar no escrever
pyautogui.click(75, 172)
pyautogui.write('estudosviny@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
#digitar o assunto 
pyautogui.write('Relatorio de vendas')
pyautogui.press('tab')

# digitar corpo do email
texto_email = """
Bom dia kr conseguimos , Nunca desista ...
ps PYTHON É FODA!!!!!
"""
pyautogui.write(texto_email)

#clicar em enviar 
pyautogui.hotkey('ctrl','enter')