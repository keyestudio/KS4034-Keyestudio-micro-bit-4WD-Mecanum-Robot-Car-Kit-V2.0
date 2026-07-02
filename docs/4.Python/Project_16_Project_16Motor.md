### Proyecto 16: Motor

![](./media/Python_32655f47.png)

1\.  **Descripción**

El coche robot Keyestudio 4WD Mecanum está equipado con 4 motores de CC con reducción, también llamados motores con caja de engranajes, que se desarrollaron a partir del motor de CC ordinario. Dispone de una caja reductora de engranajes a juego que proporciona una velocidad menor pero un par mayor. Además, distintas relaciones de reducción de la caja pueden ofrecer diferentes velocidades y pares.

El motor con engranajes es la integración de la caja de engranajes y el motor, y se aplica ampliamente en la industria siderúrgica y mecánica.

El shield controlador de motor para micro:bit viene con los chips STC8G y HR8833. Para ahorrar recursos de puertos I/O, controlamos la dirección de giro y la velocidad de los 4 motores de CC con el chip HR8833.

**Detalles sobre los chips:**

![](./media/Python_d7132b53.jpg)

Frontal

![](./media/Python_4919ce3b.png)

Trasera

![](./media/Python_fbfa17f7.png)

Circuito del chip STC8G1K08

![](./media/Python_47cdde6b.png)

Circuito del controlador de motor HR8833

2\. **Preparación**

- Inserte la placa micro:bit en la ranura del Keyestudio 4WD Mecanum Robot Car V2.0

- Inserte las baterías en el portapilas

- Ajuste el interruptor de alimentación en la posición ON

- Conecte la micro:bit al ordenador mediante un cable USB

- Abra la versión offline de Mu.

3\. **Código de prueba 1**

Abra el software Mu y abra el archivo “microbit-Motor Driving-1.py” para importar el código. También puede introducir el código usted mismo en la ventana de edición.

(**Nota: Todas las palabras y símbolos en inglés deben permanecer en inglés**.)

Haga clic en “Files” para importar el archivo de librería “keyes_mecanum_Car.py” a la micro:bit. 

Haga clic en “Check” para comprobar errores en el código. El programa está incorrecto si aparecen subrayados y cursores. 

Si el código es correcto, conecte la micro:bit al ordenador y haga clic en “Flash” para descargar el código a la placa micro:bit.

![](./media/Python_71476377.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()
while True:
    display.show(Image.ARROW_S)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    display.show(Image.ARROW_N)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(0, 100)
    mecanumCar.Motor_Lower_R(0, 100)
    sleep(1000)
    display.show(Image.ARROW_E)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    display.show(Image.ARROW_W)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(0, 100)
    mecanumCar.Motor_Lower_R(0, 100)
    sleep(1000)
    display.show(Image("00900:""09990:""99999:""99999:""09090"))
    mecanumCar.Motor_Upper_L(0, 0)
    mecanumCar.Motor_Lower_L(0, 0)
    mecanumCar.Motor_Upper_R(0, 0)
    mecanumCar.Motor_Lower_R(0, 0)
    sleep(1000)
```

4\. **Resultado de la prueba 1**

Después de descargar el código a la placa con éxito, **alimente con la fuente externa (gire el interruptor DIP a ON)** y pulse el botón de reset en la micro:bit.

![Img](./media/Python_bb3e1312.png)

A continuación, el coche avanzará durante 1 s, retrocederá durante 1 s, girará a la izquierda durante 1 s, a la derecha durante 1 s, girará en sentido antihorario durante 1 s, en sentido horario durante 1 s y se detendrá 1 s. La matriz LED también muestra los patrones.

5\. **Código de prueba 2**

Abra el software Mu y abra el archivo “microbit-Motor Driving-2.py” para importar el código. También puede introducir el código usted mismo en la ventana de edición.

(**Nota: Todas las palabras y símbolos en inglés deben permanecer en inglés**.)

Haga clic en “Files” para importar el archivo de librería “keyes_mecanum_Car.py” a la micro:bit. 

Haga clic en “Check” para comprobar errores en el código. El programa está incorrecto si aparecen subrayados y cursores. 

Si el código es correcto, conecte la micro:bit al ordenador y haga clic en “Flash” para descargar el código a la placa micro:bit.

![](./media/Python_96230faf.png)

```python
from microbit import button_a, button_b, display, Image, sleep
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()

show_L = Image("90000:""90000:""90000:""90000:""99999")
show_O = Image("09990:""90009:""90009:""90009:""09990")
a = 0
b = 0
def run_L():
    global b
    sleep(1000)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(650)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 0)
    mecanumCar.Motor_Lower_L(0, 0)
    mecanumCar.Motor_Upper_R(0, 0)
    mecanumCar.Motor_Lower_R(0, 0)
    b = 0
def run_O():
    global b
    sleep(1000)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(620)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(620)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(620)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 0)
    mecanumCar.Motor_Lower_L(0, 0)
    mecanumCar.Motor_Upper_R(0, 0)
    mecanumCar.Motor_Lower_R(0, 0)
    b = 0
while True:
    if button_a.was_pressed():
        a = a + 1
        if a >= 3:
            a = 0
    if button_b.was_pressed():
        b = 1
    if (a == 1):
        display.show(show_L)
        if b == 1:
            run_L()
    elif a == 2:
        display.show(show_O)
        if b == 1:
            run_O()
```

6\. **Resultado de la prueba 2**

Después de descargar el código a la placa con éxito, **alimente con la fuente externa (gire el interruptor DIP a ON)** y pulse el botón de reset en la micro:bit.

![Img](./media/Python_bb3e1312.png)

Cuando se presionan por primera vez los botones A y B, la micro:bit mostrará “L”; la trayectoria del coche es en forma de “L”. Cuando se presionan de nuevo, la micro:bit muestra “口” y la trayectoria del coche es “口”. El coche repetirá este patrón.

7\.  **Explicación del código**

![Img](./media/Python_70b4e70f.png)

![Img](./media/Python_e3250a8a.png)

---