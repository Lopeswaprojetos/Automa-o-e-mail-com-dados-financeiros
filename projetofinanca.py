import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

# Solicitar o código da ação
ticker = input("Digite o código da ação desejada: ")

# Obter dados da ação
dados = yfinance.Ticker(ticker).history(start="2020-01-01", end="2020-12-31")
fechamento = dados.Close

# Calcular estatísticas
maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

# Dados do e-mail
destinatario = 'email exemplo'
assunto = 'Análises Projeto 2020'
mensagem = f""" 
Prezado gestor, bom dia!

Segue abaixo as análises da ação {ticker}:
Cotação máxima : R${maxima}
Cotação mínima : R${minima}
Valor médio : R${valor_medio}

Qualquer dúvida, estou à disposição!

Atenciosamente,
Wagner Silva
"""

# Abrir o navegador e acessar o Gmail
webbrowser.open("https://mail.google.com/")
time.sleep(10)  # Tempo de espera para garantir que o Gmail carregue

# Configurar uma pausa de 3 segundos entre ações
pyautogui.PAUSE = 3

# Clicar no botão para escrever um novo e-mail
pyautogui.click(x=2019, y=229)  # Verifique as coordenadas

# Digitar o email do destinatário e pressionar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

# Digitar o assunto e pressionar TAB
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

# Digitar a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')  # Pressionar Enter ou clicar para enviar

# Clicar no botão enviar
pyautogui.click(x=3075, y=1036)  # Verifique as coordenadas

# Fechar a aba do Gmail
pyautogui.hotkey("ctrl", "w")  # Fechar a aba

print("Email enviado com sucesso!")


