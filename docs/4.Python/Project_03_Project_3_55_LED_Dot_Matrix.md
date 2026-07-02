### Proyecto 3：Matriz de puntos LED 5×5

![](./media/Python_b855274f.png)

1\.  **Descripción**

La matriz de puntos es muy común en la vida diaria y tiene amplias aplicaciones en pantallas publicitarias LED, indicadores de planta de ascensores, anuncios en paradas de autobús, etc.
La matriz LED de la placa principal Micro: Bit contiene 25 diodos. Anteriormente, hemos logrado controlar un LED específico mediante su posición. Con la misma teoría, podemos encender muchas LEDs al mismo tiempo para mostrar patrones, dígitos y caracteres.

Además, también podemos hacer clic en “show icon” para elegir el patrón que queremos mostrar. Por último, también podemos diseñar nuestros propios patrones.

2\.  **Preparación**

A. Conecte la placa principal micro:bit a su ordenador mediante el cable USB

B. Abra la versión offline de Mu.

3\.  **Código de prueba1**

Puede abrir el archivo “5×5 LED Dot Matrix-1\.py” para importar el código. También puede introducir el código en la ventana de edición usted mismo.

(**Nota: Todas las palabras y símbolos deben escribirse en inglés.**)

![](./media/Python_00f15f0a.png)

```python
from microbit import *

val = Image("00900:""00900:""90909:""09990:""00900")

display.show(val)
```

Haga clic en “Check” para examinar los errores en el código. El programa será incorrecto si se muestran subrayados y cursores. 

![](./media/Python_a1197f5e.png)

Si el código es correcto, conecte el micro:bit al ordenador y haga clic en “Flash” para descargar el código a la placa micro:bit.

![](./media/Python_1fd78e31.png)

4\.  **Resultado de la prueba1**

Tras descargar el código en la placa correctamente, **alimente mediante el cable micro USB o una fuente de alimentación externa (coloque el interruptor DIP en ON)** y pulse el botón de reinicio en la placa.

![Img](./media/Python_bb3e1312.png)

Veremos que la matriz 5×5 comienza a mostrar una flecha hacia abajo ![](./media/Python_26c7d8c0.png).

5\.  **Código de prueba2**

Puede abrir el archivo “5×5 LED Dot Matrix-2\.py” para importar el código. También puede introducir el código en la ventana de edición usted mismo.

(**Nota: Todas las palabras y símbolos deben escribirse en inglés.**)

![](./media/Python_dc6eea45.png)

```python
from microbit import *
val = Image("00900:""00900:""90909:""09990:""00900")
display.show('1')
sleep(500)
display.show('2')
sleep(500)
display.show('3')
sleep(500)
display.show('4')
sleep(500)
display.show('5')
sleep(500)
display.show(val)
sleep(500)
display.scroll("hello!")
sleep(200)
display.show(Image.HEART)
sleep(500)
display.show(Image.ARROW_NE)
sleep(500)
display.show(Image.ARROW_SE)
sleep(500)
display.show(Image.ARROW_SW)
sleep(500)
display.show(Image.ARROW_NW)
sleep(500)
display.clear()
```

Haga clic en “Check” para examinar errores en el código. El programa será incorrecto si se muestran subrayados y cursores. 

![](./media/Python_14bb490a.png)

Si el código es correcto, conecte el micro:bit al ordenador y haga clic en “Flash” para descargar el código a la placa micro:bit.

![](./media/Python_a05c33d2.png)

6\.  **Resultado de la prueba2**

Tras descargar el código en la placa correctamente, **alimente mediante el cable micro USB o una fuente de alimentación externa (coloque el interruptor DIP en ON)** y pulse el botón de reinicio en la placa.

![Img](./media/Python_bb3e1312.png)

Veremos que la matriz 5×5 comienza a mostrar los números 1, 2, 3, 4 y 5 y luego muestra alternativamente una flecha hacia abajo ![](./media/Python_26c7d8c0.png), “Hello”, un patrón de corazón ![](./media/Python_9b18b2b8.png), una flecha apuntando al noreste ![](./media/Python_364f2e35.png), luego al sureste
![](./media/Python_fb3ba009.png), luego al suroeste ![](./media/Python_7ec21961.png) y finalmente al noroeste ![](./media/Python_ced0bb41.png).

7\.  **Explicación del código**

![Img](./media/Python_ef42956d.png)


6.  **Referencia**

display.scroll() ：

La pantalla se desplaza para mostrar los valores; si es un entero o un float, usamos str() para convertirlo en cadenas de caracteres.

Para más detalles, consulte el enlace: [https://microbit-micropython.readthedocs.io/en/latest/utime.html](https://microbit-micropython.readthedocs.io/en/latest/utime.html)