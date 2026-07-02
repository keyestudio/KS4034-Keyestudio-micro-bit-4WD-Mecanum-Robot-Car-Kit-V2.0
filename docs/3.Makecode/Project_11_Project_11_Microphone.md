## Projet 11 : Microphone

![](./media/Makecode_d2f14bdc.jpg)

[Cliquez pour télécharger le code 1 de cette leçon](./Code/Microphone.hex)

[Cliquez pour télécharger le code 2 de cette leçon](./Code/Microphone2.hex)

### (1)Description du projet :

La carte principale Micro:bit main board V2 est équipée d’un microphone qui peut mesurer le volume de l’environnement ambiant. Lorsque vous applaudissez, le voyant LED du microphone s’allume. Comme il peut mesurer l’intensité du son, vous pouvez réaliser une échelle de bruit ou un éclairage disco qui change avec la musique. Le microphone est placé en face du voyant LED du microphone et à proximité d’orifices qui laissent passer le son. Lorsque la carte détecte un son, le témoin LED s’allume.

### (2)Composants nécessaires :

Micro:bit main board V2

Câble Micro USB

### (3)Code de test 1 :

Reliez l’ordinateur à la carte micro:bit avec un câble micro USB et programmez dans l’éditeur MakeCode,

![](./media/Makecode_7c037c9b.gif)

Programme complet :

![](./media/Makecode_1ea97896.png)

### (4)Résultats du test 1 :

Après avoir chargé le code, un grand icône de cœur s’affiche lorsque du son ambiant est détecté, et un petit icône de cœur lorsque l’environnement est calme (Remarque : les sons trop faibles pour être détectés ne déclencheront pas la réponse).

![](./media/Makecode_facbbb50.gif)

### (5)Code de test 2 :

Reliez l’ordinateur à la carte micro:bit avec un câble micro USB et programmez dans l’éditeur MakeCode,

![](./media/Makecode_68e37f22.gif)

Programme complet :

![](./media/Makecode_9851e889.png)

### (6)Résultats du test 2 :

![](./media/Makecode_0b914334.gif)

Après le téléchargement du code, la matrice de points pulse en synchronisation avec les variations sonores. L’appui sur la touche « A » affiche la valeur numérique du son actuel.