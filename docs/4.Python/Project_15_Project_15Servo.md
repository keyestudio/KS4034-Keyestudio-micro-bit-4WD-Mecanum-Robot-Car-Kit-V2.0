### Proyecto 15：Servo

![](./media/Python_c4b5e57b.png)

1\.  **Descripción**

Los coches inteligentes DIY suelen incluir la función de evitación automática de obstáculos. En el proceso de montaje, necesitamos un servo para controlar que el módulo ultrasónico gire a la izquierda y a la derecha, y luego detectar la distancia entre el coche y el obstáculo, para poder controlar el coche y evitar el obstáculo.

Si se utilizan otros microcontroladores para controlar la rotación del servo, es necesario establecer una cierta frecuencia y anchura de pulso para controlar el ángulo del servo. Pero si se utiliza la placa principal micro:bit para controlar el ángulo del servo, basta con fijar el ángulo de control en el entorno de desarrollo; el pulso correspondiente se generará automáticamente para controlar la rotación del servo. En este proyecto aprenderás a controlar el servo para que oscile entre 0° y 90°.

El servomotor es un actuador giratorio de control de posición, que consiste principalmente en la carcasa, la placa de circuito, el motor sin núcleo, los engranajes y el sensor de posición. Su principio de funcionamiento es que el servo recibe la señal enviada por el MCU o el receptor, genera una señal de referencia con un periodo de 20 ms y una anchura de 1,5 ms, luego compara la tensión continua adquirida con la tensión del potenciómetro y obtiene la diferencia de tensión de salida.

Para el servo usado en este proyecto, el cable marrón es tierra, el rojo es positivo y el naranja es el cable de señal.

![](./media/Python_69be9581.png)

2\.  **Información del Servo**

El ángulo de rotación del servomotor se controla regulando el ciclo de trabajo de la señal PWM (modulación por ancho de pulso). El ciclo estándar de la señal PWM es 20 ms (50 Hz). Teóricamente, la anchura se distribuye entre 1 ms y 2 ms, pero en la práctica está entre 0.5 ms y 2.5 ms. La anchura corresponde al ángulo de rotación de 0° a 180°. Tenga en cuenta que para motores de distintas marcas, la misma señal puede dar lugar a ángulos de rotación diferentes.

![](./media/Python_0982cb7b.png)

Tras mediciones, el rango de pulso del servo es de 0,65 ms a 2,5 ms. Para un servo de 180 grados, la relación de control correspondiente es la siguiente:


|Time on High Level|Angle of the Servo|Reference Signal Cycle Time（20ms）|
|-|-|-|
|0.65ms|0 degree|0.65ms high level+19.35ms low level|
|1.5ms|90 degrees|1.5ms high level+18.5ms low level|
|2.5ms|180degrees|2.5ms high level+17.5ms low level|


3\.  **Parámetros**

- Voltaje de trabajo: DC 4.8V ~ 6V

- Rango de ángulo operativo: aproximadamente 180 ° (a 500 → 2500 μsec)

- Dimensiones: 22.9\*12.2\*30mm

- Rango de ancho de pulso: 500 → 2500 μsec

- Velocidad sin carga: 0.12 ± 0.01 s / 60 (DC 4.8V), 0.1 ± 0.01 s / 60 (DC 6V)

- Corriente sin carga: 200 ± 20mA (DC 4.8V), 220 ± 20mA (DC 6V)

- Par de retención: 1.3 ± 0.01kg · cm (DC 4.8V), 1.5 ± 0.1kg · cm (DC 6V)

- Corriente en parada: ≦ 850mA (DC 4.8V) ≦ 1000mA (DC 6V)

- Corriente de reposo: 3 ± 1mA (DC 4.8V), 4 ± 1mA (DC 6V)

- Peso: 9±1g (sin cuerno del servo)

- Temperatura de trabajo: -30℃~60℃

**Debe tenerse en cuenta que no utilice la alimentación de un ordenador, porque si la demanda de corriente es superior a 500 mA, el servo puede quemarse. Se recomienda usar una batería externa para la alimentación.**

4\.  **Preparación**

- Inserte la placa micro:bit en la ranura del keyestudio 4WD Mecanum Robot Car V2.0

- Coloque las pilas en el portapilas

- Lleve el interruptor de alimentación a la posición ON

- Conecte el micro:bit al ordenador mediante un cable USB

- Abra la versión sin conexión de Mu.

5\.  **Código de prueba**

Abra el software Mu y abra el archivo “Servo\.py” para importar el código. También puede introducir el código en la ventana del editor manualmente.

(**Nota: Todas las palabras y símbolos en inglés deben escribirse en inglés**.)

Haga clic en “Check” para comprobar errores en el código. El programa se considera erróneo si aparecen subrayados o cursores.

Si el código es correcto, conecte el micro:bit al ordenador y haga clic en “Flash” para descargar el código a la placa micro:bit.

![](./media/Python_eecf365e.png)

```python
from microbit import *

class Servo:
    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.analog_period = 0
        self.pin = pin
        analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
        self.pin.set_analog_period(analog_period)

    def write_us(self, us):
        us = min(self.max_us, max(self.min_us, us))
        duty = round(us * 1024 * self.freq // 1000000)
        self.pin.write_analog(duty)
        sleep(100)
        self.pin.write_analog(0)

    def write_angle(self, degrees=None):
        if degrees is None:
            degrees = math.degrees(radians)
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.write_us(us)

Servo(pin14).write_angle(0)
display.show(Image.HAPPY)

while True:
        Servo(pin14).write_angle(0)
        sleep(1000)
        Servo(pin14).write_angle(45)
        sleep(1000)
        Servo(pin14).write_angle(90)
        sleep(1000)
        Servo(pin14).write_angle(135)
        sleep(1000)
        Servo(pin14).write_angle(180)
        sleep(1000)

```

4\.  **Resultado de la prueba**

Después de descargar el código a la placa con éxito, **alimente externamente (mueva el interruptor DIP a ON)** y presione el botón de reinicio en el micro:bit.

![Img](./media/Python_bb3e1312.png)

La matriz de LED muestra un patrón sonriente y el servo gira en el patrón 0°~45°~90°~135°~180°~0°.

---