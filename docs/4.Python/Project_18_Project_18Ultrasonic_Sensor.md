### Proyecto 18：Sensor ultrasónico

#### Proyecto 18.1：Medición por ultrasonidos

1\. **Descripción**

![](./media/Python_9810ae67.jpg)

El sensor ultrasónico utiliza sonar para determinar la distancia a un objeto, como lo hacen los murciélagos. Ofrece una excelente detección de rango sin contacto con alta precisión y lecturas estables en un paquete fácil de usar. Incluye módulos transmisor y receptor ultrasónicos.

El sensor ultrasónico se utiliza en una amplia gama de proyectos electrónicos para crear aplicaciones de detección de obstáculos y medición de distancia, así como en diversas otras aplicaciones.

![](./media/Python_0180b169.png)

El módulo ultrasónico emitirá las ondas ultrasónicas tras la señal de trigger. Cuando las ondas ultrasónicas encuentran el objeto y se reflejan, el módulo emite una señal de eco, por lo que puede determinar la distancia al objeto a partir de la diferencia de tiempo entre la señal de trigger (TRIG) y la señal de eco (ECHO).

Como muestra la imagen, es como dos ojos. Uno es el extremo transmisor y el otro el extremo receptor.

Según el diagrama de conexión anterior, el puerto integrado del módulo del sensor ultrasónico está conectado al puerto 5V G P15 P16 en la placa base del controlador de motor micro:bit. El pin Trig (T) está controlado por P15 del micro:bit y el pin Echo (E) por P16.

![](./media/Python_19b45a23.jpg)

2\. **Principio de funcionamiento**

![](./media/Python_8ff02741.png)

(1) Llevar TRIG a nivel bajo y luego generar una señal de nivel alto con al menos 10 µs;

(2) Tras el disparo, el módulo enviará automáticamente ocho pulsos ultrasónicos de 40 kHz y detectará si hay retorno de señal;

(3) Si hay retorno de señal, cuando ECHO (E) salga a nivel alto, la duración del nivel alto es el tiempo desde la transmisión hasta la recepción de las ondas ultrasónicas. Entonces la distancia de prueba = duración del nivel alto \*340 m/s\*0.5.

3\.  **Parámetros**

- Voltaje de trabajo: 3-5.5V (DC)

- Corriente de trabajo: 15mA

- Frecuencia de trabajo: 40kHz

- Distancia máxima de detección: aproximadamente 3 m

- Distancia mínima de detección: 2-3 cm

- Precisión: hasta 0.2 cm

- Ángulo de detección: menos de 15 grados

- Pulso de trigger de entrada: 10us, nivel TTL

- Señal de eco de salida: señal de nivel TTL (alto), proporcional a la distancia

4\.  **Preparación**

- Inserte la placa micro:bit en la ranura del keyestudio 4WD Mecanum Robot Car V2.0

- Coloque las baterías en el portabaterías

- Coloque el interruptor de alimentación en ON

- Conecte el micro:bit al ordenador mediante un cable USB

- Abra la versión offline de Mu.

5\.  **Código de prueba**

Abra el software Mu y cargue el archivo “Ultrasonic Ranging\.py” para importar el código. También puede introducir el código en la ventana de edición usted mismo.

(Nota: Todas las palabras y símbolos en inglés deben permanecer en inglés.)

Haga clic en “Files” para importar el archivo de biblioteca “keyes_mecanum_Car_V2.py” al micro:bit.

Haga clic en “Check” para examinar errores en el código. El programa es incorrecto si se muestran subrayados y cursores.

Si el código es correcto, conecte el micro:bit a su ordenador y haga clic en “Flash” para descargar el código a la placa micro:bit.

![](./media/Python_5a29bde9.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()
import music
tune = ["C4:4"]
distance_val = 0

while True:
    i = 0
    distance_val = mecanumCar.get_distance()
    print("distance:", distance_val)
    if distance_val < 10:
        while i < 1:
            music.play(tune)
            sleep(200)
            music.play(tune)
            sleep(200)
            i += 1

```

6\.  **Resultado de la prueba**

Después de descargar el código a la placa con éxito y sin desconectar el cable USB, haga clic en “REPL” y luego presione el botón de reset.

![Img](./media/Python_bb3e1312.png)

Se mostrará el valor de distancia del obstáculo, como se muestra a continuación.

Cuando la distancia sea menor de 10 cm, el zumbador pasivo del coche emitirá sonido.

![](./media/Python_4dc8054e.png)

7\.  **Explicación del código**

![Img](./media/Python_ebde06e9.png)

#### Proyecto 18.2：Evitación por ultrasonidos

![](./media/Python_aee41f6f.jpg)

1\. **Descripción**

En este proyecto integraremos un sensor ultrasónico y un coche para crear un coche de evitación por ultrasonidos.

Su principio es detectar la distancia entre el coche y el obstáculo mediante el sensor ultrasónico para controlar el movimiento del coche inteligente.

2\. **Preparación**

- Inserte la placa micro:bit en la ranura del keyestudio 4WD Mecanum Robot Car V2.0

- Coloque las baterías en el portabaterías

- Coloque el interruptor de alimentación en ON

- Conecte el micro:bit al ordenador mediante un cable USB

- Abra la versión offline de Mu.

3\.  **Diagrama de flujo**

![Img](./media/Python_a4efee72.png)

4\.  **Código de prueba**

Abra el software Mu y cargue el archivo “Ultrasonic Avoid Smart Car\.py” para importar el código. También puede introducir el código en la ventana de edición usted mismo.

(Nota: Todas las palabras y símbolos en inglés deben permanecer en inglés.)

Haga clic en “Files” para importar el archivo de biblioteca “keyes_mecanum_Car_V2.py” al micro:bit.

Haga clic en “Check” para examinar errores en el código. El programa es incorrecto si se muestran subrayados y cursores.

Si el código es correcto, conecte el micro:bit a su ordenador y haga clic en “Flash” para descargar el código a la placa micro:bit.

![](./media/Python_38f3510c.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()
distance_val = 0
distance_l = 0
distance_r = 0
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

Servo(pin14).write_angle(90)

while True:

    distance_val = mecanumCar.get_distance()

    if distance_val < 20:
        mecanumCar.Motor_Upper_L(0, 0)
        mecanumCar.Motor_Lower_L(0, 0)
        mecanumCar.Motor_Upper_R(0, 0)
        mecanumCar.Motor_Lower_R(0, 0)
        sleep(500)
        Servo(pin14).write_angle(180)
        sleep(500)
        distance_l = mecanumCar.get_distance()
        sleep(500)

        Servo(pin14).write_angle(0)
        sleep(500)
        distance_r = mecanumCar.get_distance()
        sleep(500)

        if distance_l > distance_r:
            mecanumCar.Motor_Upper_L(0, 100)
            mecanumCar.Motor_Lower_L(0, 100)
            mecanumCar.Motor_Upper_R(1, 100)
            mecanumCar.Motor_Lower_R(1, 100)
            Servo(pin14).write_angle(90)
            sleep(300)
        else:
            mecanumCar.Motor_Upper_L(1, 100)
            mecanumCar.Motor_Lower_L(1, 100)
            mecanumCar.Motor_Upper_R(0, 100)
            mecanumCar.Motor_Lower_R(0, 100)
            Servo(pin14).write_angle(90)
            sleep(300)

    else:
        mecanumCar.Motor_Upper_L(1, 100)
        mecanumCar.Motor_Lower_L(1, 100)
        mecanumCar.Motor_Upper_R(1, 100)
        mecanumCar.Motor_Lower_R(1, 100)
```

5\.  **Resultado de la prueba**

Después de descargar el código a la placa con éxito, **alimentación externa (poner el interruptor DIP en ON)**, y presione el botón de reset en el micro:bit.

![Img](./media/Python_bb3e1312.png)

Cuando la distancia al obstáculo es mayor de 20 cm, el coche avanza; por el contrario, el coche inteligente gira a la izquierda.

6\.  **Explicación del código**

![Img](./media/Python_9e28cce7.png)

![Img](./media/Python_c33a22a8.png)

#### Proyecto 18.3：Seguimiento por ultrasonidos

![](./media/Python_28806167.jpg)

1\. **Descripción**

En la lección anterior aprendimos el principio básico del sensor de seguimiento de línea. A continuación, combinaremos el sensor ultrasónico con el coche para crear un coche seguidor por ultrasonidos.

El sensor ultrasónico detecta la distancia al obstáculo y controla el estado de movimiento del coche.

2\. **Preparación**

- Inserte la placa micro:bit en la ranura del keyestudio 4WD Mecanum Robot Car V2.0

- Coloque las baterías en el portabaterías

- Coloque el interruptor de alimentación en ON

- Conecte el micro:bit al ordenador mediante un cable USB

- Abra la versión offline de Mu.

2\.  **Diagrama de flujo**

![Img](./media/Python_53a30906.png)

3\.  **Código de prueba**

Abra el software Mu y cargue el archivo “Ultrasonic Follow Smart Car\.py” para importar el código. También puede introducir el código en la ventana de edición usted mismo.

(Nota: Todas las palabras y símbolos en inglés deben permanecer en inglés.)

Haga clic en “Files” para importar el archivo de biblioteca “keyes_mecanum_Car_V2.py” al micro:bit.

Haga clic en “Check” para examinar errores en el código. El programa es incorrecto si se muestran subrayados y cursores.

Si el código es correcto, conecte el micro:bit a su ordenador y haga clic en “Flash” para descargar el código a la placa micro:bit.

![](./media/Python_f586f3f7.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *
import neopixel
display.off()

mecanumCar = Mecanum_Car_Driver_V2()
np = neopixel.NeoPixel(pin7, 4)

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

Servo(pin14).write_angle(90)

while True:
    distance_val = 0
    distance_val = mecanumCar.get_distance()
    if distance_val >= 20 and distance_val <= 40:
        mecanumCar.Motor_Upper_L(1, 80)
        mecanumCar.Motor_Lower_L(1, 80)
        mecanumCar.Motor_Upper_R(1, 80)
        mecanumCar.Motor_Lower_R(1, 80)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 0, 0)
            np.show()
    if distance_val <= 10:
        mecanumCar.Motor_Upper_L(0, 80)
        mecanumCar.Motor_Lower_L(0, 80)
        mecanumCar.Motor_Upper_R(0, 80)
        mecanumCar.Motor_Lower_R(0, 80)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 255, 0)
            np.show()
    if distance_val > 10 and distance_val < 20 or distance_val > 40:
        mecanumCar.Motor_Upper_L(0, 0)
        mecanumCar.Motor_Lower_L(0, 0)
        mecanumCar.Motor_Upper_R(0, 0)
        mecanumCar.Motor_Lower_R(0, 0)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 255, 255)
            np.show()
```

4\.  **Resultado de la prueba**

Después de descargar el código a la placa con éxito, **alimentación externa (poner el interruptor DIP en ON)**, y presione el botón de reset en el micro:bit.

![Img](./media/Python_bb3e1312.png)

El coche inteligente podrá seguir el obstáculo en movimiento y las 4 luces RGB WS2812 mostrarán diferentes colores.

Nota: el obstáculo sólo puede moverse frente al coche inteligente.

5\.  **Explicación del código**

![Img](./media/Python_930a04fa.png)

![Img](./media/Python_26371a4d.png)