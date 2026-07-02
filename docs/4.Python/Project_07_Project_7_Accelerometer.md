### Projet 7：Accelerometer

![](./media/Python_26d107ae.png)

1\.  **Description**

La carte principale micro: bit V2 intègre un capteur d'accélération gravitationnelle LSM303AGR, également appelé accéléromètre, avec une résolution de 8/10/12 bits. Dans la section du code, la plage peut être définie sur 1g, 2g, 4g et 8g.

Nous utilisons souvent un accéléromètre pour détecter l'état des machines.

Dans ce projet, nous allons expliquer comment mesurer la position de la carte avec l'accéléromètre. Puis nous examinerons les données brutes tridimensionnelles fournies par l'accéléromètre.

2\.  **Préparation**

A. Branchez le micro:bit main board à votre ordinateur via le câble USB.

B. Ouvrez la version hors ligne de Mu.

3\.  **Code de test1**

Lancez le logiciel Mu et ouvrez le fichier “Three-axis acceleration sensor -1\.py“ pour importer le code. Vous pouvez également saisir le code vous-même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles doivent être écrits en anglais.**)

![](./media/Python_f20f5b58.png)

```python
from microbit import *

while True:
    gesture = accelerometer.current_gesture()

    if gesture == "shake":
        display.show("1")
    if gesture == "up":
        display.show("2")
    if gesture == "down":
        display.show("3")
    if gesture == "face up":
        display.show("4")
    if gesture == "face down":
        display.show("5")
    if gesture == "left":
        display.show("6")
    if gesture == "right":
        display.show("7")
    if gesture == "freefall":
        display.show("8")
```

Cliquez sur “Check” pour examiner les erreurs dans le code. Le programme est erroné si des soulignements et des curseurs sont affichés. 

![](./media/Python_07e4b578.png)

Si le code est correct, connectez le micro:bit à votre ordinateur et cliquez sur “Flash” pour télécharger le code sur la carte micro:bit.

![](./media/Python_eb56750b.png)

4\.  **Résultat du test1**

Après avoir téléchargé le code sur la carte avec succès, **alimentez via le câble micro USB ou une alimentation externe (mettez le commutateur DIP sur ON)**, et appuyez sur le bouton de réinitialisation du micro:bit.

![Img](./media/Python_bb3e1312.png)

Lorsque nous secouons le micro: bit main board, quelle que soit la direction, la matrice de LED affiche le chiffre “1”.

Lorsqu'il est maintenu à la verticale (le logo au-dessus de la matrice LED), le chiffre 2 apparaît.

![](./media/Python_b91421df.jpg)

Lorsqu'il est maintenu à l'envers (le logo sous la matrice LED), il s'affiche comme ci-dessous.

![](./media/Python_69e81587.jpg)

Lorsqu'il est posé immobile sur le bureau, face visible, le chiffre 4 apparaît.

![](./media/Python_9e08cb69.jpg)

Lorsqu'il est posé immobile sur le bureau, face arrière visible, le chiffre 5 apparaît.

Lorsque la carte est inclinée vers la gauche, la matrice de LED affiche le chiffre 6, comme illustré ci-dessous :

![](./media/Python_81fa2ce1.jpg)

Lorsque la carte est inclinée vers la droite, la matrice de LED affiche le chiffre 7, comme illustré ci-dessous：

![](./media/Python_fc13912b.jpg)

Lorsque la carte est projetée au sol, ce processus peut être considéré comme une chute libre et la matrice de LED affiche le chiffre 8. (Veuillez noter que ce test n'est pas recommandé car il peut endommager la carte principale.)

**Attention : Si vous souhaitez essayer cette fonction, vous pouvez également définir l'accélération sur 3g, 6g ou 8g.**

5\.  **Code de test2**

Lancez le logiciel Mu et ouvrez le fichier “Three-axis acceleration sensor -2\.py“ pour importer le code. Vous pouvez également saisir le code vous-même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles doivent être écrits en anglais.**)

![](./media/Python_0f7ccf57.png)

```python
from microbit import *

while True:

    x = accelerometer.get_x()

    y = accelerometer.get_y()

    z = accelerometer.get_z()

    print("x, y, z:", x, y, z)

    sleep(100)
```
Cliquez sur “Check” pour examiner les erreurs dans le code. Le programme est erroné si des soulignements et des curseurs sont affichés. 

![](./media/Python_0ed2221e.png)

Si le code est correct, connectez le micro:bit à votre ordinateur et cliquez sur “Flash” pour télécharger le code sur la carte micro:bit.

![](./media/Python_35c4c76b.png)

6\.  **Résultat du test2**

Après avoir téléchargé le code sur la carte avec succès, **alimentez via le câble micro USB ou une alimentation externe (mettez le commutateur DIP sur ON)**. Cliquez sur “REPL” et appuyez sur le bouton de réinitialisation du micro:bit.

![Img](./media/Python_bb3e1312.png)

Ensuite, la fenêtre REPL affichera les valeurs de l'accélération sur l'axe X, l'axe Y et l'axe Z comme indiqué ci-dessous :

![](./media/Python_940cfcf7.png)

Après consultation du manuel de données du MMA8653FC et du schéma matériel du micro: bit main board, les coordonnées de l'accéléromètre du micro: bit sont représentées dans la figure ci-dessous :

![](./media/Python_ebd0d44d.png)

7\.  **Explication du code**

![Img](./media/Python_d533d72c.png)

![Img](./media/Python_89d95342.png)

---