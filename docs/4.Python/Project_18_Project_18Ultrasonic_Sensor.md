### Projet 18：Capteur ultrasonique

#### Projet 18.1：Mesure de distance ultrasonique

1\. **Description**

![](./media/Python_9810ae67.jpg)

Le capteur ultrasonique utilise le sonar pour déterminer la distance à un objet, comme le font les chauves-souris. Il offre une excellente détection de distance sans contact avec une grande précision et des mesures stables, dans un boîtier facile d'utilisation. Il est fourni avec les modules émetteur et récepteur ultrasoniques.

Le capteur ultrasonique est utilisé dans un large éventail de projets électroniques pour créer des applications de détection d'obstacles et de mesure de distance ainsi que diverses autres applications.

![](./media/Python_0180b169.png)

Le module ultrasonique émettra des ondes ultrasoniques après le signal de déclenchement. Lorsque les ondes ultrasoniques rencontrent un objet et sont réfléchies, le module sort un signal d'écho ; il peut ainsi déterminer la distance de l'objet à partir du temps écoulé entre le signal de déclenchement (TRIG) et le signal d'écho (ECHO).

Comme le montre l'image, il ressemble à deux yeux. L'un est l'émetteur, l'autre est le récepteur.

Selon le schéma de câblage ci‑dessus, le port intégré du module capteur ultrasonique est connecté au port 5V G P15 P16 sur la carte de commande de moteur micro:bit. La broche Trig (T) est contrôlée par P15 du micro:bit et la broche Echo (E) par P16.

![](./media/Python_19b45a23.jpg)

2\. **Principe de fonctionnement**

![](./media/Python_8ff02741.png)

(1) Mettre TRIG à l'état bas puis envoyer un signal de déclenchement d'au moins 10us en niveau haut ;

(2) Après le déclenchement, le module enverra automatiquement huit impulsions ultrasoniques à 40 kHz et détectera s'il y a un retour de signal ;

(3) S'il y a un retour de signal, lorsque ECHO (E) passe au niveau haut, la durée de ce niveau haut correspond au temps aller‑retour des ondes ultrasoniques. Ensuite distance mesurée = durée du niveau haut * 340 m/s * 0,5.

3\.  **Paramètres**

- Tension de fonctionnement : 3‑5,5V (DC)
- Courant de fonctionnement : 15 mA
- Fréquence de fonctionnement : 40 kHz
- Distance maximum de détection : environ 3 m
- Distance minimum de détection : 2‑3 cm
- Précision : jusqu'à 0,2 cm
- Angle de détection : inférieur à 15 degrés
- Impulsion d'entrée de déclenchement : 10 µs niveau TTL
- Signal d'écho de sortie : sortie signal niveau TTL (haut), proportionnel à la portée

4\.  **Préparation**

- Insérer la carte micro:bit dans le logement du keyestudio 4WD Mecanum Robot Car V2.0
- Placer les batteries dans le porte‑pile
- Mettre l'interrupteur d'alimentation sur ON
- Connecter le micro:bit à l'ordinateur via un câble USB
- Ouvrir la version hors ligne de Mu

5\.  **Code de test**

Ouvrir Mu et ouvrir le fichier “Ultrasonic Ranging\.py” pour importer le code. Vous pouvez aussi saisir le code directement dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles en anglais doivent être écrits en anglais**.)

Cliquer sur “Files” pour importer le fichier de bibliothèque “keyes_mecanum_Car_V2.py” vers le micro:bit.

Cliquer sur “Check” pour vérifier les erreurs dans le code. Le programme est erroné si des soulignements et des curseurs sont affichés.

Si le code est correct, connecter le micro:bit à votre ordinateur et cliquer sur “Flash” pour télécharger le code sur la carte micro:bit.

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

6\.  **Résultat du test**

Après avoir téléchargé le code sur la carte avec succès et sans débrancher le câble USB, cliquer sur “REPL” puis appuyer sur le bouton reset.

![Img](./media/Python_bb3e1312.png)

La valeur de distance de l'obstacle sera affichée, comme indiqué ci‑dessous.

Quand la distance est inférieure à 10 cm, le buzzer passif de la voiture émettra un son.

![](./media/Python_4dc8054e.png)

7\.  **Explication du code**

![Img](./media/Python_ebde06e9.png)

#### Projet 18.2：Évitement ultrasonique

![](./media/Python_aee41f6f.jpg)

1\. **Description**

Dans ce projet, nous allons intégrer un capteur ultrasonique à une voiture pour réaliser une voiture d'évitement ultrasonique.

Le principe est de détecter la distance entre la voiture et l'obstacle via le capteur ultrasonique afin de contrôler le mouvement de la voiture.

2\. **Préparation**

- Insérer la carte micro:bit dans le logement du keyestudio 4WD Mecanum Robot Car V2.0
- Placer les batteries dans le porte‑pile
- Mettre l'interrupteur d'alimentation sur ON
- Connecter le micro:bit à l'ordinateur via un câble USB
- Ouvrir la version hors ligne de Mu

3\.  **Diagramme de flux**

![Img](./media/Python_a4efee72.png)

4\.  **Code de test**

Ouvrir Mu et ouvrir le fichier “Ultrasonic Avoid Smart Car\.py” pour importer le code. Vous pouvez aussi saisir le code directement dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles en anglais doivent être écrits en anglais**.)

Cliquer sur “Files” pour importer le fichier de bibliothèque “keyes_mecanum_Car_V2.py” vers le micro:bit.

Cliquer sur “Check” pour vérifier les erreurs dans le code. Le programme est erroné si des soulignements et des curseurs sont affichés.

Si le code est correct, connecter le micro:bit à votre ordinateur et cliquer sur “Flash” pour télécharger le code sur la carte micro:bit.

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

5\.  **Résultat du test**

Après avoir téléchargé le code sur la carte avec succès, **alimentation externe (mettre l'interrupteur DIP sur ON)**, et appuyer sur le bouton reset du micro:bit.

![Img](./media/Python_bb3e1312.png)

Lorsque la distance de l'obstacle est supérieure à 20 cm, la voiture avance ; dans le cas contraire, la voiture tourne à gauche.

6\.  **Explication du code**

![Img](./media/Python_9e28cce7.png)

![Img](./media/Python_c33a22a8.png)

#### Projet 18.3：Suiveur ultrasonique

![](./media/Python_28806167.jpg)

1\. **Description**

Dans la leçon précédente, nous avons appris le principe de base du capteur de suivi de ligne. Ensuite, nous allons combiner le capteur ultrasonique avec la voiture pour réaliser une voiture suiveuse ultrasonique.

Le capteur ultrasonique détecte la distance de l'obstacle et contrôle l'état de mouvement de la voiture.

2\. **Préparation**

- Insérer la carte micro:bit dans le logement du keyestudio 4WD Mecanum Robot Car V2.0
- Placer les batteries dans le porte‑pile
- Mettre l'interrupteur d'alimentation sur ON
- Connecter le micro:bit à l'ordinateur via un câble USB
- Ouvrir la version hors ligne de Mu

2\.  **Diagramme de flux**

![Img](./media/Python_53a30906.png)

3\.  **Code de test**

Ouvrir Mu et ouvrir le fichier “Ultrasonic Follow Smart Car\.py” pour importer le code. Vous pouvez aussi saisir le code directement dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles en anglais doivent être écrits en anglais**.)

Cliquer sur “Files” pour importer le fichier de bibliothèque “keyes_mecanum_Car_V2.py” vers le micro:bit.

Cliquer sur “Check” pour vérifier les erreurs dans le code. Le programme est erroné si des soulignements et des curseurs sont affichés.

Si le code est correct, connecter le micro:bit à votre ordinateur et cliquer sur “Flash” pour télécharger le code sur la carte micro:bit.

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

4\.  **Résultat du test**

Après avoir téléchargé le code sur la carte avec succès, **alimentation externe (mettre l'interrupteur DIP sur ON)**, et appuyer sur le bouton reset du micro:bit.

![Img](./media/Python_bb3e1312.png)

La voiture pourra suivre l'obstacle en mouvement et les 4 LED RGB WS2812 afficheront différentes couleurs.

**Remarque :** l'obstacle ne peut se déplacer que devant la voiture.

5\.  **Explication du code**

![Img](./media/Python_930a04fa.png)

![Img](./media/Python_26371a4d.png)