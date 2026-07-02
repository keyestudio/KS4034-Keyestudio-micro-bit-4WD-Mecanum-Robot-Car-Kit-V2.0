### Projet 1：Heart Beat

![](./media/Python_b855274f.png)

1\.  **Description**

Ce projet est facile à réaliser uniquement avec une carte micro:bit et un câble micro USB. Cet expérience sert d'introduction pour vous permettre d'entrer dans le monde magique de la programmation du micro:bit.

2\.  **Préparation**

A. Branchez la carte micro:bit à votre ordinateur via le câble USB.

B. Ouvrez la version hors ligne de Mu.

3\.  **Code de test**

Ouvrez le logiciel Mu, appuyez sur «Load», sélectionnez le fichier «“microbit-Heartbeat\.py“» et cliquez sur «open» :

![](./media/Python_1ec17d44.png)

![](./media/Python_4bda2b61.png)

Il existe une autre façon d'importer du code. Ouvrez Mu et glissez le fichier „microbit-Heartbeat\.py“ dedans.

![](./media/Python_c5b7322b.png)

Vous pouvez aussi saisir le code directement dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles anglais doivent être écrits en anglais.**)

![](./media/Python_80af4cb3.png)

```python
from microbit import *

while True:
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART_SMALL)
    sleep(500)
```
Voici la liste des images intégrées :

• Image.HEART

• Image.HEART_SMALL

• Image.HAPPY

• Image.SMILE

• Image.SAD

• Image.CONFUSED

• Image.ANGRY

• Image.ASLEEP

• Image.SURPRISED

• Image.SILLY

• Image.FABULOUS

• Image.MEH

• Image.YES

• Image.NO

• Image.CLOCK12, Image.CLOCK11, Image.CLOCK10, Image.CLOCK9, Image.CLOCK8, Image.CLOCK7, Image.CLOCK6, Image.CLOCK5,

Image.CLOCK4, Image.CLOCK3, Image.CLOCK2, Image.CLOCK1

• Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE, Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW

• Image.TRIANGLE

• Image.TRIANGLE_LEFT

• Image.CHESSBOARD

• Image.DIAMOND

• Image.DIAMOND_SMALL

• Image.SQUARE

• Image.SQUARE_SMALL

• Image.RABBIT

• Image.COW

• Image.MUSIC_CROTCHET

• Image.MUSIC_QUAVER

• Image.MUSIC_QUAVERS

• Image.PITCHFORK

• Image.PACMAN

• Image.TARGET

• Image.TSHIRT

• Image.ROLLERSKATE

• Image.DUCK

• Image.HOUSE

• Image.TORTOISE

• Image.BUTTERFLY

• Image.STICKFIGURE

• Image.GHOST

• Image.SWORD

• Image.GIRAFFE

• Image.SKULL

• Image.UMBRELLA

• Image.SNAKE，Image.ALL_CLOCKS，Image.ALL_ARROWS

Connectez la carte micro:bit à l'ordinateur via un câble USB, puis cliquez sur «Flash» pour télécharger le code sur la carte.

![](./media/Python_93e18731.png)


![](./media/Python_48e78948.png)


![](./media/Python_cc33f1a9.png)

Le code, même s'il contient des erreurs, peut être téléchargé avec succès sur la carte micro:bit, mais il ne fonctionnera pas sur le micro:bit.

Cliquez sur «Flash» pour télécharger le code sur le micro:bit.

![](./media/Python_8982d0b0.png)

Cliquez sur «REPL» et appuyez sur le bouton reset du micro:bit ; les informations d'erreur s'afficheront dans la fenêtre REPL, comme illustré ci-dessous :

![](./media/Python_0c2abf18.png)

Cliquez de nouveau sur «REPL» pour désactiver le mode REPL, puis vous pourrez actualiser le nouveau code.

Pour vérifier que le code est correct, il suffit d'appuyer sur «Check». Les erreurs seront affichées dans la fenêtre.

![](./media/Python_b994c0d3.png)

Modifiez le code selon les indications puis cliquez sur «Check».

![](./media/Python_bc5cbed3.png)

 Veuillez consulter le site pour plus de tutoriels : [https://codewith.mu/en/tutorials/](https://codewith.mu/en/tutorials/)

4\.  **Résultat du test**

Cliquez sur “<span style="color: rgb(255, 76, 65);">**Flash**</span>” pour charger le code sur la carte micro:bit.

![Img](./media/Python_ed83ac25.png)

Après avoir téléchargé le code sur la carte avec succès, **alimentez via le câble micro USB ou une alimentation externe (mettre l'interrupteur DIP sur ON)**, et appuyez sur le bouton reset de la carte.

![Img](./media/Python_bb3e1312.png)

La matrice LED affiche alternativement le motif «❤» puis «![](./media/Python_04fdfc90.png)».

5\.  **Explication du code**

|from microbit import*|Importe le fichier de la bibliothèque du micro:bit|
|-|-|
|while True:|Ceci est une boucle permanente qui fait exécuter au micro:bit le code contenu dans cette boucle indéfiniment.|
|display.show(Image.HEART)|micro:bit affiche «❤»|
|sleep(500)|Attente de 500 ms|
|display.show(Image.HEART_SMALL)|La matrice LED affiche «![](./media/Python_04fdfc90.png)»|

---