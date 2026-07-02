## Projet 5 : Détection de la température

![](./media/Makecode_22c6434f.jpg)

[Cliquez pour télécharger le code 1 de cette leçon](./Code/Temperature-Detection.hex)

[Cliquez pour télécharger le code 2 de cette leçon](./Code/Temperature-Detection2.hex)

### (1)Description du projet :

La carte principale Micro:bit main board V2 n'est pas équipée d'un capteur de température, mais utilise le capteur de température intégré au circuit NFR52833 pour la détection. Par conséquent, la température détectée est plus proche de la température du circuit et peut différer de la température ambiante.

### (2)Composants nécessaires :

Micro:bit main board V2

Câble Micro USB

### (3)Code de test 1 :

![](./media/Makecode_e6674fe9.gif)

### (4)Résultats du test 1 :

Après avoir téléversé le code de test 1 sur le Micro:bit main board V2, alimenté la carte via le câble USB et cliqué sur "Show console Device", les données de température s'affichent dans le moniteur série comme illustré ci-dessous.

![](./media/Makecode_898eded8.gif)

Si vous utilisez Windows 7 ou 8 au lieu de Windows 10, Google Chrome ne pourra pas appairer les périphériques. Vous devrez utiliser le logiciel de moniteur série CoolTerm pour lire les données. Ouvrez CoolTerm, cliquez sur Options, sélectionnez SerialPort, choisissez le port COM et réglez le débit en bauds sur 115200 (après essais, le débit en bauds de la communication USB SerialPort sur le Micro:bit main board V2 est 115200), cliquez sur OK, puis Connect. Le moniteur série CoolTerm affiche la variation de la température dans l'environnement courant, comme montré dans les images ci-dessous :

![](./media/Makecode_268159a1.gif)

### (5)Code de test 2 :

Reliez l'ordinateur à la carte micro:bit par un câble Micro USB et programmez dans l'éditeur MakeCode,

![](./media/Makecode_4057bdd7.gif)

Programme complet :

![](./media/Makecode_ec457959.png)

### (6)Résultats du test 2 :

Après le téléchargement du code 2, lorsque la température ambiante est inférieure à 35℃, la matrice LED 5x5 affiche ![](./media/Makecode_350d26c6.png). Lorsque la température est égale ou supérieure à 35℃, le motif ![](./media/Makecode_ef8d7c88.png) apparaît.

---