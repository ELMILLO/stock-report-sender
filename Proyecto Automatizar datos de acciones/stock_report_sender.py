import time 
import webbrowser
import pyautogui
import pyperclip
import yfinance
import matplotlib

stocks = input("Ingrese la accion que desea consultar ")
destinatario = input("Ingresa el email a quien deseas enviarle el reporte de la accion ")

data = yfinance.Ticker(stocks).history("6mo")
close = data.Close
maxima = round(close.max(), 2)
minima = round(close.min(), 2)
media = round(close.mean(), 2)


asunto = f"Reporte de accion {stocks}, de los ultimos 6 meses"
mensaje = f"""
Buenas Tardes 

Aca te envio el analisis de las accion que solicitaste en los ultimos 6 meses de {stocks}

Cotizacion Maxima: {maxima} USD
Cotizacion Minima: {minima} USD
Valor Medio: {media} USD

Cualquier cosa quedo al pendiente

Buen dia :)
"""

webbrowser.open("https://outlook.live.com/mail/0/?msalAuthRedirect=true")
pyautogui.position()
time.sleep(3)
pyautogui.PAUSE = 1
pyautogui.click(x=143, y=221)
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")
pyperclip.copy(asunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")
pyperclip.copy(mensaje)
pyautogui.hotkey("ctrl", "v")
pyautogui.click(x=321, y=281)