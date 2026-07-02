### Projet 4：Boutons programmables

![](./media/Python_06be84fb.png)

1\.  **Description**

![](./media/Python_b6d60ae2.png)

Les boutons peuvent être utilisés pour contrôler des circuits. Dans un circuit intégré avec un bouton-poussoir, le circuit est fermé lorsque le bouton est enfoncé et s'ouvre de nouveau après son relâchement.

Les deux extrémités du bouton ressemblent à deux montagnes. Il y a une rivière entre les deux. 
La pièce métallique interne relie les deux côtés pour laisser passer le courant, comme construire un pont pour relier deux montagnes.

La structure interne du bouton est montrée comme suit : avant d'enfoncer le bouton, 1, 2, 3 et 4 sont activés. Cependant, 1 et 3 ou 1 et 4 ou 2 et 3 ou 2 et 4 sont déconnectés ; ces connexions ne sont activées que lorsque le bouton est pressé. ![](./media/Python_d2a204e6.png)

La carte principale micro:bit possède trois boutons-poussoirs, deux sont des boutons programmables (marqués A et B), et celui de l'autre côté est un bouton de réinitialisation. En appuyant sur les deux boutons programmables, on peut entrer trois signaux différents. On peut appuyer sur le bouton A ou B seul, ou les presser ensemble ; la matrice de LED affiche alors respectivement A, B et AB. Commençons.

2\.  **Préparation**

A. Connectez la carte principale micro:bit à votre ordinateur via le câble USB.

B. Ouvrez la version hors ligne de Mu.

3\.  **Test Code1**

Ouvrez le logiciel Mu et ouvrez le fichier “Programmable Buttons-1\.py” pour importer le code. Vous pouvez aussi saisir le code vous-même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles doivent être écrits en anglais.**)

![](./media/Python_2637f524.png)

```python
from microbit import *

while True:
    if button_a.is_pressed():
        display.show("A")
    elif button_a.is_pressed() and button_b.is_pressed():
        display.scroll("AB")
    elif button_b.is_pressed():
        display.show("B")
```
Cliquez sur « Check » pour vérifier les erreurs dans le code. Le programme est incorrect si des soulignements et des curseurs sont affichés.

![](./media/Python_a0f284f3.png)

Si le code est correct, connectez le micro:bit à votre ordinateur et cliquez sur « Flash » pour télécharger le code sur la carte micro:bit.

![](./media/Python_5694d3ce.png)

4\.  **Résultat du test 1**

Après avoir téléchargé le code sur la carte avec succès, **alimentez via le câble micro USB ou une alimentation externe (poussez l'interrupteur DIP sur ON)**, puis appuyez sur le bouton de réinitialisation de la carte.

![Img](./media/Python_bb3e1312.png)

La matrice de LED 5*5 affiche « A » si le bouton A est pressé, puis « B » si le bouton B est pressé, et « AB » si les boutons A et B sont pressés simultanément.

5\.  **Test Code2**

Ouvrez le logiciel Mu et ouvrez le fichier “Programmable Buttons-2\.py” pour importer le code. Vous pouvez aussi saisir le code vous-même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles doivent être écrits en anglais.**)

![](./media/Python_1a1126f6.png)

![](./media/Python_94849305.png)

```python
from microbit import *
a = 0
b = 0
val1 = Image("00000:""00000:""00000:""00000:""00900")
val2 = Image("00000:""00000:""00000:""00900:""99999")
val3 = Image("00000:""00000:""00900:""99999:""99999")
val4 = Image("00000:""00900:""99999:""99999:""99999")
val5 = Image("00900:""99999:""99999:""99999:""99999")
val6 = Image("99999:""99999:""99999:""99999:""99999")
display.show(val1)

while True:
    while button_a.is_pressed() == True:
        sleep(10)
        if button_a.is_pressed() == False:
            a = a + 1
            if(a >= 5):
                a = 5
            break
    while button_b.is_pressed() == True:
        sleep(10)
        if button_b.is_pressed() == False:
            a = a - 1
            if(a <= 0):
                a = 0
            break
    if a == 0:
        display.show(val1)
    if a == 1:
        display.show(val2)
    if a == 2:
        display.show(val3)
    if a == 3:
        display.show(val4)
    if a == 4:
        display.show(val5)
    if a == 5:
        display.show(val6)
```
Cliquez sur « Check » pour vérifier les erreurs dans le code. Le programme est incorrect si des soulignements et des curseurs sont affichés.

![](./media/Python_21771d90.png)

![Img](./media/Python_8d257384.png)

Si le code est correct, connectez le micro:bit à votre ordinateur et cliquez sur « Flash » pour télécharger le code sur la carte micro:bit.

![](./media/Python_84ba8cde.png)

![Img](./media/Python_8d257384.png)

6\.  **Résultat du test 2**

Après avoir téléchargé le code sur la carte avec succès, **alimentez via le câble micro USB ou une alimentation externe (poussez l'interrupteur DIP sur ON)**, puis appuyez sur le bouton de réinitialisation de la carte.

![Img](./media/Python_bb3e1312.png)

Si le bouton A est pressé, le nombre de LED rouge augmente ; si le bouton B est pressé, le nombre de LED rouge diminue.

7\.  **Explication du code**

![Img](./media/Python_b33858dc.png)

![Img](./media/Python_32bd1cca.png)

---