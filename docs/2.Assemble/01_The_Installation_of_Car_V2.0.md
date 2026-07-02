## La instalación del Keyestudio 4WD Mecanum Robot Car V2.0

### Paso 1

**Componentes necesarios:**

![](./media/Assemble_Mecanum_Robot_f3d856b4.png)

**Diagrama de instalación:**

![](./media/Assemble_Mecanum_Robot_3d1dbf07.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_f5d38786.png)

### Paso 2

**Componentes necesarios:**

![](./media/Assemble_Mecanum_Robot_a2ee8074.png)

**Diagrama de instalación:**

![](./media/Assemble_Mecanum_Robot_6fdf9d4d.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_3fec7c19.png)

### Paso 3

**Componentes necesarios:**

![](./media/Assemble_Mecanum_Robot_d4f24cc5.png)

**Diagrama de instalación:**

![](./media/Assemble_Mecanum_Robot_e1d7b425.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_cc96b9d6.png)

### Paso 4

（ajuste primero el ángulo del servo）

**Ajuste el ángulo del servo a 90 grados.**

**Método 1: código MakeCode**

⚠️**Nota especial:** Antes de escribir el código y cargarlo, debe comprender el IDE MakeCode y añadir archivos de biblioteca. Por favor visite el enlace: [Get Started with makecode](./Code1.7z)

![](./media/Assemble_Mecanum_Robot_a9ff633c.png)

El código MakeCode anterior se proporciona en los materiales. Abra el código de ajuste del servo y grábelo en la placa microbit del 4WD Mecanum Robot Car V2.0, y **enciéndalo mediante cable micro USB o fuente de alimentación externa (ponga el DIP switch en ON)**. Eso es todo. El código está en la posición indicada en la figura:

![Img](./media/Assemble_Mecanum_Robot_21db9fa2.png)

**Método 2：código Python**

⚠️**Nota especial:** Antes de escribir el código y cargarlo, debe instalar Mu IDE y añadir archivos de biblioteca. Por favor visite el enlace: [Get Started with Python](./Code2.7z)

```Python
# import microbit related libraries
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


Servo(pin14).write_angle(90)
sleep(1000)
```

**Componentes necesarios:**

![](./media/Assemble_Mecanum_Robot_1e3fd9e2.png)

Diagrama de instalación: (preste atención a la dirección de instalación)

![](./media/Assemble_Mecanum_Robot_9ca5d2c8.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_9b8bccaa.png)

### Paso 5

**Componentes necesarios:**

![](./media/Assemble_Mecanum_Robot_8d138501.png)

**Diagrama de instalación:**

![](./media/Assemble_Mecanum_Robot_bda8fbc4.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_9f244272.png)

### Paso 6

**Componentes necesarios:**

![](./media/Assemble_Mecanum_Robot_36259594.png)

**Diagrama de instalación:**

![](./media/Assemble_Mecanum_Robot_6d3e3ad9.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_3c33f63b.png)

### Paso 7

**Componentes necesarios:**

![](./media/Assemble_Mecanum_Robot_817e834e.png)

**Diagrama de instalación:** (preste atención a la dirección del motor)

![](./media/Assemble_Mecanum_Robot_09a61aa6.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_8c97de28.png)

### Paso 8

**Componentes necesarios:**

![](./media/Assemble_Mecanum_Robot_43bac346.png)

**Diagrama de instalación:** (preste atención a la dirección de instalación de la rueda mecanum)

![](./media/Assemble_Mecanum_Robot_d92dee68.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_64467ed0.png)

### Paso 9

**Componentes necesarios:**

![](./media/Assemble_Mecanum_Robot_5c38573f.png)

**Diagrama de instalación:**

![](./media/Assemble_Mecanum_Robot_a72469e3.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_243aa35b.png)

### Paso 10

**Componentes necesarios:**

![](./media/Assemble_Mecanum_Robot_b60b9f16.png)

**Diagrama de instalación:**

![](./media/Assemble_Mecanum_Robot_55f2db60.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_456df8a0.png)

### Diagrama de cableado

**El cableado del servo:**

![Img](./media/Assemble_Mecanum_Robot_c82a9395.png)

![](./media/Assemble_Mecanum_Robot_859cd41e.jpg)

![](./media/Assemble_Mecanum_Robot_b3bcce9d.png)

**El cableado del sensor ultrasónico:**

![Img](./media/Assemble_Mecanum_Robot_c9f3da75.png)

![](./media/Assemble_Mecanum_Robot_5747ad7c.jpg)

![](./media/Assemble_Mecanum_Robot_a8f0e176.png)

**El cableado del módulo receptor IR:**

![Img](./media/Assemble_Mecanum_Robot_61d53b21.png)

![](./media/Assemble_Mecanum_Robot_1e081a3a.png)

**El cableado del RGB:**

![Img](./media/Assemble_Mecanum_Robot_c5b8a804.png)

![](./media/Assemble_Mecanum_Robot_01848b2e.jpg)

**El cableado para controlar el motor y la luz de siete colores:**

![Img](./media/Assemble_Mecanum_Robot_0c4635c5.png)

![](./media/Assemble_Mecanum_Robot_1689f2c9.jpg)

**El cableado para controlar el sensor de seguimiento de línea de 3 canales:**

![Img](./media/Assemble_Mecanum_Robot_542d1798.png)

![](./media/Assemble_Mecanum_Robot_08eb8d7e.jpg)

**El cableado de la alimentación:**

![](./media/Assemble_Mecanum_Robot_cdcec4ba.jpg)

**La interfaz correspondiente del motor:**

![](./media/Assemble_Mecanum_Robot_ffcceef1.jpg)

**La instalación de la batería:**

![](./media/Assemble_Mecanum_Robot_fe8ce786.png)