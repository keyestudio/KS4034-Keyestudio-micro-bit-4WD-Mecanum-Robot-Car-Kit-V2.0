### Proyecto 13: LED de siete colores

![](./media/Python_804e502b.png)

1\.  **Descripción**

Este módulo consiste en un LED de uso común con 7 colores pero de apariencia blanca. Puede parpadear automáticamente diferentes colores para crear efectos de luz fantásticos cuando se aplica un nivel alto, como una LED normal.

2\.  **Preparación**

- Inserte la placa micro:bit en la ranura del keyestudio 4WD Mecanum Robot Car V2.0

- Coloque las baterías en el portapilas

- Gire el interruptor de alimentación a la posición ON

- Conecte el micro:bit a su ordenador mediante un cable USB

- Abra la versión sin conexión de Mu.

3\.  **Código de prueba**

Abra el software Mu y abra el archivo“Colorful lights\.py”para importar el código. También puede introducir el código usted mismo en la ventana de edición.

(**Nota: Todas las palabras y símbolos deben escribirse en inglés**.)

![](./media/Python_010a8a12.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *

mecanumCar = Mecanum_Car_Driver_V2()

while True:
    mecanumCar.left_led(1)
    mecanumCar.right_led(1)
    sleep(3000)
    mecanumCar.left_led(0)
    mecanumCar.right_led(0)
    sleep(3000)
```

**Aviso importante:** Si el archivo de biblioteca 'keyes_mecanum_Car_V2.py' aún no se ha importado en la placa micro:bit, es imprescindible importar primero el archivo de la biblioteca a la placa micro:bit. El método para importar la biblioteca se encuentra haciendo clic en el enlace: [How to Import Library to Micro:bit](https://docs.keyestudio.com/projects/KS4034/en/latest/docs/Python/Python.html#how-mu-import-library-to-micro-bit) y siguiendo las instrucciones proporcionadas; de lo contrario, el código no se ejecutará.

Después de que el archivo de biblioteca se importe correctamente, también debe hacer clic en el botón "Check" para comprobar el código. Si un cursor o un subrayado aparece en una determinada línea, entonces hay errores en el programa.

![](./media/Python_ce67f468.png)

Sin embargo, durante este proceso aparecerá el siguiente aviso incluso si no hay ningún error en el código. Estas advertencias son solo avisos y no mensajes de error del código.

![](./media/Python_863bb61b.png)

![](./media/Python_ccfbfa56.png)

Si el código es correcto, conecte el micro:bit a su ordenador y haga clic en“Flash”para descargar el código a la placa micro:bit.

![](./media/Python_39512a13.png)

Si aparecen errores después de hacer clic en el botón "Flash", confirme si ha importado el archivo de biblioteca proporcionado "keyes_mecanum_Car_V2.py".

**Nota:** Antes de programar con Micropython, debe importar el archivo de biblioteca "keyes_mecanum_Car_V2.py" al micro:bit. Si programa con un micro:bit diferente, el archivo de biblioteca "keyes_mecanum_Car_V2.py" debe importarse nuevamente al nuevo micro:bit.

4\. **Resultado de la prueba**

Después de descargar el código en la placa correctamente, **alimentación externa (ponga el interruptor DIP en ON)**, y presione el botón de reinicio en el micro:bit.

![Img](./media/Python_bb3e1312.png)

El LED de siete colores parpadeará durante 3s y luego se detendrá durante 3s y repetirá este patrón.

5\. **Explicación del código**

![Img](./media/Python_a4a670c0.png)