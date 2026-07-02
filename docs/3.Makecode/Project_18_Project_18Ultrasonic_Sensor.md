## Projet 18：Capteur à ultrasons

### Projet 18.1：Mesure de distance par ultrasons

1\.  **Description**

Le capteur à ultrasons utilise le sonar pour mesurer la distance d’un objet, comme le font les chauves-souris. Il offre une excellente détection de distance sans contact, avec une grande précision et des lectures stables, dans un ensemble facile à utiliser. Il comprend un module émetteur et un module récepteur ultrasoniques.

Le capteur à ultrasons est utilisé dans un large éventail de projets électroniques pour la détection d’obstacles, la mesure de distance et diverses autres applications.

![](./media/Makecode_0180b169.png)

Le module ultrasonique émettra des ondes ultrasonores après les signaux de déclenchement. Lorsque les ondes ultrasonores rencontrent un objet et sont réfléchies, le module émet un signal d’écho, ce qui permet de déterminer la distance de l’objet à partir de la différence de temps entre le signal de déclenchement (TRIG) et le signal d’écho (ECHO).

Comme le montre l’image, il ressemble à deux yeux. L’un est l’émetteur, l’autre le récepteur.

Selon le schéma de câblage ci-dessus, la prise intégrée du module de capteur ultrasonique est connectée au port 5V G P15 P16 sur la carte de commande moteur micro:bit. Le broche Trig (T) est commandée par P15 du micro:bit et la broche Echo (E) par P16.

![](./media/Makecode_1174e0ec.png)

2\. **Principe de fonctionnement**

![](./media/Makecode_8ff02741.png)

(1) Tirez TRIG à bas niveau puis déclenchez un signal haut d’au moins 10 µs ;

(2) Après le déclenchement, le module enverra automatiquement huit impulsions ultrasonores à 40 kHz et détectera s’il y a un retour de signal ;

(3) S’il y a un retour de signal, lorsque ECHO (E) passe à l’état haut, la durée de l’état haut correspond au temps entre l’émission et la réception des ondes ultrasonores. Ensuite distance de test = durée de l’état haut \*340m/s\*0.5. 

3\. **Paramètres**

- Tension de fonctionnement : 3-5.5V (DC)

- Courant de fonctionnement : 15mA

- Fréquence de fonctionnement : 40 kHz

- Distance maximale de détection : environ 3 m

- Distance minimale de détection : 2-3 cm

- Précision : jusqu’à 0,2 cm

- Angle de détection : inférieur à 15 degrés

- Impulsion d’entrée de déclenchement : 10 µs niveau TTL

- Signal d’écho en sortie : signal de niveau TTL (haut), proportionnel à la distance

4\. **Préparation**

- Insérez la carte micro:bit dans la fente du keyestudio 4WD Mecanum Robot Car V2.0

- Placez les piles dans le porte-piles

- Positionnez l’interrupteur d’alimentation sur ON

- Connectez le micro:bit à votre ordinateur via un câble USB

- Ouvrez la version Web de Makecode


5\. **Code de test**

![](./media/Makecode_497760b1.png)

Cliquez sur “JavaScript” pour afficher le code JavaScript correspondant : 

![](./media/Makecode_387f3243.png)

6\.  **Résultat du test**

Téléversez le code sur le micro:bit, laissez le câble USB connecté et positionnez l’interrupteur POWER sur ON. La valeur de distance s’affichera sur le moniteur.

![](./media/Makecode_2cd74c16.png)

Le moniteur affiche la distance entre l’obstacle et le capteur ultrasonique (comme ci-dessous).

![](./media/Makecode_422adea3.png)

Ouvrez CoolTerm, cliquez sur Options pour sélectionner SerialPort. Réglez le port COM et le débit sur 115200 bauds (le débit de communication série USB du Micro:bit est de 115200 lors du test). Cliquez sur “OK” puis “Connect”.

Le moniteur série CoolTerm affiche la valeur de distance comme suit :

![](./media/Makecode_69b06998.png)

### Projet 18.2：Évitement par ultrasons

![Img](./media/Makecode_13139b46.png)

1\. **Description**

Dans ce projet, nous allons intégrer un capteur à ultrasons et une voiture pour réaliser une voiture d’évitement ultrasonique.

Le principe consiste à détecter la distance entre la voiture et l’obstacle via le capteur à ultrasons afin de contrôler le mouvement de la voiture intelligente.

2\.  **Préparation**

- Insérez la carte micro:bit dans la fente du keyestudio 4WD Mecanum Robot Car V2.0

- Placez les piles dans le porte-piles

- Positionnez l’interrupteur d’alimentation sur ON

- Connectez le micro:bit à votre ordinateur via un câble USB

- Ouvrez la version Web de Makecode

3\.  **Organigramme**

![Img](./media/Makecode_e2adae4b.png)

4\.  **Code de test**

![](./media/Makecode_05a4740b.png)

![Img](./media/Makecode_d7879887.png)

Cliquez sur “JavaScript” pour afficher le code JavaScript correspondant : 

![](./media/Makecode_c8f86a24.png)

![](./media/Makecode_13baf1d6.png)

5\.  **Résultat du test**

Téléversez le code sur le micro:bit, mettez-le sous tension et positionnez l’interrupteur POWER sur ON. Lorsque la distance à l’obstacle est supérieure à 20 cm, la voiture avance ; sinon, la voiture intelligente tourne à gauche.

### Projet 18.3：Suivi par ultrasons

![Img](./media/Makecode_d17a7889.png)

1\. **Description**

Dans la leçon précédente, nous avons appris le principe de base du capteur de suivi de ligne. Ensuite, nous allons combiner le capteur à ultrasons avec la voiture pour réaliser une voiture suiveuse ultrasonique.

Le capteur à ultrasons détecte la distance de l’obstacle et contrôle l’état de mouvement de la voiture.

2\. **Préparation**

- Insérez la carte micro:bit dans la fente du keyestudio 4WD Mecanum Robot Car V2.0

- Placez les piles dans le porte-piles

- Positionnez l’interrupteur d’alimentation sur ON

- Connectez le micro:bit à votre ordinateur via un câble USB

- Ouvrez la version Web de Makecode

3\. **Organigramme**

![Img](./media/Makecode_f5026aed.png)

4\. **Code de test**

![](./media/Makecode_03b95531.png)

Cliquez sur “JavaScript” pour afficher le code JavaScript correspondant : 

![](./media/Makecode_a93c8245.png)

5\. **Résultat du test**

Téléversez le code sur le micro:bit, mettez l’interrupteur POWER sur ON sur le shield, la voiture intelligente pourra suivre l’obstacle et se déplacer.