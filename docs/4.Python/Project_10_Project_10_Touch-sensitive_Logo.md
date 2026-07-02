### Proyecto 10: Logo sensible al tacto

![](./media/Python_64469585.png)

1\.  **Descripción**

La placa principal micro:bit V2 está equipada con un logotipo dorado sensible al tacto, que puede actuar como un componente de entrada similar a un botón.

Contiene un sensor táctil capacitivo que detecta pequeños cambios en el campo eléctrico cuando se presiona (o toca), igual que la pantalla de tu teléfono o tablet. Cuando lo presionas, el programa puede activarse.

2\.  **Preparación**

A. Conecta la placa principal micro:bit a tu ordenador mediante el cable USB.

B. Abre la versión offline de Mu.

3\.  **Código de prueba**

Abre el software Mu y abre el archivo “Touch-sensitive Logo\.py” para importar el código. También puedes introducir el código tú mismo en la ventana de edición.

(**Nota: Todas las palabras y símbolos en inglés deben escribirse en inglés**.)

![](./media/Python_0c54cbe5.png)

```python
from microbit import *
time = 0
start = 0
running = False

while True:

    if button_a.was_pressed():
        running = True
        start = running_time()
    if button_b.was_pressed():
        if running:
            time += running_time() - start
        running = False
    if pin_logo.is_touched():
        if not running:
            display.scroll(int(time/1000))

    if running:
        display.show(Image.HEART)
        sleep(300)
        display.show(Image.HEART_SMALL)
        sleep(300)
    else:
        display.show(Image.ASLEEP)
```

**¿Cómo funciona el Micro:bit?**

A\. El tiempo de ejecución se registra en milisegundos (ms).

B\. Cuando presionas el botón A, una variable llamada start se establecerá en el tiempo de ejecución actual.

C\. Cuando presionas el botón B, el tiempo de inicio se sustrae del nuevo tiempo de ejecución para calcular el tiempo transcurrido desde que comenzaste el cronómetro. Esta diferencia se añade al tiempo total, que se almacena en una variable llamada time.

D\. Si presionas el logo dorado, el programa mostrará el tiempo total transcurrido en la pantalla LED. Convierte el tiempo de milisegundos (milésimas de segundo) a segundos dividiendo por 1000. Usa el operador de división entera para dar un resultado entero.

E\. El programa también está controlado por una variable booleana llamada running. Una variable booleana solo tiene dos valores: true o false. Si "running" es "true", significa que el cronómetro se ha iniciado. Si "running" es false, significa que el cronómetro no se ha iniciado o se ha detenido.

F\. Si "running" es true, el patrón de corazón latiendo se mostrará en la pantalla de matriz de LED.

G\. (7) Si el cronómetro se ha detenido y "running" es false, cuando presiones el logo dorado, solo mostrará el tiempo.

H\. Si el cronómetro se ha iniciado y "running" es true, solo es necesario asegurarse de que la variable time cambie cuando se presione el botón B, y el código también puede prevenir lecturas falsas.

Haz clic en “Check” para examinar errores en el código. El programa es incorrecto si se muestran subrayados y cursores.

![](./media/Python_1766a28c.png)

Si el código es correcto, conecta el micro:bit a tu ordenador y haz clic en “Flash” para descargar el código en la placa micro:bit.

![](./media/Python_a3d6e994.png)

4\.  **Resultado de la prueba**

Después de descargar el código en la placa correctamente, **alimentar mediante el cable micro USB o una fuente de alimentación externa (coloca el interruptor DIP en ON)** y presiona el botón de reinicio del micro:bit.

![Img](./media/Python_bb3e1312.png)

Pulsa el botón A para iniciar el cronómetro. Durante la medición, el patrón de corazón latiendo se mostrará en la matriz de LED. Pulsa el botón B para detenerlo; puedes iniciarlo y detenerlo en cualquier momento.

Seguirá registrando el tiempo, igual que un cronómetro real. Pulsa el logo dorado en la parte frontal del micro:bit para mostrar el tiempo medido en segundos. Y el tiempo puede restablecerse a cero pulsando el botón de reinicio en la parte posterior.

---