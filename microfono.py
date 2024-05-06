from gpiozero import MCP3008, Button
import time

# Configuración del ADC (MCP3008)
adc = MCP3008(channel=0)  # Canal 0 para el micrófono (ajusta según tus necesidades)
boton = Button(17)  # Cambia al pin que desees usar para el botón

def leer_valor_adc():
    valor_adc = adc.value
    voltaje = valor_adc * 5.0
    return voltaje

try:
    while True:
        boton.wait_for_press()
        leer_valor_adc()
except KeyboardInterrupt:
    print("\nLectura detenida por el usuario.")