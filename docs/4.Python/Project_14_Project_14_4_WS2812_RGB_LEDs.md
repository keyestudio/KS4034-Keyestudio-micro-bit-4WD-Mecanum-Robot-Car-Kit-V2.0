### Proyecto 14: 4 LEDs RGB WS2812

![](./media/Python_eecf79fe.png)

1\.  **Descripción**

El shield controlador trabaja con 4 piezas de LED RGB WS2812, es compatible con la placa micro:bit y se controla por P7. En esta lección haremos que los LED RGB muestren diferentes colores mediante P7. En esta lección se proporcionan 3 conjuntos de código de prueba para que los 4 LED WS2812 RGB muestren diferentes efectos.

![Img](./media/Python_0be70eda.png)

2\.  **Preparación**

- Inserte la placa micro:bit en la ranura del keyestudio 4WD Mecanum Robot Car V2.0

- Coloque las baterías en el portapilas

- Gire el interruptor de alimentación a la posición ON

- Conecte el micro:bit a su ordenador mediante un cable USB

- Abra la versión offline de Mu.

3\.  **Test Code1**

Abra el software Mu y abra el archivo“4 WS2812 RGB LEDs-1\.py”para importar el código\ También puede introducir el código usted mismo en la ventana de edición.

(**Nota: Todas las palabras y símbolos en inglés deben escribirse en inglés.**)

Haga clic en“Check”para comprobar errores en el código. El programa es incorrecto si se muestran subrayados y cursores. 

![](./media/Python_5b5266e2.png)

```python
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin7, 4)
while True:
    for pixel_id1 in range(0, len(np)):
        np[pixel_id1] = (255, 0, 0)
        np.show()
    sleep(1000)
    for pixel_id2 in range(0, len(np)):
        np[pixel_id2] = (255, 165, 0)
        np.show()
    sleep(1000)
    for pixel_id3 in range(0, len(np)):
        np[pixel_id3] = (255, 255, 0)
        np.show()
    sleep(1000)
    for pixel_id4 in range(0, len(np)):
        np[pixel_id4] = (0, 255, 0)
        np.show()
    sleep(1000)
    for pixel_id5 in range(0, len(np)):
        np[pixel_id5] = (0, 0, 255)
        np.show()
    sleep(1000)
    for pixel_id6 in range(0, len(np)):
        np[pixel_id6] = (75, 0, 130)
        np.show()
    sleep(1000)
    for pixel_id7 in range(0, len(np)):
        np[pixel_id7] = (238, 130, 238)
        np.show()
    sleep(1000)
    for pixel_id8 in range(0, len(np)):
        np[pixel_id8] = (160, 32, 240)
        np.show()
    sleep(1000)
    for pixel_id9 in range(0, len(np)):
        np[pixel_id9] = (255, 255, 255)
    sleep(1000)
```

Si el código es correcto, conecte el micro:bit a su ordenador y haga clic en“Flash”para descargar el código en la placa micro:bit.

![](./media/Python_56a9ab63.png)

4\.  **Resultado de la Prueba1**

Después de descargar el código en la placa con éxito, **alimentación externa (gire el interruptor DIP a ON)**, y presione el botón de reinicio en el micro:bit.

![Img](./media/Python_bb3e1312.png)

Los 4 LED WS2812RGB se encienden cíclicamente, cada vez con un color diferente.

5\.  **Test Code2**

Abra el software Mu y abra el archivo“4 WS2812 RGB LEDs-2\.py”para importar el código. También puede introducir el código usted mismo en la ventana de edición.

(**Nota: Todas las palabras y símbolos en inglés deben escribirse en inglés**.)

Haga clic en“Check”para comprobar errores en el código. El programa es incorrecto si se muestran subrayados y cursores. 

Si el código es correcto, conecte el micro:bit a su ordenador y haga clic en“Flash”para descargar el código en la placa micro:bit.

![](./media/Python_8cb1dd7c.png)

```python
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin7, 4)
while True:
    for index in range(0, 4):
        np.clear()
        np[index] = (255, 0, 0)
        np.show()
        sleep(100)
    for index1 in range(0, 4):
        np.clear()
        np[index1] = (255, 165, 0)
        np.show()
        sleep(100)
    for index2 in range(0, 4):
        np.clear()
        np[index2] = (255, 255, 0)
        np.show()
        sleep(100)
    for index3 in range(0, 4):
        np.clear()
        np[index3] = (0, 255, 0)
        np.show()
        sleep(100)
    for index4 in range(0, 4):
        np.clear()
        np[index4] = (0, 0, 255)
        np.show()
        sleep(100)
    for index5 in range(0, 4):
        np.clear()
        np[index5] = (75, 0, 130)
        np.show()
        sleep(100)
    for index6 in range(0, 4):
        np.clear()
        np[index6] = (238, 130, 238)
        np.show()
        sleep(100)
    for index7 in range(0, 4):
        np.clear()
        np[index7] = (160, 32, 240)
        np.show()
        sleep(100)
    for index8 in range(0, 4):
        np.clear()
        np[index8] = (255, 255, 255)
        np.show()
        sleep(100)
```

6\.  **Resultado de la Prueba2**

Después de descargar el código en la placa con éxito, **alimentación externa (gire el interruptor DIP a ON)**, y presione el botón de reinicio en el micro:bit.

![Img](./media/Python_bb3e1312.png)

Los LED WS2812RGB muestran un efecto de luz en movimiento (flow light).

7\.  **Test Code3**

Abra el software Mu y abra el archivo“4 WS2812 RGB LEDs-3\.py”para importar el código. También puede introducir el código usted mismo en la ventana de edición.

(**Nota: Todas las palabras y símbolos en inglés deben escribirse en inglés.**)

Haga clic en“Check”para comprobar errores en el código. El programa es incorrecto si se muestran subrayados y cursores. 

Si el código es correcto, conecte el micro:bit a su ordenador y haga clic en“Flash”para descargar el código en la placa micro:bit.

![](./media/Python_b248f1c5.png)

```python
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin7, 4)
from random import randint
R = 0
G = 0
B = 0
while True:
   for index in range(0, 4):
        R = randint(10, 255)
        G = randint(10, 255)
        B = randint(10, 255)
        np.clear()
        np[index] = (R, G, B)
        np.show()
        sleep(500)
```

8\.  **Resultado de la Prueba3**

Después de descargar el código en la placa con éxito, **alimentación externa (gire el interruptor DIP a ON)**, y presione el botón de reinicio en el micro:bit.

![Img](./media/Python_bb3e1312.png)

Cada LED WS2812RGB muestra un color aleatorio, uno por uno.

5\.  **Explicación del Código**

![Img](./media/Python_d1e3977b.png)

---