### Proyecto 12: Controlar el altavoz

1\.  **Descripción**

En los proyectos anteriores hemos aprendido sobre el logo sensible al tacto y sobre el altavoz, respectivamente. En este proyecto combinaremos estos dos componentes para reproducir música.

2\.  **Componentes necesarios**

|![](./media/Python_021507bd.png)|![](./media/Python_84cdea05.jpg)|
|-|-|
|Micro:bit main board \*1|USB cable\*1|


3\.  **Diagrama de conexiones**

Conecte el Micro:bit main board a su ordenador mediante el cable USB.

![](./media/Python_611b2c4e.png)

4\.  **Código de prueba**

Abra el software Mu y abra el archivo “Touch the Logo to control the speaker\.py” para importar el código. También puede introducir el código en la ventana de edición usted mismo.

(**Nota: Todas las palabras y símbolos deben escribirse en inglés**.)

![](./media/Python_600c8fa6.png)

```python
from microbit import *

import music

display.show(Image.MUSIC_QUAVER)

while True:

    if pin_logo.is_touched():
        music.play(music.BIRTHDAY)
```

Haga clic en “Check” para comprobar los errores en el código. El programa se considera incorrecto si aparecen subrayados y cursores.

![](./media/Python_dcc17127.png)

Si el código es correcto, conecte el micro:bit a su ordenador y haga clic en “Flash” para descargar el código a la placa micro:bit.

![](./media/Python_be3d4ee9.png)

5\.  **Resultado de la prueba**

Después de descargar el código a la placa correctamente, **alimente mediante el cable micro USB o una fuente de alimentación externa (mueva el interruptor DIP a ON)** y pulse el botón de reinicio en el micro:bit.

![Img](./media/Python_bb3e1312.png)

El altavoz reproduce la canción “*Happy Birthday to You*” cuando se toca el logo.

6\.  **Explicación del código**

![Img](./media/Python_852be78f.png)

**Comunicación inalámbrica Bluetooth**

El micro:bit dispone de un módulo Bluetooth de bajo consumo para comunicarse, pero cuenta con 16 KB de RAM. Sin embargo, el heap/stack de BLE ocupa 12 KB de RAM, por lo que no hay suficiente espacio para ejecutar microPython.

En la actualidad, microPython no admite el servicio Bluetooth.

[https://microbit-micropython.readthedocs.io/en/latest/ble.html](https://microbit-micropython.readthedocs.io/en/latest/ble.html)

Los proyectos anteriores son la introducción a sensores y módulos. Las lecciones posteriores son más desafiantes para los principiantes.

(**Nota: Para evitar que la placa micro:bit se queme, desconecte el cable micro USB de la misma y apague la alimentación de la micro:bit motor driver base plate antes de instalarla en la placa de expansión del coche y ponga el interruptor POWER en OFF. Del mismo modo, antes de retirar la placa principal de la placa de expansión del coche, desconecte el cable micro USB de la misma y apague la alimentación de la micro:bit motor driver base plate.**)