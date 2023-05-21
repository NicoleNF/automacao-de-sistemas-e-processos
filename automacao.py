import pyautogui
from selenium import webdriver
import pandas as pd
import pyperclip
import time
from webdriver_manager.chrome import ChromeDriverManager

# Passo 1: Acessar o sistema da empresa
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")
time.sleep(5)

# Passo 2: Fazer login no sistema
pyautogui.click(x=973, y=426)
pyautogui.write("meu_login")
pyautogui.click(x=935, y=521)
pyautogui.write("minha_senha")
pyautogui.click(x=971, y=601)
time.sleep(3)

# Passo 3: Baixar base de dados
pyautogui.click(x=510, y=330)
pyautogui.click(x=1661, y=198)
pyautogui.click(x=1485, y=623)
time.sleep(3)

# Passo 4: Calcular os indicadores
tabela = pd.read_csv(r"C:\Users\joaol\Downloads\Compras.csv", sep=";")
total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantifsfr"].sum()
preco_medio = total_gasto / quantidade

print(total_gasto)
print(quantidade)
print(preco_medio)

# Passo 5: Enviar o e-mail para o chefe
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")
time.sleep(5)

pyautogui.click(x=135, y=240)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

texto = f"""
Prezados,
Segue o relatório de compras

Total Gasto: R${total_gasto:,.2f}
Quantidade de Produtos: {quantidade:,}
Preço Médio: R${preco_medio:,.2f}

Qualquer dúvida, é só falar.
Att., Nicole Ferreira
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("ctrl", "enter")