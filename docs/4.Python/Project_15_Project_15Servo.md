### Projet 15：Servo

![](./media/Python_c4b5e57b.png)

1\.  **Description**

Les voitures intelligentes DIY intègrent généralement une fonction d'évitement automatique des obstacles. Lors du montage, nous avons besoin d'un servomoteur pour faire pivoter le module ultrasonique à gauche et à droite, puis détecter la distance entre la voiture et l'obstacle afin de contrôler la voiture pour éviter l'obstacle.

Si d'autres microcontrôleurs sont utilisés pour contrôler la rotation du servo, il faut définir une certaine fréquence et largeur d'impulsion pour contrôler l'angle du servo. Mais si la carte principale micro:bit est utilisée pour contrôler l'angle du servo, il suffit de définir l'angle de commande dans l'environnement de développement : l'impulsion correspondante sera automatiquement générée pour piloter la rotation du servo. Dans ce projet, vous apprendrez à faire osciller le servo entre 0° et 90°.

Le servomoteur est un actionneur rotatif à contrôle de position, composé principalement du boîtier, de la carte électronique, du moteur sans noyau, des engrenages et d'un capteur de position. Son principe de fonctionnement est que le servo reçoit le signal envoyé par le MCU ou le récepteur, génère un signal de référence avec une période de 20 ms et une largeur de 1,5 ms, puis compare la tension continue obtenue à la tension du potentiomètre et en déduit la différence de tension en sortie.

Pour le servo utilisé dans ce projet, le fil marron est la masse, le fil rouge est le + et le fil orange est le fil de signal.

![](./media/Python_69be9581.png)

2\.  **Informations sur le Servo**

L'angle de rotation du servomoteur est contrôlé en régulant le rapport cyclique du signal PWM (modulation de largeur d'impulsion). Le cycle standard du signal PWM est de 20 ms (50 Hz). Théoriquement, la largeur se situe entre 1 ms et 2 ms, mais en pratique elle varie entre 0,5 ms et 2,5 ms. La largeur correspond à l'angle de rotation de 0° à 180°. Notez toutefois que pour des marques différentes, le même signal peut entraîner des angles de rotation différents.

![](./media/Python_0982cb7b.png)

Après mesure, la plage d'impulsion du servo est de 0,65 ms à 2,5 ms. Pour un servo de 180 degrés, la relation de commande correspondante est la suivante :


|Time on High Level|Angle of the Servo|Reference Signal Cycle Time（20ms）|
|-|-|-|
|0.65ms|0 degree|0.65ms high level+19.35ms low level|
|1.5ms|90 degrees|1.5ms high level+18.5ms low level|
|2.5ms|180degrees|2.5ms high level+17.5ms low level|


3\.  **Paramètres**

- Tension de fonctionnement : DC 4.8V ~ 6V

- Plage d'angle de fonctionnement : environ 180 ° (à 500 → 2500 μsec)

- Dimensions : 22.9\*12.2\*30mm

- Plage de largeur d'impulsion : 500 → 2500 μsec

- Vitesse à vide : 0.12 ± 0.01 s / 60 (DC 4.8V), 0.1 ± 0.01 s / 60 (DC 6V)

- Courant à vide : 200 ± 20mA (DC 4.8V), 220 ± 20mA (DC 6V)

- Couple d'arrêt : 1.3 ± 0.01kg · cm (DC 4.8V), 1.5 ± 0.1kg · cm (DC 6V)

- Courant au blocage : ≦ 850mA (DC 4.8V) ≦ 1000mA (DC 6V)

- Courant de repos : 3 ± 1mA (DC 4.8V), 4 ± 1mA (DC 6V)

- Poids : 9±1g (sans bras de servo)

- Température de fonctionnement : -30℃~60℃

**Il convient de noter de ne pas utiliser l'alimentation d'un ordinateur, car si la demande en courant dépasse 500 mA, le servo peut être endommagé. Il est recommandé d'utiliser une batterie externe pour l'alimentation.**

4\.  **Préparation**

- Insérez la carte micro:bit dans la fente du keyestudio 4WD Mecanum Robot Car V2.0

- Placez les piles dans le porte-piles

- Passez l'interrupteur d'alimentation sur la position ON

- Connectez le micro:bit à l'ordinateur via un câble USB

- Ouvrez la version hors ligne de Mu.

5\.  **Code de test**

Lancez le logiciel Mu et ouvrez le fichier “Servo\.py” pour importer le code. Vous pouvez également saisir le code vous-même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles en anglais doivent être écrits en anglais**.)

Cliquez sur “Check” pour vérifier les erreurs dans le code. Le programme est erroné si des soulignements ou des curseurs sont affichés.

Si le code est correct, connectez le micro:bit à votre ordinateur et cliquez sur “Flash” pour téléverser le code sur la carte micro:bit.

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

4\.  **Résultat du test**

Après avoir téléchargé le code sur la carte avec succès, **alimentez en externe (mettre le DIP switch sur ON)**, puis appuyez sur le bouton de réinitialisation du micro:bit.

![Img](./media/Python_bb3e1312.png)

La matrice de LED affiche un smiley et le servo tourne selon le motif 0°~45°~90°~135°~180°~0°.

---