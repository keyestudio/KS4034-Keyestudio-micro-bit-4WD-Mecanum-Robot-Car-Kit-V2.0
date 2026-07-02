## L'installazione del Keyestudio 4WD Mecanum Robot Car V2.0

### Passo 1

**Componenti necessari:**

![](./media/Assemble_Mecanum_Robot_f3d856b4.png)

**Diagramma di installazione:**

![](./media/Assemble_Mecanum_Robot_3d1dbf07.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_f5d38786.png)

### Passo 2

**Componenti necessari:**

![](./media/Assemble_Mecanum_Robot_a2ee8074.png)

**Diagramma di installazione:**

![](./media/Assemble_Mecanum_Robot_6fdf9d4d.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_3fec7c19.png)

### Passo 3

**Componenti necessari:**

![](./media/Assemble_Mecanum_Robot_d4f24cc5.png)

**Diagramma di installazione:**

![](./media/Assemble_Mecanum_Robot_e1d7b425.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_cc96b9d6.png)

### Passo 4

（regolare prima l'angolo del servo）

**Regolare l'angolo del servo a 90 gradi.**

**Metodo 1: codice MakeCode**

⚠️**Nota speciale:** Prima di scrivere il codice e caricarlo, è necessario conoscere l'IDE MakeCode e aggiungere i file della libreria. Vai al link: [Get Started with makecode](./Code1.7z)

![](./media/Assemble_Mecanum_Robot_a9ff633c.png)

Il codice MakeCode sopra è fornito nei materiali. Apri il codice di regolazione del servo e scrivilo sulla scheda microbit del 4WD Mecanum Robot Car V2.0, e **alimentalo tramite cavo micro USB o alimentatore esterno (imposta il DIP switch su ON)**. Fatto. Il codice si trova nella posizione mostrata nella figura:

![Img](./media/Assemble_Mecanum_Robot_21db9fa2.png)

**Metodo 2：codice Python**

⚠️**Nota speciale:** Prima di scrivere il codice e caricarlo, è necessario installare Mu IDE e aggiungere i file della libreria. Vai al link: [Get Started with Python](./Code2.7z)

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

**Componenti necessari:**

![](./media/Assemble_Mecanum_Robot_1e3fd9e2.png)

Diagramma di installazione: (prestare attenzione alla direzione di montaggio)

![](./media/Assemble_Mecanum_Robot_9ca5d2c8.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_9b8bccaa.png)

### Passo 5

**Componenti necessari:**

![](./media/Assemble_Mecanum_Robot_8d138501.png)

**Diagramma di installazione:**

![](./media/Assemble_Mecanum_Robot_bda8fbc4.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_9f244272.png)

### Passo 6

**Componenti necessari:**

![](./media/Assemble_Mecanum_Robot_36259594.png)

**Diagramma di installazione:**

![](./media/Assemble_Mecanum_Robot_6d3e3ad9.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_3c33f63b.png)

### Passo 7

**Componenti necessari:**

![](./media/Assemble_Mecanum_Robot_817e834e.png)

**Diagramma di installazione:** (prestare attenzione alla direzione del motore)

![](./media/Assemble_Mecanum_Robot_09a61aa6.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_8c97de28.png)

### Passo 8

**Componenti necessari:**

![](./media/Assemble_Mecanum_Robot_43bac346.png)

**Diagramma di installazione:** (prestare attenzione alla direzione di montaggio della ruota mecanum)

![](./media/Assemble_Mecanum_Robot_d92dee68.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_64467ed0.png)

### Passo 9

**Componenti necessari:**

![](./media/Assemble_Mecanum_Robot_5c38573f.png)

**Diagramma di installazione:**

![](./media/Assemble_Mecanum_Robot_a72469e3.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_243aa35b.png)

### Passo 10

**Componenti necessari:**

![](./media/Assemble_Mecanum_Robot_b60b9f16.png)

**Diagramma di installazione:**

![](./media/Assemble_Mecanum_Robot_55f2db60.png)

**Prototipo:**

![](./media/Assemble_Mecanum_Robot_456df8a0.png)

### Schema elettrico

**Il cablaggio del servo:**

![Img](./media/Assemble_Mecanum_Robot_c82a9395.png)

![](./media/Assemble_Mecanum_Robot_859cd41e.jpg)

![](./media/Assemble_Mecanum_Robot_b3bcce9d.png)

**Il cablaggio del sensore ad ultrasuoni:**

![Img](./media/Assemble_Mecanum_Robot_c9f3da75.png)

![](./media/Assemble_Mecanum_Robot_5747ad7c.jpg)

![](./media/Assemble_Mecanum_Robot_a8f0e176.png)

**Il cablaggio del modulo ricevitore IR:**

![Img](./media/Assemble_Mecanum_Robot_61d53b21.png)

![](./media/Assemble_Mecanum_Robot_1e081a3a.png)

**Il cablaggio del RGB:**

![Img](./media/Assemble_Mecanum_Robot_c5b8a804.png)

![](./media/Assemble_Mecanum_Robot_01848b2e.jpg)

**Il cablaggio per il controllo del motore e della luce a sette colori:**

![Img](./media/Assemble_Mecanum_Robot_0c4635c5.png)

![](./media/Assemble_Mecanum_Robot_1689f2c9.jpg)

**Il cablaggio per il controllo del sensore di tracciamento linea a 3 canali:**

![Img](./media/Assemble_Mecanum_Robot_542d1798.png)

![](./media/Assemble_Mecanum_Robot_08eb8d7e.jpg)

**Il cablaggio dell'alimentazione:**

![](./media/Assemble_Mecanum_Robot_cdcec4ba.jpg)

**La corrispondente interfaccia del motore:**

![](./media/Assemble_Mecanum_Robot_ffcceef1.jpg)

**L'installazione della batteria:**

![](./media/Assemble_Mecanum_Robot_fe8ce786.png)