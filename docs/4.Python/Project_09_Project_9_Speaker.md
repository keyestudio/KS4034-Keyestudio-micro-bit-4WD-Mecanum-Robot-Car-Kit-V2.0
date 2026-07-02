### Proyecto 9: Altavoz

![](./media/Python_ac515b9a.png)

1\.  **Descripción**

La placa principal micro:bit tiene un altavoz incorporado, lo que facilita agregar sonido a los programas. También puede programarse para producir todo tipo de tonos, como interpretar la canción *Ode to Joy*.

2\.  **Preparación**

A. Conecte la placa principal micro:bit a su ordenador mediante el cable USB

B. Abra la versión offline de Mu.

3\.  **Código de prueba**

Abra el software Mu y abra el archivo “Speaker\.py” para importar el código. También puede introducir el código usted mismo en la ventana de edición.

(**Nota: Todas las palabras y símbolos deben escribirse en inglés**.)

![](./media/Python_eec7f643.png)

```python
from microbit import *

import audio

display.show(Image.MUSIC_QUAVER)

while True:
    audio.play(Sound.GIGGLE)
    sleep(1000)
    audio.play(Sound.HAPPY)
    sleep(1000)
    audio.play(Sound.HELLO)
    sleep(1000)
    audio.play(Sound.YAWN)
    sleep(1000)
```

Haga clic en “Check” para comprobar errores en el código. El programa es incorrecto si aparecen subrayados y cursores.

![](./media/Python_f8852abf.png)

Si el código es correcto, conecte el micro:bit a su ordenador y haga clic en “Flash” para descargar el código en la placa micro:bit.

![](./media/Python_3fd94e43.png)

4\.  **Resultado de la prueba**

Después de descargar el código en la placa con éxito, **alimente mediante el cable micro USB o una fuente de alimentación externa (ponga el interruptor DIP en ON)** y presione el botón de reinicio en el micro:bit.

![Img](./media/Python_bb3e1312.png)

 El altavoz emite sonido y la matriz de puntos LED muestra el símbolo de música.

5\.  **Explicación del código**

![Img](./media/Python_18c047bd.png)

---