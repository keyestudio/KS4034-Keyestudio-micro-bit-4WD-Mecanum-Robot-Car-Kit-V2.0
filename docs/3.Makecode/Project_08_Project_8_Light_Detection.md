## Projet 8 : Détection de la lumière

![](./media/Makecode_14063ef9.jpg)

[Cliquez pour télécharger le code de cette leçon](./Code/Light-Detection.hex)

### (1) Description du projet :

Dans ce projet, nous nous concentrons sur la fonction de détection de la lumière du Micro: Bit main board V2. Cela est réalisé par la matrice de LED, car la carte principale n'est pas équipée d'une photorésistance.

### (2) Composants nécessaires :

Micro:bit main board V2

Câble Micro USB

### (3) Code de test :

Reliez l'ordinateur à la carte micro:bit via le câble Micro USB et programmez dans l'éditeur MakeCode,

![](./media/Makecode_38ffa3b8.gif)

Programme complet :

![](./media/Makecode_5b9a2acf.png)

### (4) Résultats du test :

Téléversez le code de test sur le micro:bit main board V2, alimentez la carte via le câble USB et cliquez sur "Show console Device".

Lorsque la matrice de points LED est couverte par la main, l'intensité lumineuse affichée est d'environ 0 ; lorsque la matrice de points LED est exposée à la lumière, l'intensité lumineuse affichée augmente avec la luminosité, comme montré ci-dessous.

![](./media/Makecode_11dd3c0b.gif)

Si vous utilisez Windows 7 ou 8 au lieu de Windows 10, Google Chrome ne pourra pas reconnaître les appareils. Vous devrez utiliser le logiciel de moniteur série CoolTerm pour lire les données.

Vous pouvez ouvrir le logiciel CoolTerm, cliquer sur Options, sélectionner SerialPort, définir le COM port et régler la baud rate sur 115200 (après test, la baud rate de la communication USB SerialPort sur le Micro: Bit main board V2 est 115200), cliquer sur OK, puis sur Connect. Le moniteur série CoolTerm affiche la valeur de l'intensité lumineuse, comme illustré ci-dessous :

![](./media/Makecode_3c6eae52.gif)

---