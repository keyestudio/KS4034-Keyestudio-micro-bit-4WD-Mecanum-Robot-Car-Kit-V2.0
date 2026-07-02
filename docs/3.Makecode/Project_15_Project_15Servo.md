## Projet 15：Servo

![](./media/Makecode_215da878.png)

1\.  **Description**

Pour les voitures intelligentes DIY, il y a souvent une fonction d'évitement automatique des obstacles. Dans le processus DIY, nous devons utiliser un servomoteur pour faire tourner le module ultrasonique à gauche et à droite, puis détecter la distance entre la voiture et l'obstacle afin de contrôler la voiture pour éviter l'obstacle. Si d'autres microcontrôleurs sont utilisés pour contrôler la rotation du servo, il faut régler une certaine fréquence et une certaine largeur d'impulsion pour contrôler l'angle du servo.

Cependant, si la carte principale micro:bit est utilisée pour contrôler l'angle du servo, il suffit de définir l'angle de contrôle dans l'environnement de développement ; l'impulsion correspondante sera automatiquement générée pour contrôler la rotation du servo. Dans ce projet, vous apprendrez à contrôler le servo pour qu'il oscille entre 0° et 90°.

2\.  **Informations sur le servo**

Un servomoteur est un actionneur rotatif de contrôle de position. Il se compose principalement d'un boîtier, d'une carte électronique, d'un moteur sans noyau, d'engrenages et d'un capteur de position. Son principe de fonctionnement est que le servo reçoit le signal envoyé par le MCU ou le récepteur, produit un signal de référence avec une période de 20 ms et une largeur de 1,5 ms, puis compare la tension de décalage continue acquise à la tension du potentiomètre et obtient la différence de tension en sortie.

![](./media/Makecode_87b41036.png)

Pour le servo utilisé dans ce projet, le fil marron est la masse, le fil rouge est l'alimentation positive et le fil orange est le fil de signal.

L'angle de rotation du servomoteur est contrôlé en régulant le rapport cyclique du signal PWM (Pulse-Width Modulation). Le cycle standard du signal PWM est de 20 ms (50 Hz). Théoriquement, la largeur est répartie entre 1 ms et 2 ms, mais en pratique elle se situe entre 0,5 ms et 2,5 ms. La largeur correspond à l'angle de rotation de 0° à 180°. Notez cependant que pour des moteurs de marques différentes, le même signal peut produire des angles de rotation différents.

![](./media/Makecode_49467dfa.png)

Plus de détails :

![](./media/Makecode_b167d550.png)

3\.  **Paramètres**

- Tension de fonctionnement : DC 4.8V ~ 6V

- Plage d'angle de fonctionnement : environ 180 ° (à 500 → 2500 μsec)

- Plage de largeur d'impulsion : 500 → 2500 μsec

- Vitesse à vide : 0.12 ± 0.01 s / 60 (DC 4.8V) 0.1 ± 0.01 s / 60 (DC 6V)

- Courant à vide : 200 ± 20mA (DC 4.8V) 220 ± 20mA (DC 6V)

- Couple de maintien : 1.3 ± 0.01kg·cm (DC 4.8V) 1.5 ± 0.1kg·cm (DC 6V)

- Courant d'arrêt : ≦ 850mA (DC 4.8V) ≦ 1000mA (DC 6V)

- Courant de veille : 3 ± 1mA (DC 4.8V) 4 ± 1mA (DC 6V)

4\.  **Préparation**

- Insérez la carte micro:bit dans l'emplacement du keyestudio   4WD Mecanum Robot Car V2.0

- Placez les piles dans le porte-piles

- Positionnez l'interrupteur d'alimentation sur ON

- Connectez la micro:bit à votre ordinateur via un câble USB

- Ouvrez la version Web de Makecode


5\.  **Code de test**

![](./media/Makecode_087e1822.png)

Cliquez sur "JavaScript" pour voir le code JavaScript correspondant :

![](./media/Makecode_2354311f.png)

6.  **Résultat du test**

Après avoir téléversé le code de test et positionné l'interrupteur POWER sur ON, le servo tourne de 0 degré à 180 degrés.