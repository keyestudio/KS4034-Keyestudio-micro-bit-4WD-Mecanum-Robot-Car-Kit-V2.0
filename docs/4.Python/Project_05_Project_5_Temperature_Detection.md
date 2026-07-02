### Proyecto 5：Detección de temperatura

1\.  **Descripción**

La placa principal Micro:bit no está equipada con un sensor de temperatura, sino que utiliza el sensor de temperatura integrado en el chip NFR52833 para la detección de temperatura. Por lo tanto, la temperatura detectada está más próxima a la temperatura del chip y puede diferir de la temperatura ambiente.

En este proyecto, utilizaremos el sensor para medir la temperatura en el entorno actual y mostrar los resultados de la medición en el dispositivo de visualización. A continuación, controlaremos la matriz de LED para mostrar diferentes patrones estableciendo el rango de temperatura detectado por el sensor.

**Nota: el sensor de temperatura de la placa principal Micro:bit se muestra a continuación:**

![](./media/Python_206c8ec1.png)

2\.  **Preparación**

A. Conecte la placa principal micro:bit a su ordenador mediante el cable USB

B. Abra la versión offline de Mu.

3\.  **Código de prueba1**

Abra el software Mu e importe el archivo “Temperature Measurement -1\.py “. También puede introducir el código usted mismo en la ventana de edición.

(**Nota: Todas las palabras y símbolos deben escribirse en inglés.**)

![](./media/Python_03cbb6e9.png)

```python
from microbit import *

while True:

    Temperature = temperature()

    print("Temperature:", Temperature, "C")

    sleep(500)
```

Haga clic en “Check” para comprobar si hay errores en el código. El programa es incorrecto si aparecen subrayados y cursores. 

![](./media/Python_7b437c2d.png)

Si el código es correcto, conecte el micro:bit al ordenador y haga clic en “Flash” para descargar el código en la placa micro:bit.

![](./media/Python_193065ab.png)

4\.  **Resultado de la prueba1**

Después de descargar el código a la placa correctamente, **alimente mediante el cable micro USB o una fuente de alimentación externa (ponga el interruptor DIP en ON)**. Haga clic en “REPL” y pulse el botón de reinicio en el micro:bit.

![Img](./media/Python_bb3e1312.png)

A continuación, la ventana REPL mostrará el valor de la temperatura ambiente, como se muestra a continuación: (C representa la unidad de temperatura)

![](./media/Python_d08386d8.png)

5\.  **Código de prueba2**

Abra el software Mu e importe el archivo “Temperature Measurement -2\.py “. También puede introducir el código usted mismo en la ventana de edición.

(**Nota: Todas las palabras y símbolos deben escribirse en inglés.**)

El valor de la temperatura se puede ajustar de acuerdo con la temperatura real.

![](./media/Python_c6456d78.png)

```python
from microbit import *

while True:

    if temperature() >= 35:
        display.show(Image.HEART)

    else:
        display.show(Image.HEART_SMALL)
```

Haga clic en “Check” para comprobar si hay errores en el código. El programa es incorrecto si aparecen subrayados y cursores. 

![](./media/Python_709d3031.png)

Si el código es correcto, conecte el micro:bit al ordenador y haga clic en “Flash” para descargar el código en la placa micro:bit.

![](./media/Python_06f7542e.png)

6\.  **Resultado de la prueba2**

Después de descargar el código a la placa correctamente, **alimente mediante el cable micro USB o una fuente de alimentación externa (ponga el interruptor DIP en ON)** y pulse el botón de reinicio en el micro:bit.

![Img](./media/Python_bb3e1312.png)

 Cuando la temperatura ambiente es inferior a 35℃, la matriz de LED 5×5 muestra ![](./media/Python_034dc0d5.png). Cuando la temperatura es igual o superior a 35℃, aparece el patrón ![](./media/Python_ebfaeac9.png).

7\.  **Explicación del código**

![Img](./media/Python_d7cdc397.png)

---