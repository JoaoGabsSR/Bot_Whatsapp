import pywhatkit as pw
import keyboard
import time
from datetime import datetime

# !REGRA DE FORMATO DE CONTATOS: +(COD. PAÍS)(COD. ÁREA)(NÚMERO) #
contatos = ['']

while len(contatos) >= 1:
    # ENVIAR MENSAGEM #
    pw.sendwhatmsg(contatos[0], 'Vamos automatizar tudo!', datetime.now().hour,
                   datetime.now().minute + 1)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')
