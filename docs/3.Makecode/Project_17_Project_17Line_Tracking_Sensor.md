## Projet 17：Line Tracking Sensor

### Projet 17.1：Detect Line Tracking Sensor

![](./media/Makecode_ea7f6c8c.png)

1\. **Description**

La carte pilote du Keyestudio 4WD Mecanum Robot Car est fournie avec un capteur de suivi de ligne 3 canaux, qui utilise des modules IR TCRT5000 et 3 potentiomètres.

Le module IR TCRT5000 contient un émetteur IR et un récepteur IR. Lorsque les signaux infrarouges de l’émetteur sont reçus par le récepteur après réflexion, la résistance du récepteur change, ce qui se traduit généralement par une variation de tension dans le circuit.  

La résistance varie en fonction de l’intensité des signaux infrarouges reçus par le récepteur, ce qui dépend souvent de la couleur de la surface réfléchissante et de la distance entre la surface réfléchissante et le récepteur. Lors de la détection, le noir correspond à un niveau haut actif et le blanc à un niveau bas actif. 

2\.  **Working Principle**

Lorsque la voiture roule au-dessus d’une route blanche, la diode IR installée sous la voiture émet des signaux infrarouges pour détecter la route et la diode réceptrice reçoit et renvoie les signaux. Ensuite la sortie fournit un niveau bas (0) ; lorsqu’elle détecte des lignes noires, elle fournit un niveau haut (1).

Après avoir placé une feuille blanche sous le 4WD Mecanum Robot Car, nous tournerons les potentiomètres du capteur de suivi 3 voies. Lorsque la LED d’indication du module capteur s’allume, soulevez la voiture de façon à ce que les deux roues du 4WD Mecanum Robot Car puissent tourner librement. La hauteur entre le papier blanc et le capteur est d’environ 1,5 cm ; lorsque la LED du module capteur s’éteint, la sensibilité est correctement réglée.

3\.  **Preparation**

- Insérez la carte micro:bit dans la fente du keyestudio 4WD Mecanum Robot Car V2.0

- Placez des piles dans le porte-piles

- Positionnez l’interrupteur d’alimentation sur ON

- Connectez le micro:bit à votre ordinateur via un câble USB

- Ouvrez la version Web de Makecode

4\.  **Test Code**

![](./media/Makecode_3683d83f.png)

Cliquez sur “JavaScript” pour voir le code JavaScript correspondant : 

![](./media/Makecode_4b440616.png)

5\.  **Test Result**

Téléversez le code sur la carte micro:bit, positionnez l’interrupteur POWER sur ON. 

Ouvrez CoolTerm, cliquez sur Options et sélectionnez SerialPort. Définissez le port COM et le débit sur 115200. Cliquez sur “OK” puis “Connect”.

![](./media/Makecode_ea164439.png)

![](./media/Makecode_b3a18bca.png)

![](./media/Makecode_f78128c1.png)

![](./media/Makecode_13238e98.png)

Le moniteur série CoolTerm affiche les signaux numériques lus par les capteurs de suivi de ligne.

![](./media/Makecode_0141051a.png)

### Projet 17.2：Tracking Smart Car

![Img](./media/Makecode_547634e4.png)

1\. **Description**

Dans cette leçon, nous combinerons un capteur de suivi de ligne avec un moteur pour réaliser une voiture intelligente de suivi de ligne.

La carte micro:bit analysera les signaux et contrôlera la voiture intelligente pour démontrer la fonction de suivi de ligne.

2\. **Working Principle**

La voiture intelligente effectuera différents mouvements en fonction des valeurs reçues par le capteur de suivi de ligne 3 canaux.

![Img](./media/Makecode_bbccdb34.png)

3\. **Preparation**

- Insérez la carte micro:bit dans la fente du keyestudio 4WD Mecanum Robot Car V2.0

- Placez des piles dans le porte-piles

- Positionnez l’interrupteur d’alimentation sur ON

- Connectez le micro:bit à votre ordinateur via un câble USB

- Ouvrez la version Web de Makecode

**Warning:** Le capteur de suivi 3 voies doit être utilisé dans des environnements sans interférence infrarouge tels que la lumière directe du soleil. La lumière du soleil contient beaucoup de lumière invisible, comme l’infrarouge et l’ultraviolet. Dans un environnement très ensoleillé, le capteur 3 voies ne fonctionnera pas correctement.

4\.**Flow Chart**

![Img](./media/Makecode_70f1fd80.png)


5\.  **Test Code**

![](./media/Makecode_4b104155.png)

![Img](./media/Makecode_d36220cf.png)

![Img](./media/Makecode_4fff0a27.png)

![Img](./media/Makecode_ca91a31f.png)


Cliquez sur “JavaScript” pour voir le code JavaScript correspondant :

![](./media/Makecode_f5caa06a.png)

![](./media/Makecode_8f5f07ec.png)

5\. **Test Result**

Téléversez le code sur le micro:bit et positionnez l’interrupteur POWER sur ON, la voiture de suivi suit la ligne noire vers l’avant.

**Note :** activez l’interrupteur à l’arrière de la voiture micro:bit ; la largeur de la ligne noire doit être supérieure à la largeur du capteur de suivi de ligne.

Évitez de tester la voiture intelligente sous un fort éclairage.