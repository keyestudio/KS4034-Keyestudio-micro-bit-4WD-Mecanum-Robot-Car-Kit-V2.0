## Die Installation des Keyestudio 4WD Mecanum Robot Car V2.0

### Schritt 1

**Benötigte Komponenten:**

![](./media/Assemble_Mecanum_Robot_f3d856b4.png)

**Installationsdiagramm:**

![](./media/Assemble_Mecanum_Robot_3d1dbf07.png)

**Prototyp:**

![](./media/Assemble_Mecanum_Robot_f5d38786.png)

### Schritt 2

**Benötigte Komponenten:**

![](./media/Assemble_Mecanum_Robot_a2ee8074.png)

**Installationsdiagramm:**

![](./media/Assemble_Mecanum_Robot_6fdf9d4d.png)

**Prototyp:**

![](./media/Assemble_Mecanum_Robot_3fec7c19.png)

### Schritt 3

**Benötigte Komponenten:**

![](./media/Assemble_Mecanum_Robot_d4f24cc5.png)

**Installationsdiagramm:**

![](./media/Assemble_Mecanum_Robot_e1d7b425.png)

**Prototyp:**

![](./media/Assemble_Mecanum_Robot_cc96b9d6.png)

### Schritt 4

（stellen Sie zuerst den Winkel des Servos ein）

**Stellen Sie den Winkel des Servos auf 90 Grad ein.**

**Methode 1: MakeCode-Code**

⚠️**Besondere Anmerkung:** Bevor Sie den Code schreiben und hochladen, müssen Sie die MakeCode-IDE verstehen und Bibliotheksdateien hinzufügen. Bitte gehen Sie zu folgendem Link: [Get Started with makecode](./Code1.7z)

![](./media/Assemble_Mecanum_Robot_a9ff633c.png)

Der obige MakeCode-Code liegt im Material bei. Öffnen Sie den Einstellungs-Code für den Servo und schreiben Sie ihn auf das microbit-Motherboard des 4WD Mecanum Robot Car V2.0, und **schalten Sie die Stromversorgung über ein micro-USB-Kabel oder eine externe Stromversorgung ein (drehen Sie den DIP switch auf ON)**. Das war's. Der Code befindet sich an der im Bild gezeigten Position:

![Img](./media/Assemble_Mecanum_Robot_21db9fa2.png)

**Methode 2：Python-Code**

⚠️**Besondere Anmerkung:** Bevor Sie den Code schreiben und hochladen, müssen Sie die Mu IDE installieren und Bibliotheksdateien hinzufügen. Bitte gehen Sie zu folgendem Link: [Get Started with Python](./Code2.7z)

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

**Benötigte Komponenten:**

![](./media/Assemble_Mecanum_Robot_1e3fd9e2.png)

Installationsdiagramm: (achten Sie auf die Einbaurichtung)

![](./media/Assemble_Mecanum_Robot_9ca5d2c8.png)

**Prototyp:**

![](./media/Assemble_Mecanum_Robot_9b8bccaa.png)

### Schritt 5

**Benötigte Komponenten:**

![](./media/Assemble_Mecanum_Robot_8d138501.png)

**Installationsdiagramm:**

![](./media/Assemble_Mecanum_Robot_bda8fbc4.png)

**Prototyp:**

![](./media/Assemble_Mecanum_Robot_9f244272.png)

### Schritt 6

**Benötigte Komponenten:**

![](./media/Assemble_Mecanum_Robot_36259594.png)

**Installationsdiagramm:**

![](./media/Assemble_Mecanum_Robot_6d3e3ad9.png)

**Prototyp:**

![](./media/Assemble_Mecanum_Robot_3c33f63b.png)

### Schritt 7

**Benötigte Komponenten:**

![](./media/Assemble_Mecanum_Robot_817e834e.png)

**Installationsdiagramm:** (achten Sie auf die Richtung des Motors)

![](./media/Assemble_Mecanum_Robot_09a61aa6.png)

**Prototyp:**

![](./media/Assemble_Mecanum_Robot_8c97de28.png)

### Schritt 8

**Benötigte Komponenten:**

![](./media/Assemble_Mecanum_Robot_43bac346.png)

**Installationsdiagramm:** (achten Sie auf die Einbaurichtung des Mecanum-Rads)

![](./media/Assemble_Mecanum_Robot_d92dee68.png)

**Prototyp:**

![](./media/Assemble_Mecanum_Robot_64467ed0.png)

### Schritt 9

**Benötigte Komponenten:**

![](./media/Assemble_Mecanum_Robot_5c38573f.png)

**Installationsdiagramm:**

![](./media/Assemble_Mecanum_Robot_a72469e3.png)

**Prototyp:**

![](./media/Assemble_Mecanum_Robot_243aa35b.png)

### Schritt 10

**Benötigte Komponenten:**

![](./media/Assemble_Mecanum_Robot_b60b9f16.png)

**Installationsdiagramm:**

![](./media/Assemble_Mecanum_Robot_55f2db60.png)

**Prototyp:**

![](./media/Assemble_Mecanum_Robot_456df8a0.png)

### Schaltplan

**Die Verkabelung des Servos:**

![Img](./media/Assemble_Mecanum_Robot_c82a9395.png)

![](./media/Assemble_Mecanum_Robot_859cd41e.jpg)

![](./media/Assemble_Mecanum_Robot_b3bcce9d.png)

**Die Verkabelung des Ultraschallsensors:**

![Img](./media/Assemble_Mecanum_Robot_c9f3da75.png)

![](./media/Assemble_Mecanum_Robot_5747ad7c.jpg)

![](./media/Assemble_Mecanum_Robot_a8f0e176.png)

**Die Verkabelung des IR-Empfängermoduls:**

![Img](./media/Assemble_Mecanum_Robot_61d53b21.png)

![](./media/Assemble_Mecanum_Robot_1e081a3a.png)

**Die Verkabelung der RGB-LED:**

![Img](./media/Assemble_Mecanum_Robot_c5b8a804.png)

![](./media/Assemble_Mecanum_Robot_01848b2e.jpg)

**Die Verkabelung zur Steuerung des Motors und der Sieben-Farben-Leuchte:**

![Img](./media/Assemble_Mecanum_Robot_0c4635c5.png)

![](./media/Assemble_Mecanum_Robot_1689f2c9.jpg)

**Die Verkabelung zur Steuerung des 3-Kanal Linienverfolgungssensors:**

![Img](./media/Assemble_Mecanum_Robot_542d1798.png)

![](./media/Assemble_Mecanum_Robot_08eb8d7e.jpg)

**Die Verkabelung der Stromversorgung:**

![](./media/Assemble_Mecanum_Robot_cdcec4ba.jpg)

**Die entsprechende Motor-Schnittstelle:**

![](./media/Assemble_Mecanum_Robot_ffcceef1.jpg)

**Die Installation der Batterie:**

![](./media/Assemble_Mecanum_Robot_fe8ce786.png)