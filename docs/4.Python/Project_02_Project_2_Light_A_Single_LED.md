### Proyecto 2：Encender un solo LED

![](./media/Python_b855274f.png)

1\.  **Descripción**

La matriz de puntos LED consta de 25 diodos dispuestos en un cuadrado de 5 por 5 y colocados en la intersección de las líneas de fila (X) y las líneas de columna (Y). Podemos controlar uno de los 25 LEDs estableciendo puntos de coordenadas. Por ejemplo, el primer LED en la primera fila está en (0,0) y el tercer LED posicionado en la primera fila está en (2,0) y así sucesivamente.

![](./media/Python_094d5908.png)

2\.  **Preparación**

A. Conecte la placa principal micro:bit a su ordenador mediante el cable USB

B. Abra la versión offline de Mu.

3\.  **Código de prueba**

Abra el software Mu y abra el archivo “Single LED display\.py.” para importar el código. También puede introducir el código en la ventana de edición usted mismo.

(**Nota: Todas las palabras y símbolos en inglés deben escribirse en inglés**)

![](./media/Python_9545233e.png)

```python
from microbit import *

val1 = Image("09000:""00000:""00000:""00000:""00000:")
val2 = Image("00000:""00000:""00000:""00000:""00090:")
val3 = Image("00000:""00000:""00000:""00000:""00000:")

while True:
    display.show(val1)
    sleep(500)
    display.show(val3)
    sleep(500)
    display.show(val2)
    sleep(500)
    display.show(val3)
    sleep(500)

```

Haga clic en “Check” para examinar errores en el código. El programa se considera erróneo si aparecen subrayados y cursores.

![](./media/Python_d205be08.png)

Si el código es correcto, conecte el micro:bit a su ordenador y haga clic en “Flash” para descargar el código a la placa micro:bit.

![](./media/Python_86dd6eea.png)

4\.  **Resultado de la prueba**

Después de descargar el código en la placa correctamente, **alimente mediante el cable micro USB o una fuente de alimentación externa (mueva el interruptor DIP a ON)** y presione el botón de reinicio en la placa.

![Img](./media/Python_bb3e1312.png)

El LED en (1,0) se encenderá y apagará durante 0,5 s y el de (3,4) se encenderá y apagará durante 0,5 s, repitiendo esta secuencia.

5\.  **Explicación del código**

![Img](./media/Python_c79b7922.png)

6\.  **Referencia**

sleep(ms) : tiempo de retardo

Para más detalles sobre la demora, consulte el enlace: [https://microbit-micropython.readthedocs.io/en/latest/utime.html](https://microbit-micropython.readthedocs.io/en/latest/utime.html)