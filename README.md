#  Bot de Envío de Reporte Financiero por Correo

Este script automatiza la generación y el envío de un reporte financiero por correo electrónico, con estadísticas básicas sobre el comportamiento de una acción en los últimos 6 meses, utilizando datos de Yahoo Finance.

##  ¿Qué hace?

1. Solicita al usuario:
   - El ticker de la acción (por ejemplo, `AAPL`, `TSLA`, `MSFT`).
   - El correo electrónico del destinatario.

2. Descarga los datos de los últimos 6 meses usando `yfinance`.

3. Calcula:
   - Precio máximo
   - Precio mínimo
   - Promedio de cierre

4. Redacta un mensaje con esta información.

5. Abre Outlook en el navegador y, mediante automatización con `pyautogui` y `pyperclip`, completa los campos del correo y lo envía automáticamente.

##  Requisitos

Instala los siguientes paquetes antes de ejecutar el script:

```bash
pip install yfinance matplotlib pyautogui pyperclip
