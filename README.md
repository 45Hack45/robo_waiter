# robo_waiter
Practica RLP 

### 1-RoboWaiter

Robot camarero que recorre las mesas esperando pedidos, le pides lo que quieres a través de un micrófono, va a la cocina a buscar el pedido y lo entrega.

### 2-Install

* Pip
    * pip install PyAudio
    * pip install google-cloud
    * pip install google-oauth2-tool

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

  
### 5-To do's

* Donar-li un pes als diferents aliments i fer que comprobés el pes mes o menys exacte per moure's

* Fer que el robot pogués anar a més taules

* Fer el diseny del robot més atractiu per a un restaurant

### 6-Refs

* [Libreria sensor de peso hx711](https://github.com/endail/hx711-rpi-py)
* [Snipets gpiozero](https://gpiozero.readthedocs.io/en/latest/recipes.html)
