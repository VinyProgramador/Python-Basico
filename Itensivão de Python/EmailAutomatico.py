import displayfunction
from sys import displayhook
import pandas as pd
import pyautogui
import time
import pyperclip

#abrir a aba no navegador 

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.press('chrome')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 't')
link = "mail.google.com"
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(15)
#clicar no escrever
pyautogui.click(75, 172)
pyautogui.write('heldergavioes@hotmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
#digitar o assunto 
pyautogui.write('email automatico do viny')
pyautogui.press('tab')

# digitar corpo do email
texto_email = """
dboa helder?
"""
pyautogui.write(texto_email)

#clicar em enviar 
pyautogui.hotkey('ctrl','enter')