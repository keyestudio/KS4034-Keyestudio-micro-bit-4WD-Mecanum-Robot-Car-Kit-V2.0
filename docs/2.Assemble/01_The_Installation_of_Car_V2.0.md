## De installatie van de Keyestudio 4WD Mecanum Robot Car V2.0

### Stap 1

**Benodigde componenten:**

![](./media/Assemble_Mecanum_Robot_f3d856b4.png)

**Installatieschema:**

![](./media/Assemble_Mecanum_Robot_3d1dbf07.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_f5d38786.png)

### Stap 2

**Benodigde componenten:**

![](./media/Assemble_Mecanum_Robot_a2ee8074.png)

**Installatieschema:**

![](./media/Assemble_Mecanum_Robot_6fdf9d4d.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_3fec7c19.png)

### Stap 3

**Benodigde componenten:**

![](./media/Assemble_Mecanum_Robot_d4f24cc5.png)

**Installatieschema:**

![](./media/Assemble_Mecanum_Robot_e1d7b425.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_cc96b9d6.png)

### Stap 4

（stel eerst de hoek van de servo af）

**Stel de hoek van de servo in op 90 graden.**

**Methode 1: MakeCode-code**

⚠️**Bijzondere opmerking:** Voordat u de code schrijft en uploadt, moet u de MakeCode IDE begrijpen en bibliotheekbestanden toevoegen. Ga naar de volgende link: [Get Started with makecode](./Code1.7z)

![](./media/Assemble_Mecanum_Robot_a9ff633c.png)

De bovenstaande MakeCode-code wordt meegeleverd in het materiaal. Open de afstelcode voor de servo en schrijf deze naar het microbit‑board van de 4WD Mecanum Robot Car V2.0, en **zet stroom via micro USB‑kabel of externe voeding (zet de DIP switch op ON)**. Dat is alles. De code bevindt zich op de positie zoals in de afbeelding getoond:

![Img](./media/Assemble_Mecanum_Robot_21db9fa2.png)

**Methode 2：Python-code**

⚠️**Bijzondere opmerking:** Voordat u de code schrijft en uploadt, moet u de Mu IDE installeren en bibliotheekbestanden toevoegen. Ga naar de volgende link: [Get Started with Python](./Code2.7z)

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

**Benodigde componenten:**

![](./media/Assemble_Mecanum_Robot_1e3fd9e2.png)

Installatieschema: (let op de montagerichting)

![](./media/Assemble_Mecanum_Robot_9ca5d2c8.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_9b8bccaa.png)

### Stap 5

**Benodigde componenten:**

![](./media/Assemble_Mecanum_Robot_8d138501.png)

**Installatieschema:**

![](./media/Assemble_Mecanum_Robot_bda8fbc4.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_9f244272.png)

### Stap 6

**Benodigde componenten:**

![](./media/Assemble_Mecanum_Robot_36259594.png)

**Installatieschema:**

![](./media/Assemble_Mecanum_Robot_6d3e3ad9.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_3c33f63b.png)

### Stap 7

**Benodigde componenten:**

![](./media/Assemble_Mecanum_Robot_817e834e.png)

**Installatieschema:** (let op de richting van de motor)

![](./media/Assemble_Mecanum_Robot_09a61aa6.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_8c97de28.png)

### Stap 8

**Benodigde componenten:**

![](./media/Assemble_Mecanum_Robot_43bac346.png)

**Installatieschema:** (let op de montage richting van het mecanum-wiel)

![](./media/Assemble_Mecanum_Robot_d92dee68.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_64467ed0.png)

### Stap 9

**Benodigde componenten:**

![](./media/Assemble_Mecanum_Robot_5c38573f.png)

**Installatieschema:**

![](./media/Assemble_Mecanum_Robot_a72469e3.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_243aa35b.png)

### Stap 10

**Benodigde componenten:**

![](./media/Assemble_Mecanum_Robot_b60b9f16.png)

**Installatieschema:**

![](./media/Assemble_Mecanum_Robot_55f2db60.png)

**Prototype:**

![](./media/Assemble_Mecanum_Robot_456df8a0.png)

### Bedradingsschema

**De bedrading van de servo:**

![Img](./media/Assemble_Mecanum_Robot_c82a9395.png)

![](./media/Assemble_Mecanum_Robot_859cd41e.jpg)

![](./media/Assemble_Mecanum_Robot_b3bcce9d.png)

**De bedrading van de ultrasone sensor:**

![Img](./media/Assemble_Mecanum_Robot_c9f3da75.png)

![](./media/Assemble_Mecanum_Robot_5747ad7c.jpg)

![](./media/Assemble_Mecanum_Robot_a8f0e176.png)

**De bedrading van de IR-ontvangermodule:**

![Img](./media/Assemble_Mecanum_Robot_61d53b21.png)

![](./media/Assemble_Mecanum_Robot_1e081a3a.png)

**De bedrading van de RGB:**

![Img](./media/Assemble_Mecanum_Robot_c5b8a804.png)

![](./media/Assemble_Mecanum_Robot_01848b2e.jpg)

**De bedrading voor het aansturen van de motor en de zeven-kleurige lamp:**

![Img](./media/Assemble_Mecanum_Robot_0c4635c5.png)

![](./media/Assemble_Mecanum_Robot_1689f2c9.jpg)

**De bedrading voor het aansturen van de 3-kanaals lijnvolgsensor:**

![Img](./media/Assemble_Mecanum_Robot_542d1798.png)

![](./media/Assemble_Mecanum_Robot_08eb8d7e.jpg)

**De bedrading van de voeding:**

![](./media/Assemble_Mecanum_Robot_cdcec4ba.jpg)

**De corresponderende interface van de motor:**

![](./media/Assemble_Mecanum_Robot_ffcceef1.jpg)

**De installatie van de batterij:**

![](./media/Assemble_Mecanum_Robot_fe8ce786.png)