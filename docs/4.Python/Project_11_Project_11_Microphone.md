### Proyecto 11: Micrófono

![](./media/Python_3073a8af.png)

![](./media/Python_7f074115.png)

1\.  **Descripción**

La placa principal Micro: Bit tiene un micrófono incorporado, que puede medir el volumen del entorno. Cuando aplaudes, se enciende el indicador LED del micrófono. Además, puede medir la intensidad del sonido, de modo que puedes crear una escala de ruido o luces tipo disco que cambian con la música.

El micrófono está ubicado en el lado opuesto al indicador LED del micrófono y cerca de agujeros que permiten el paso del sonido. Cuando la placa detecta el sonido, se enciende el indicador LED.

2\.  **Preparación**

A. Conecta la placa principal micro:bit a tu ordenador mediante el cable USB

B. Abre la versión sin conexión de Mu.

3\.  **Código de prueba1**

Abre el software Mu y abre el archivo “Microphone-1\.py” para importar el código. También puedes introducir el código tú mismo en la ventana de edición.

(**Nota: Todas las palabras y símbolos deben estar escritos en inglés**.)

![](./media/Python_19b38832.png)

```python
from microbit import *

while True:
    if microphone.current_event() == SoundEvent.LOUD:
        display.show(Image.HEART)
        sleep(200)
    if microphone.current_event() == SoundEvent.QUIET:
        display.show(Image.HEART_SMALL)
```

Haz clic en “Check” para examinar errores en el código. El programa está mal si se muestran subrayados y cursores. 

![](./media/Python_36a669c7.png)

Si el código es correcto, conecta el micro:bit a tu ordenador y haz clic en “Flash” para descargar el código a la placa micro:bit.

![](./media/Python_0515bf32.png)

4\.  **Resultado de la prueba1**

Tras descargar el código en la placa con éxito, **enciende mediante el cable micro USB o una fuente de alimentación externa (coloca el interruptor DIP en ON)** y pulsa el botón de reinicio del micro:bit.

![Img](./media/Python_bb3e1312.png)

La matriz de puntos LED muestra el patrón “❤” cuando aplaudes y el patrón ![](./media/04fdfc9060943954e7938bb1a741d626.png) cuando está en silencio alrededor.

5\.  **Código de prueba2**

Abre el software Mu y abre el archivo “Microphone-2\.py” para importar el código. También puedes introducir el código tú mismo en la ventana de edición.

(**Nota: Todas las palabras y símbolos deben estar escritos en inglés.**)

![](./media/Python_f0e5a346.png)

```python
from microbit import *
maxSound = 0
lights = Image("11111:"
              "11111:"
              "11111:"
              "11111:"
              "11111")
# ignore first sound level reading
soundLevel = microphone.sound_level()
sleep(200)

while True:
    if button_a.is_pressed():
        display.scroll(maxSound)
    else:
        soundLevel = microphone.sound_level()
        display.show(lights * soundLevel)
        if soundLevel > maxSound:
            maxSound = soundLevel
```

Haz clic en “Check” para examinar errores en el código. El programa está mal si se muestran subrayados y cursores. 

![](./media/Python_d0c79871.png)

Si el código es correcto, conecta el micro:bit a tu ordenador y haz clic en “Flash” para descargar el código a la placa micro:bit.

![](./media/Python_d828b9ee.png)

6\.  **Resultado de la prueba2**

Tras descargar el código en la placa con éxito, **enciende mediante el cable micro USB o una fuente de alimentación externa (coloca el interruptor DIP en ON)** y pulsa el botón de reinicio del micro:bit.

![Img](./media/Python_bb3e1312.png)

 Cuando se pulsa el botón A, la matriz de puntos LED muestra el valor del volumen máximo ( **ten en cuenta que el volumen máximo puede restablecerse mediante el botón Reset en el otro lado de la placa** ). Al aplaudir, cuanto más fuerte sea el sonido medido, más brillantes se muestran los 25 LED de la pantalla de matriz LED.

7\.  **Explicación del código**

![Img](./media/Python_980f62b3.png)