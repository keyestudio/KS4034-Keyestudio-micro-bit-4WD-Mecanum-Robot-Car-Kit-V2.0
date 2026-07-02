## Projet 7: Accelerometer

![](./media/Makecode_66670811.jpg)

[Cliquez pour télécharger le code 1 de cette leçon](./Code/Accelerometer.hex)

[Cliquez pour télécharger le code 2 de cette leçon](./Code/Accelerometer2.hex)

### (1)Description du projet :

La carte principale Micro: Bit main board V2 intègre un capteur d'accélération gravitationnelle LSM303AGR, également appelé accéléromètre, avec une résolution de 8/10/12 bits. Dans la section du code, la plage peut être réglée sur 1g, 2g, 4g et 8g.

Nous utilisons souvent des accéléromètres pour détecter l'état des machines. Dans ce projet, nous allons expliquer comment mesurer l'orientation de la carte à l'aide de l'accéléromètre, puis examiner les données brutes tri-axiales fournies par l'accéléromètre.

### (2)Composants nécessaires :

Micro:bit main board V2

Câble Micro USB

### (3)Code de test 1 :

Reliez l'ordinateur à la carte micro:bit avec un câble Micro USB et programmez dans l'éditeur MakeCode,

![](./media/Makecode_2cd48603.gif)

Programme complet :

![](./media/Makecode_ba28162b.png)

### (4)Résultats du test 1 :

Après avoir téléversé le Code de Test 1 sur la carte micro:bit V2, le changement d'orientation de la carte entraîne l'affichage de différents chiffres sur la matrice de points 5x5.

![](./media/Makecode_2e6708e6.gif)

Si nous secouons le Micro: Bit main board V2, quelle que soit la direction, la matrice de LED affiche le chiffre "1".

Lorsqu'elle est tenue à la verticale (le logo au-dessus de la matrice de LED), le chiffre 2 s'affiche.

![](./media/Makecode_67247ae1.jpg)

Lorsqu'elle est tenue tête en bas (le logo sous la matrice de LED), elle s'affiche comme ci-dessous.

![](./media/Makecode_1668a9d0.jpg)

Lorsqu'elle est posée immobile sur le bureau, face visible, le chiffre 4 apparaît.

![](./media/Makecode_0dd33fa1.jpg)

Lorsqu'elle est posée immobile sur le bureau, face arrière visible, le chiffre 5 s'affiche.

Lorsque la carte est inclinée vers la gauche, la matrice de LED affiche le chiffre 6 comme indiqué ci-dessous.

![](./media/Makecode_ce2b3501.jpg)

Lorsque la carte est inclinée vers la droite, la matrice de LED affiche le chiffre 7 comme indiqué ci-dessous.

![](./media/Makecode_d098ff98.jpg)

Lorsque la carte est frappée au sol, ce processus peut être considéré comme une chute libre et la matrice de LED affiche le chiffre 8. (Veuillez noter que ce test n'est pas recommandé car il peut endommager la carte principale.)

Attention : si vous souhaitez essayer cette fonction, vous pouvez également régler l'accélération sur 3g, 6g ou 8g. Toutefois, nous ne le recommandons toujours pas.

### (5)Code de test 2 :

![](./media/Makecode_99083bf6.gif)

Programme complet :

![](./media/Makecode_42654b0e.png)

### (6) Résultats du test 2

Téléversez le code de test sur le Micro: Bit main board V2, alimentez la carte principale via le câble USB et cliquez sur "Show console Device".

L'interface suivante affiche les valeurs de décomposition de l'accélération sur les axes X, Y et Z respectivement, ainsi que la synthèse de l'accélération (synthèse de la gravité et d'autres forces externes).

![](./media/Makecode_c17f5477.gif)

Après consultation du manuel de données du MMA8653FC et du schéma matériel du Micro: Bit main board V2, les coordonnées de l'accéléromètre de la carte mère Micro: Bit V2 sont représentées dans la figure ci-dessous :

![](./media/Makecode_79d90885.jpg)

Si vous utilisez Windows 7 ou 8 au lieu de Windows 10, Google Chrome ne pourra pas appairer les appareils. Vous devrez utiliser le logiciel de moniteur série CoolTerm pour lire les données. Ouvrez CoolTerm, cliquez sur Options, sélectionnez SerialPort, définissez le port COM et mettez la vitesse en bauds à 115200 (après tests, la vitesse de communication du port série USB sur le Micro: Bit main board V2 est de 115200), cliquez sur OK, puis Connect. Le moniteur série CoolTerm affiche les données des axes X, Y et Z, comme illustré ci-dessous :

![](./media/Makecode_2a63fc72.gif)