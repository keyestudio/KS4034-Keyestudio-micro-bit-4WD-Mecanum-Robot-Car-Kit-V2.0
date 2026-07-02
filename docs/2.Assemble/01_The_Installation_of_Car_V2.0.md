## L'installation du Keyestudio 4WD Mecanum Robot Car V2.0

### Étape 1

**Composants nécessaires :**

![](./media/Assemble_Mecanum_Robot_f3d856b4.png)

**Schéma d'installation :**

![](./media/Assemble_Mecanum_Robot_3d1dbf07.png)

**Prototype :**

![](./media/Assemble_Mecanum_Robot_f5d38786.png)

### Étape 2

**Composants nécessaires :**

![](./media/Assemble_Mecanum_Robot_a2ee8074.png)

**Schéma d'installation :**

![](./media/Assemble_Mecanum_Robot_6fdf9d4d.png)

**Prototype :**

![](./media/Assemble_Mecanum_Robot_3fec7c19.png)

### Étape 3

**Composants nécessaires :**

![](./media/Assemble_Mecanum_Robot_d4f24cc5.png)

**Schéma d'installation :**

![](./media/Assemble_Mecanum_Robot_e1d7b425.png)

**Prototype :**

![](./media/Assemble_Mecanum_Robot_cc96b9d6.png)

### Étape 4

（réglez d'abord l'angle du servo）

**Réglez l'angle du servo à 90 degrés.**

**Méthode 1 : code MakeCode**

⚠️**Remarque spéciale :** Avant d'écrire le code et de le téléverser, vous devez connaître l'IDE MakeCode et ajouter les fichiers de la bibliothèque. Veuillez accéder au lien suivant : [Get Started with makecode](./Code1.7z)

![](./media/Assemble_Mecanum_Robot_a9ff633c.png)

Le code MakeCode ci-dessus est fourni dans les matériaux. Ouvrez le code d'ajustement du servo et téléversez-le sur le microbit de la 4WD Mecanum Robot Car V2.0, puis **alimentez via un câble micro USB ou une alimentation externe (passez le DIP switch sur ON)**. C'est tout. Le code se trouve à l'emplacement indiqué sur l'image :

![Img](./media/Assemble_Mecanum_Robot_21db9fa2.png)

**Méthode 2：code Python**

⚠️**Remarque spéciale :** Avant d'écrire le code et de le téléverser, vous devez installer Mu IDE et ajouter les fichiers de la bibliothèque. Veuillez accéder au lien suivant : [Get Started with Python](./Code2.7z)

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

**Composants nécessaires :**

![](./media/Assemble_Mecanum_Robot_1e3fd9e2.png)

Schéma d'installation : (faites attention au sens d'installation)

![](./media/Assemble_Mecanum_Robot_9ca5d2c8.png)

**Prototype :**

![](./media/Assemble_Mecanum_Robot_9b8bccaa.png)

### Étape 5

**Composants nécessaires :**

![](./media/Assemble_Mecanum_Robot_8d138501.png)

**Schéma d'installation :**

![](./media/Assemble_Mecanum_Robot_bda8fbc4.png)

**Prototype :**

![](./media/Assemble_Mecanum_Robot_9f244272.png)

### Étape 6

**Composants nécessaires :**

![](./media/Assemble_Mecanum_Robot_36259594.png)

**Schéma d'installation :**

![](./media/Assemble_Mecanum_Robot_6d3e3ad9.png)

**Prototype :**

![](./media/Assemble_Mecanum_Robot_3c33f63b.png)

### Étape 7

**Composants nécessaires :**

![](./media/Assemble_Mecanum_Robot_817e834e.png)

**Schéma d'installation :** (faites attention au sens du moteur)

![](./media/Assemble_Mecanum_Robot_09a61aa6.png)

**Prototype :**

![](./media/Assemble_Mecanum_Robot_8c97de28.png)

### Étape 8

**Composants nécessaires :**

![](./media/Assemble_Mecanum_Robot_43bac346.png)

**Schéma d'installation :** (faites attention au sens d'installation de la roue mecanum)

![](./media/Assemble_Mecanum_Robot_d92dee68.png)

**Prototype :**

![](./media/Assemble_Mecanum_Robot_64467ed0.png)

### Étape 9

**Composants nécessaires :**

![](./media/Assemble_Mecanum_Robot_5c38573f.png)

**Schéma d'installation :**

![](./media/Assemble_Mecanum_Robot_a72469e3.png)

**Prototype :**

![](./media/Assemble_Mecanum_Robot_243aa35b.png)

### Étape 10

**Composants nécessaires :**

![](./media/Assemble_Mecanum_Robot_b60b9f16.png)

**Schéma d'installation :**

![](./media/Assemble_Mecanum_Robot_55f2db60.png)

**Prototype :**

![](./media/Assemble_Mecanum_Robot_456df8a0.png)

### Schéma de câblage

**Le câblage du servo :**

![Img](./media/Assemble_Mecanum_Robot_c82a9395.png)

![](./media/Assemble_Mecanum_Robot_859cd41e.jpg)

![](./media/Assemble_Mecanum_Robot_b3bcce9d.png)

**Le câblage du capteur ultrasonique :**

![Img](./media/Assemble_Mecanum_Robot_c9f3da75.png)

![](./media/Assemble_Mecanum_Robot_5747ad7c.jpg)

![](./media/Assemble_Mecanum_Robot_a8f0e176.png)

**Le câblage du module récepteur IR :**

![Img](./media/Assemble_Mecanum_Robot_61d53b21.png)

![](./media/Assemble_Mecanum_Robot_1e081a3a.png)

**Le câblage du RGB :**

![Img](./media/Assemble_Mecanum_Robot_c5b8a804.png)

![](./media/Assemble_Mecanum_Robot_01848b2e.jpg)

**Le câblage pour contrôler le moteur et la lumière sept-couleurs :**

![Img](./media/Assemble_Mecanum_Robot_0c4635c5.png)

![](./media/Assemble_Mecanum_Robot_1689f2c9.jpg)

**Le câblage pour contrôler le capteur de suivi de ligne 3 canaux :**

![Img](./media/Assemble_Mecanum_Robot_542d1798.png)

![](./media/Assemble_Mecanum_Robot_08eb8d7e.jpg)

**Le câblage de l'alimentation :**

![](./media/Assemble_Mecanum_Robot_cdcec4ba.jpg)

**L'interface correspondante du moteur :**

![](./media/Assemble_Mecanum_Robot_ffcceef1.jpg)

**L'installation de la batterie :**

![](./media/Assemble_Mecanum_Robot_fe8ce786.png)