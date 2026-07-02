### Projet 2：Allumer une seule LED

![](./media/Python_b855274f.png)

1\.  **Description**

La matrice de LED est composée de 25 diodes disposées en carré 5×5 et placées aux intersections des lignes de rangée (X) et des lignes de colonne (Y). Nous pouvons contrôler l'une des 25 LED en définissant des points de coordonnées. Par exemple, la première LED située sur la première ligne est (0,0) et la troisième LED positionnée sur la première ligne est (2,0), et ainsi de suite.

![](./media/Python_094d5908.png)

2\.  **Préparation**

A. Branchez la carte micro:bit à votre ordinateur via le câble USB

B. Ouvrez la version hors ligne de Mu.

3\.  **Code de test**

Ouvrez le logiciel Mu et ouvrez le fichier “Single LED display\.py.” pour importer le code. Vous pouvez également saisir le code vous-même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles anglais doivent être écrits en anglais**)

![](./media/Python_9545233e.png)

```python
from microbit import *

val1 = Image("09000:""00000:""00000:""00000:""00000:")
val2 = Image("00000:""00000:""00000:""00000:""00090:")
val3 = Image("00000:""00000:""00000:""00000:""00000:")

while True:
    display.show(val1)
    sleep(500)
    display.show(val3)
    sleep(500)
    display.show(val2)
    sleep(500)
    display.show(val3)
    sleep(500)

```

Cliquez sur “Check” pour vérifier les erreurs dans le code. Le programme est erroné si des soulignements et des curseurs s'affichent.

![](./media/Python_d205be08.png)

Si le code est correct, connectez le micro:bit à votre ordinateur et cliquez sur “Flash” pour télécharger le code sur la carte micro:bit.

![](./media/Python_86dd6eea.png)

4\.  **Résultat du test**

Après avoir téléchargé le code sur la carte avec succès, **alimentez via le câble micro USB ou une alimentation externe (passez le commutateur DIP sur ON)**, puis appuyez sur le bouton de réinitialisation de la carte.

![Img](./media/Python_bb3e1312.png)

La LED en (1,0) s'allumera et s'éteindra pendant 0,5 s, puis celle en (3,4) s'allumera et s'éteindra pendant 0,5 s, et cette séquence se répétera.

5\.  **Explication du code**

![Img](./media/Python_c79b7922.png)

6\.  **Référence**

sleep(ms) : temps de délai

Pour plus de détails sur le délai, veuillez consulter le lien : [https://microbit-micropython.readthedocs.io/en/latest/utime.html](https://microbit-micropython.readthedocs.io/en/latest/utime.html)