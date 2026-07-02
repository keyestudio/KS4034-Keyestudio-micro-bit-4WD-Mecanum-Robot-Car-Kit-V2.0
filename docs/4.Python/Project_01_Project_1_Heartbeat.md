### Project 1：Heart Beat

![](./media/Python_b855274f.png)

1\.  **Descripción**

Este proyecto es fácil de realizar únicamente con una placa micro:bit y un cable micro USB. Este experimento sirve como introducción para que entres en el mágico mundo de la programación del micro:bit.

2\.  **Preparación**

A. Conecta la placa micro:bit a tu ordenador mediante el cable USB.

B. Abre la versión offline de Mu.

3\.  **Código de prueba**

Abre el software Mu, pulsa “Load”, selecciona el archivo ““microbit-Heartbeat\.py“” y haz clic en “open”:

![](./media/Python_1ec17d44.png)

![](./media/Python_4bda2b61.png)

Hay otra forma de importar código. Abre Mu y arrastra el archivo “microbit-Heartbeat\.py” dentro.

![](./media/Python_c5b7322b.png)

También puedes introducir el código directamente en la ventana de edición.

(**Nota: Todas las palabras y símbolos en inglés deben escribirse en inglés.**)

![](./media/Python_80af4cb3.png)

```python
from microbit import *

while True:
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART_SMALL)
    sleep(500)
```
A continuación se muestra una lista de imágenes integradas:

• Image.HEART

• Image.HEART_SMALL

• Image.HAPPY

• Image.SMILE

• Image.SAD

• Image.CONFUSED

• Image.ANGRY

• Image.ASLEEP

• Image.SURPRISED

• Image.SILLY

• Image.FABULOUS

• Image.MEH

• Image.YES

• Image.NO

• Image.CLOCK12, Image.CLOCK11, Image.CLOCK10, Image.CLOCK9, Image.CLOCK8, Image.CLOCK7, Image.CLOCK6, Image.CLOCK5,

Image.CLOCK4, Image.CLOCK3, Image.CLOCK2, Image.CLOCK1

• Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE, Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW

• Image.TRIANGLE

• Image.TRIANGLE_LEFT

• Image.CHESSBOARD

• Image.DIAMOND

• Image.DIAMOND_SMALL

• Image.SQUARE

• Image.SQUARE_SMALL

• Image.RABBIT

• Image.COW

• Image.MUSIC_CROTCHET

• Image.MUSIC_QUAVER

• Image.MUSIC_QUAVERS

• Image.PITCHFORK

• Image.PACMAN

• Image.TARGET

• Image.TSHIRT

• Image.ROLLERSKATE

• Image.DUCK

• Image.HOUSE

• Image.TORTOISE

• Image.BUTTERFLY

• Image.STICKFIGURE

• Image.GHOST

• Image.SWORD

• Image.GIRAFFE

• Image.SKULL

• Image.UMBRELLA

• Image.SNAKE，Image.ALL_CLOCKS，Image.ALL_ARROWS

Conecta la placa micro:bit al ordenador mediante un cable USB y haz clic en “Flash” para descargar el código en la placa.

![](./media/Python_93e18731.png)


![](./media/Python_48e78948.png)


![](./media/Python_cc33f1a9.png)

El código, aunque esté mal, puede descargarse correctamente en la placa micro:bit, pero no funcionará en el micro:bit.

Haz clic en “Flash” para descargar el código al micro:bit.

![](./media/Python_8982d0b0.png)

Haz clic en “REPL” y pulsa el botón de reinicio en el micro:bit; la información de error se mostrará en la ventana REPL, como se muestra a continuación:

![](./media/Python_0c2abf18.png)

Haz clic de nuevo en “REPL” para desactivar el modo REPL, entonces podrás actualizar el código nuevo.

Para asegurarte de que el código es correcto, solo necesitas tocar “Check”. Los errores se mostrarán en la ventana.

![](./media/Python_b994c0d3.png)

Modifica el código de acuerdo con las indicaciones y haz clic en “Check”.

![](./media/Python_bc5cbed3.png)

 Por favor, visita el sitio web para más tutoriales: [https://codewith.mu/en/tutorials/](https://codewith.mu/en/tutorials/)

4\.  **Resultado de la prueba**

Haz clic en “<span style="color: rgb(255, 76, 65);">**Flash**</span>” para cargar el código en la placa micro:bit.

![Img](./media/Python_ed83ac25.png)

Después de descargar correctamente el código en la placa, **enciende la alimentación mediante el cable micro USB o una fuente de alimentación externa (mueve el interruptor DIP a ON)**, y pulsa el botón de reinicio en la placa.

![Img](./media/Python_bb3e1312.png)

La matriz de puntos LED muestra alternativamente el patrón “❤” y luego “![](./media/Python_04fdfc90.png)”.

5\.  **Explicación del código**

|from microbit import*|Importa el archivo de la librería del micro:bit|
|-|-|
|while True:|Este es un bucle permanente que hace que el micro:bit ejecute el código en este bucle para siempre.|
|display.show(Image.HEART)|micro:bit muestra “❤”|
|sleep(500)|Retardo de 500 ms|
|display.show(Image.HEART_SMALL)|La matriz LED muestra “![](./media/Python_04fdfc90.png)”|

---