import requests
import time
import random

WEBHOOK = https://hook.us2.make.com/fwbqvf59fxyv1xsyfptn3ol7nd8ndxfy

while True:
    temperatura = random.randint(30, 50)
    data = {
        "nombre": "Sensor_Industrial",
        "mensaje": f"Temperatura_{temperatura}C"
    }
    requests.post(WEBHOOK, data=data)
    print("Dato enviado:", data)
    time.sleep(10)
