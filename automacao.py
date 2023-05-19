# Passo 1: Acessar o sistema da empresa

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> apertar uma combinação de teclas (um atalho)


import pyautogui
import selenium
import pandas as pd
import pyperclip
import time
from webdriver_manager.chrome import ChromeDriverManager

pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")

time.sleep(5)

# Passo 2: Fazer login no sistema

pyautogui.click(x=973, y=426)

pyautogui.write("meu_login")

pyautogui.click(x=935, y=521)
pyautogui.write("minha_senha")

# clicar em acessar
pyautogui.click(x=971, y=601)
time.sleep(3)

# Passo 3: Baixar base de dados
pyautogui.click(x=510, y=330) # clica no arquivo de compras
pyautogui.click(x=1661, y=198) # clica nos 3 pontinhos
pyautogui.click(x=1485, y=623) # faz o download
time.sleep(3)

# Passo 4: Calcular os indicadores

tabela = pd.read_csv(r"C:\Users\joaol\Downloads\Compras.csv", sep=";")
print("tabela")
total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantifsfr"].sum()
preco_medio = total_gasto / quantidade

print(total_gasto)
print(quantidade)
print(preco_medio)

# Passo 5: Enviar o e-mail para o chefe

# entrar no email: https://mail.google.com/mail/u/0/#inbox
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")

time.sleep(5)

# clicar no botão escrever
pyautogui.click(x=135, y=240)

# preencher as informações do email
# destinatário

pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # escolher o destinatario

pyautogui.press("tab") # passar para o campo assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab") # passando para o corpo do email

texto = f"""
Prezados,
Segue o relatório de compras

Total Gasto: R${total_gasto:,.2f}
Quantidade de Produtos: {quantidade:,}
Preço Médio: R${preco_medio:,.2f}

Qualquer dúvida, é só falar.
Att., Lira Python
"""

pyperclip.copy(texto)meu_login
pyautogui.hotkey("ctrl", "v")


# enviar
pyautogui.hotkey("ctrl", "enter")