## Projet 12 : Communication sans fil Bluetooth

![](./media/Makecode_041ff91a.jpg)

### (1)Description du projet :

Remarque : Cette leçon explique comment téléverser du code via Bluetooth en utilisant une application, donc aucun code n'est fourni. Veuillez suivre les étapes dans le GIF animé.

La carte principale Micro: Bit main board V2 est équipée d'un processeur nRF52833 (avec un module BLE (Bluetooth Low Energy) intégré, Bluetooth 5.1) et d'une antenne 2,4 GHz pour la communication sans fil Bluetooth et la communication sans fil 2,4 GHz. Grâce à ces éléments, la carte peut communiquer avec une variété d'appareils Bluetooth, y compris les smartphones et les tablettes.

Dans ce projet, nous nous concentrons principalement sur la fonction de communication sans fil Bluetooth de cette carte principale. Connectée via Bluetooth, elle peut transmettre du code ou des signaux. À cette fin, nous devons connecter un appareil Apple (un iPhone ou un iPad) à la carte.

Étant donné que la configuration des téléphones Android pour réaliser la transmission sans fil est similaire à celle des appareils Apple, il n'est pas nécessaire de la réexpliquer.

### (2) Préparation

Connectez le Micro:bit main board V2 à votre ordinateur via le câble Micro USB.

Un appareil Apple (un téléphone ou un iPad) ou un appareil Android ;

### (3) Installer Micro:bit :

Pour Android

![](./media/Makecode_0cf9abf0.gif)

Pour ios

![](./media/Makecode_5937459b.gif)

(4)Code de test :

Ensuite, nous utiliserons nos téléphones pour écrire du code et nous connecter via Bluetooth (Remarque : le processus est identique pour les appareils Android et iOS ; cette démonstration utilise un téléphone Android).

1、Ouvrez le logiciel et connectez-vous au Bluetooth.

![](./media/Makecode_dcb2416a.gif)

2、Appuyez successivement sur le bouton A, le bouton B et le bouton de réinitialisation à l'arrière du Microbit. La carte principale affichera alors une icône.

![](./media/Makecode_6985c2b1.gif)

3、Saisissez le motif affiché à l'étape deux dans l'interface du téléphone.

![](./media/Makecode_9095fb35.gif)

Écrire le code et téléverser

1、Accédez à l'interface de programmation du code et écrivez un code.

![](./media/Makecode_b7c8c1ca.gif)

2、Appuyez successivement sur le bouton A, le bouton B et le bouton de réinitialisation. (Remarque : cette procédure doit être répétée chaque fois que du code est téléversé via l'application.)

 ![](./media/Makecode_86ab2b39.gif)

3、Après avoir confirmé que l'icône Microbit correspond à celle affichée sur votre téléphone, cliquez simplement sur « Next ».

![](./media/Makecode_f3c17f45.gif)

Enfin, vous pouvez voir la carte Microbit afficher le motif du code.

Ici, nous avons terminé le processus de téléversement du code vers le téléphone. Il est important de noter :

1. Pour connecter le téléphone à la carte Microbit, appuyez successivement sur les boutons A, B et Reset. L'affichage matriciel affichera alors un motif, qui doit être saisi dans le téléphone.
2. La carte Microbit peut être alimentée via un câble USB ou en fournissant 3V à l'entrée d'alimentation de la carte via un pack de batteries. Remarque : la tension ne doit pas dépasser 3V, car un dépassement endommagerait la carte.