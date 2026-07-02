## Projet 19：Télécommande IR

### Projet 19.1：Décoder la télécommande IR

![](./media/Makecode_3a3e9860.png)

1\. **Description**

Il ne fait aucun doute que la télécommande infrarouge est omniprésente dans la vie quotidienne. Elle est utilisée pour contrôler divers appareils ménagers, tels que les téléviseurs, stéréos, magnétoscopes et récepteurs satellite. La télécommande infrarouge se compose d'un système d'émission infrarouge et d'un système de réception infrarouge, c'est-à-dire d'une télécommande, d'un module récepteur infrarouge et d'un microcontrôleur capable de décoder.

![](./media/Makecode_9980b41f.png)

Le signal porteuse infrarouge 38K émis par la télécommande est encodé par la puce d'encodage de la télécommande. Il est composé d'une section de code pilote, d'un code utilisateur, du code inverse utilisateur, d'un code de données et du code inverse de données. L'intervalle de temps des impulsions permet de distinguer s'il s'agit d'un signal 0 ou 1 et l'encodage est constitué de ces signaux 0 et 1.

Le code utilisateur d'une même télécommande reste inchangé. Le code de données permet de distinguer la touche.

Lorsque le bouton de la télécommande est enfoncé, la télécommande envoie un signal porteur infrarouge. Lorsque le récepteur IR reçoit le signal, le programme décode le signal porteur et détermine quelle touche a été enfoncée. Le MCU décode le signal 01 reçu, ce qui permet de déterminer quelle touche de la télécommande a été pressée.

Le récepteur infrarouge que nous utilisons est un module récepteur infrarouge. Principalement composé d'une tête de réception infrarouge, c'est un dispositif qui intègre réception, amplification et démodulation. Son circuit intégré interne a déjà effectué la démodulation et peut assurer la réception infrarouge jusqu'à la sortie et est compatible avec les signaux TTL. De plus, il convient à la télécommande infrarouge et à la transmission de données infrarouges. Le module de réception infrarouge fabriqué par le récepteur n'a que trois broches : ligne de signal, VCC et GND.

Selon l'image ci-dessus, le port intégré du récepteur infrarouge est connecté au port P9 5V G sur la carte pilote du moteur et contrôlé par le P9 du micro:bit.

2\. **Paramètres :**

- Tension de fonctionnement : 3.3-5V（DC）

- Interface : 3PIN

- Signal de sortie : signal numérique

- Angle de réception : 90 degrés

- Fréquence : 38khz

- Distance de réception : environ 5m

3\. **Préparation**

- Insérez la carte micro:bit dans le logement du keyestudio   4WD Mecanum Robot Car V2.0

- Placez des piles dans le support de piles

- Tournez l'interrupteur d'alimentation en position ON

- Connectez le micro:bit à votre ordinateur via un câble USB

- Ouvrez la version Web de Makecode


4\. **Code de test**

![](./media/Makecode_2e20f731.png)

Cliquez sur “JavaScript" pour passer au code JavaScript correspondant :

![](./media/Makecode_87e18859.png)

**Explication du code :** Si les boutons ne sont pas enfoncés, le moniteur série affiche constamment 0 ; lorsqu'ils sont enfoncés, les valeurs des touches correspondantes sont affichées.

**Remarques：**

La télécommande fournie dans ce kit ne contient pas de piles. Nous vous recommandons de les acheter en ligne. (type de pile : CR2025).

Assurez-vous que la télécommande IR fonctionne avant le test. Voici un conseil pour la vérifier :

Ouvrez l'appareil photo du téléphone portable, pointez la télécommande IR vers l'appareil photo et appuyez sur un bouton. Si vous voyez une lumière violette clignotante à l'écran de l'appareil photo, la télécommande fonctionne.

5\. **Résultat du test**

Téléchargez le code sur la carte micro:bit et ne débranchez pas le câble USB. Cliquez ![](./media/Makecode_e0580d78.png)

![](./media/Makecode_0d3198e0.png)

Pointez la télécommande IR vers le récepteur IR et appuyez sur le bouton ; le moniteur série affichera les valeurs de touches correspondantes, comme indiqué ci-dessous :

![](./media/Makecode_c7a33a4c.png)

Ouvrez CoolTerm, cliquez sur Options pour sélectionner SerialPort. Réglez le port COM et le débit en bauds à 115200. Cliquez sur “OK” et “Connect”.

Le moniteur série CoolTerm affiche la valeur de la touche comme suit :

![Img](./media/Makecode_155c857a.png)

La valeur de la touche est affichée à titre de référence :

![](./media/Makecode_1fc0d9bb.jpg)

### Projet 19.2：Télécommande IR

![Img](./media/Makecode_643cb701.png)

1\. **Description**

Dans ce projet, nous combinons la télécommande IR avec le car shield pour réaliser une voiture intelligente contrôlée par IR. Le principe consiste à contrôler le mouvement de la voiture en envoyant des signaux de touches depuis la télécommande IR vers le module récepteur IR du car shield.

2\. **Préparation**

- Insérez la carte micro:bit dans le logement du keyestudio   4WD Mecanum Robot Car V2.0

- Placez des piles dans le support de piles

- Tournez l'interrupteur d'alimentation en position ON

- Connectez le micro:bit à votre ordinateur via un câble USB

- Ouvrez la version Web de Makecode

**Remarque :** Le capteur infrarouge et la télécommande infrarouge ne doivent pas être utilisés dans des environnements présentant des interférences infrarouges, comme la lumière du soleil, car celle-ci contient de nombreuses lumières invisibles, telles que l'infrarouge et l'ultraviolet. Dans un environnement fortement ensoleillé, ils ne peuvent pas fonctionner normalement.

3\. **Organigramme**

![Img](./media/Makecode_e5f416e3.png)

4\. **Code de test**

![](./media/Makecode_22d06d74.png)

Cliquez sur “JavaScript" pour passer au code JavaScript correspondant :

![](./media/Makecode_e68b6275.png)

![](./media/Makecode_94de6552.png)

5\. **Résultat du test**

Téléchargez le code sur la carte micro:bit et mettez l'interrupteur POWER sur ON.

Pointez la télécommande IR vers le micro:bit et appuyez sur un bouton pour contrôler le déplacement de la voiture intelligente.

![](./media/Makecode_d55474f3.png) Le bouton fait avancer la voiture intelligente，![](./media/Makecode_5c8a6549.png) signifie tourner à gauche，![](./media/Makecode_41116032.png) implique tourner à droite，![](./media/Makecode_369433f6.png) indique reculer，![](./media/Makecode_a8ef4b17.png) arrête la voiture.

**Remarque :** La distance entre la télécommande IR et la tête réceptrice IR de la voiture intelligente doit être inférieure à 5 m pendant le test.

---