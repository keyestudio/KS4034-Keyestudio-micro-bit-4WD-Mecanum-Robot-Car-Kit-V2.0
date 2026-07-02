### Proyecto 17：Line Tracking Sensor

#### Proyecto 17.1：Detect Line Tracking Sensor

![](./media/Python_ea7f6c8c.png)

1\. **Descripción**

La placa controladora de motor del Keyestudio 4WD Mecanum Robot Car incluye un sensor de seguimiento de línea de 3 canales, que utiliza tubos IR TCRT5000 y 3 potenciómetros.

El tubo IR TCRT5000 contiene un emisor IR y un receptor IR. Cuando las señales infrarrojas del emisor son recibidas por el receptor mediante reflexión, la resistencia del receptor cambia, lo cual generalmente se refleja en el cambio de voltaje en el circuito.

La resistencia varía dependiendo de la intensidad de las señales infrarrojas recibidas por el receptor, lo cual suele depender del color de la superficie reflectante y de la distancia entre la superficie reflectante y el receptor. En la detección, el negro es activo en nivel alto y el blanco es activo en nivel bajo.

2\. **Principio de funcionamiento**

Cuando el coche se desplaza sobre una superficie blanca, el tubo emisor IR instalado bajo el coche emite señales infrarrojas para detectar la carretera y el receptor recibirá las señales enviando respuesta. Entonces la salida ofrece nivel bajo (0); cuando detecta líneas negras, emite nivel alto (1).

El puerto integrado del sensor de seguimiento de 3 canales en el 4WD Mecanum Robot Car está conectado al puerto de recolección de G, 5V, P10, P4 y P3 en la placa de expansión micro:bit, y es controlado por P10, P4 y P3 del micro:bit. El par IR TCRT5000 izquierdo en el sensor es controlado por P3, el central por P4 y el derecho por P10.

Colocando un papel blanco bajo el 4WD Mecanum Robot Car, giraremos los potenciómetros en el sensor de 3 vías. Cuando la luz indicadora en el módulo del sensor esté encendida, levante el coche para separar las dos ruedas del 4WD Mecanum Robot Car. La altura del papel blanco debe ser de aproximadamente 1.5 cm; cuando la luz indicadora en el módulo del sensor se apague, se ha ajustado la sensibilidad.

**Tenga en cuenta que como la matriz de puntos 5*5 usa P3 P4 P6 P7 P10, debemos desactivar la función de la matriz de puntos cuando usemos el sensor de seguimiento de línea.**

3\. **Preparación**

- Inserte la placa micro:bit en la ranura del Keyestudio 4WD Mecanum Robot Car V2.0

- Coloque las pilas en el portapilas

- Gire el interruptor de alimentación a la posición ON

- Conecte el micro:bit al ordenador mediante un cable USB

- Abra la versión offline de Mu.

4\. **Código de prueba**

Abra el software Mu y abra el archivo “Line tracking detection\.py” para importar el código. También puede introducir el código en la ventana de edición usted mismo.

(**Nota: Todas las palabras y símbolos en inglés deben estar escritos en inglés**.)

Haga clic en “Check” para comprobar errores en el código. El programa estará mal si aparecen subrayados o cursores.

Si el código es correcto, conecte el micro:bit a su ordenador y haga clic en “Flash” para descargar el código a la placa micro:bit.

![](./media/Python_2c7b1c21.png)

```python
from microbit import *
display.off()

val_L = 0
val_C = 0
val_R = 0
while True:
    val_L = pin3.read_digital()
    val_C = pin4.read_digital()
    val_R = pin10.read_digital()
    print("digital signal:", end = ' ')
    print(val_L, end = ' ')
    print(val_C, end = ' ')
    print(val_R)
    sleep(200)
```

5\. **Resultado de la prueba**

Tras descargar el código en la placa correctamente y sin desconectar el cable USB, haga clic en “REPL” y luego presione el botón de reset.

![Img](./media/Python_bb3e1312.png)

Las lecturas detectadas por el tubo IR TCRT5000 izquierdo se mostrarán en el monitor.

Cuando el tubo IR TCRT5000 izquierdo detecta un objeto blanco, se mostrará 0 y el indicador izquierdo estará encendido; cuando sólo detecta objeto negro, se mostrará 1 y el indicador estará apagado, como se muestra a continuación:

![](./media/Python_6a25b450.png)

6\. **Explicación del código**

![Img](./media/Python_5dad345e.png)


#### Proyecto 17.2：Tracking Smart Car

![](./media/Python_f0b62e0f.jpg)

1\. Descripción

En esta lección combinaremos un sensor de seguimiento de línea con un motor para crear un coche inteligente que siga líneas.

La placa micro:bit analizará las señales y controlará el coche inteligente para mostrar la función de seguimiento de línea.

2\. **Principio de funcionamiento**

El coche inteligente realizará diferentes movimientos según los valores recibidos por el sensor de seguimiento de línea de 3 canales.

![Img](./media/Python_e672c637.png)

3\. **Preparación**

- Inserte la placa micro:bit en la ranura del Keyestudio 4WD Mecanum Robot Car V2.0

- Coloque las pilas en el portapilas

- Gire el interruptor de alimentación a la posición ON

- Conecte el micro:bit al ordenador mediante un cable USB

- Abra la versión offline de Mu.

**Advertencia:** El sensor de 3 vías debe utilizarse en un entorno sin interferencias infrarrojas como la luz solar. La luz solar contiene mucha luz invisible, como infrarrojos y ultravioleta. En un entorno con luz solar intensa, el sensor de 3 vías no funcionará correctamente.

4\. **Diagrama de flujo**

![Img](./media/Python_47856ed2.png)

5\. **Código de prueba**

Abra el software Mu y abra el archivo “Line tracking car\.py” para importar el código. También puede introducir el código en la ventana de edición usted mismo.

(**Nota: Todas las palabras y símbolos en inglés deben estar escritos en inglés**.)

Haga clic en “Files” para importar el archivo de librería “keyes_mecanum_Car.py” al micro:bit.

Haga clic en “Check” para comprobar errores en el código. El programa estará mal si aparecen subrayados o cursores.

Si el código es correcto, conecte el micro:bit a su ordenador y haga clic en “Flash” para descargar el código a la placa micro:bit.

![](./media/Python_bd395cbe.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()
display.off()

val_L = 0
val_C = 0
val_R = 0
while True:
    val_L = pin3.read_digital()
    val_C = pin4.read_digital()
    val_R = pin10.read_digital()
    if val_C == 0:
        if val_L == 0 and val_R == 1:
            mecanumCar.Motor_Upper_L(1, 80)
            mecanumCar.Motor_Lower_L(1, 80)
            mecanumCar.Motor_Upper_R(0, 80)
            mecanumCar.Motor_Lower_R(0, 80)
        elif val_L == 1 and val_R == 0:
            mecanumCar.Motor_Upper_L(0, 80)
            mecanumCar.Motor_Lower_L(0, 80)
            mecanumCar.Motor_Upper_R(1, 80)
            mecanumCar.Motor_Lower_R(1, 80)
        else:
            mecanumCar.Motor_Upper_L(0, 0)
            mecanumCar.Motor_Lower_L(0, 0)
            mecanumCar.Motor_Upper_R(0, 0)
            mecanumCar.Motor_Lower_R(0, 0)
    else :
        if val_L == 0 and val_R == 1:
            mecanumCar.Motor_Upper_L(1, 80)
            mecanumCar.Motor_Lower_L(1, 80)
            mecanumCar.Motor_Upper_R(0, 80)
            mecanumCar.Motor_Lower_R(0, 80)
        elif val_L == 1 and val_R == 0:
            mecanumCar.Motor_Upper_L(0, 80)
            mecanumCar.Motor_Lower_L(0, 80)
            mecanumCar.Motor_Upper_R(1, 80)
            mecanumCar.Motor_Lower_R(1, 80)
        else:
            mecanumCar.Motor_Upper_L(1, 80)
            mecanumCar.Motor_Lower_L(1, 80)
            mecanumCar.Motor_Upper_R(1, 80)
            mecanumCar.Motor_Lower_R(1, 80)
```

6\. **Resultado de la prueba**

Tras descargar el código en la placa correctamente, **alimenta con fuente externa (mueva el interruptor DIP a ON)**, y presione el botón de reset del micro:bit.

![Img](./media/Python_bb3e1312.png)

El coche seguidor de línea avanza siguiendo la línea negra.

**Nota:** (1) El ancho de la línea negra debe ser igual o mayor que el ancho del sensor de seguimiento de línea durante el seguimiento.

(2) Evite probar el coche inteligente bajo luz intensa.

7\. **Explicación del código**

![Img](./media/Python_b16f9d7b.png)

![Img](./media/Python_35f35a4c.png)