# robo_waiter
Practica RLP 

### 1-RoboWaiter

Robot camarero que recorre las mesas esperando pedidos, le pides lo que quieres a través de un micrófono, va a la cocina a buscar el pedido y lo entrega.

### 2-Install
Las dependencias necesarias a instalar en una raspberry pi.
* Pip
    * PyAudio
    * google-cloud
    * google-oauth2-tool

* HX711: Seguir las instrucciones de instalacion del [repositorio](https://github.com/endail/hx711-rpi-py?tab=readme-ov-file#install)

### 3-Libraries

* gpiozero

* time 

* io

* google.cloud

* google.oauth2

* hx711

* pyaudio

* wave

* signal

* threading

* queue


#### M1-Hardware

![Diagrama de conexiones](https://github.com/45Hack45/robo_waiter/blob/23fafc6506aca0948aa448da716c69b8cfb494a7/conexiones_proyecto.jpg)

#### M2-3D

![Modelo 3D](https://github.com/45Hack45/robo_waiter/blob/main/Robowaiter_3D.png)

#### M3-Mòdul Controlador

El mòdul controlador sencarrega de fer els dos modes que té el nostre robot.

* Mode demanar: En aquest mode el robot surt de la cuïna (lloc d'inici) i recorre totes les taules esperant-se una mica en cada per agafar les comandes.

* Mode repartir: En aquest mode el robot va al lloc d'inici a esperar el pes de la comanda i una vegada el detecta torna a la taula que s'ha fet la comanda i s'espera fins que hi hagi pes.

#### M4-Mòdul Escolta

Aquest mòdul s'encarrega de grabar les comandes de les persones per audio. Pasa el audio a una funció de speech-to-text on es treuran les paraules claus que hem possat (diferents menjars).
  
### 5-To do's

* Utilitzar encoders per a millorar la precisió dels moviments del robot

* Donar-li un pes als diferents aliments i fer que comprobés el pes mes o menys exacte per moure's

* Fer que el robot pogués anar a més taules

* Fer el diseny del robot més atractiu per a un restaurant

### 6-Refs

* [Libreria sensor de peso hx711](https://github.com/endail/hx711-rpi-py)
* [Snipets gpiozero](https://gpiozero.readthedocs.io/en/latest/recipes.html)
