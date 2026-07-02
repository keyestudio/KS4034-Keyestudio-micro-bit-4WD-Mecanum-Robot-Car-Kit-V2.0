### Projet 3：Matrice de points LED 5×5

![](./media/Python_b855274f.png)

1\.  **Description**

La matrice de points est très courante dans la vie quotidienne et trouve de larges applications dans les écrans publicitaires LED, l'affichage d'étage des ascenseurs, les annonces d'arrêt de bus, etc.
La matrice de LED de la carte principale Micro: Bit contient 25 diodes. Auparavant, nous avons réussi à contrôler une LED particulière via son point de position. Sur la même théorie, nous pouvons allumer plusieurs LED en même temps pour afficher des motifs, des chiffres et des caractères.

De plus, nous pouvons cliquer sur “show icon” pour choisir le motif que nous souhaitons afficher. Enfin, nous pouvons également concevoir nos propres motifs.

2\.  **Préparation**

A. Connectez la carte principale micro:bit à votre ordinateur via le câble USB

B. Ouvrez la version hors ligne de Mu.

3\.  **Code de test1**

Vous pouvez ouvrir le fichier “5×5 LED Dot Matrix-1\.py” pour importer le code. Vous pouvez aussi saisir le code vous-même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles doivent être écrits en anglais.**)

![](./media/Python_00f15f0a.png)

```python
from microbit import *

val = Image("00900:""00900:""90909:""09990:""00900")

display.show(val)
```

Cliquez sur “Check” pour vérifier les erreurs dans le code. Le programme est considéré comme erroné si des soulignements et des curseurs sont affichés. 

![](./media/Python_a1197f5e.png)

Si le code est correct, connectez le micro:bit à l'ordinateur et cliquez sur “Flash” pour télécharger le code sur la carte micro:bit.

![](./media/Python_1fd78e31.png)

4\.  **Résultat du test1**

Après le téléchargement réussi du code sur la carte, **alimentez via le câble micro USB ou une alimentation externe (placez l'interrupteur DIP sur ON)**, et appuyez sur le bouton de réinitialisation de la carte.

![Img](./media/Python_bb3e1312.png)

Vous verrez que la matrice 5×5 commence à afficher une flèche vers le bas ![](./media/Python_26c7d8c0.png).

5\.  **Code de test2**

Vous pouvez ouvrir le fichier “5×5 LED Dot Matrix-2\.py” pour importer le code. Vous pouvez aussi saisir le code vous-même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles doivent être écrits en anglais.**)

![](./media/Python_dc6eea45.png)

```python
from microbit import *
val = Image("00900:""00900:""90909:""09990:""00900")
display.show('1')
sleep(500)
display.show('2')
sleep(500)
display.show('3')
sleep(500)
display.show('4')
sleep(500)
display.show('5')
sleep(500)
display.show(val)
sleep(500)
display.scroll("hello!")
sleep(200)
display.show(Image.HEART)
sleep(500)
display.show(Image.ARROW_NE)
sleep(500)
display.show(Image.ARROW_SE)
sleep(500)
display.show(Image.ARROW_SW)
sleep(500)
display.show(Image.ARROW_NW)
sleep(500)
display.clear()
```

Cliquez sur “Check” pour vérifier les erreurs dans le code. Le programme est considéré comme erroné si des soulignements et des curseurs sont affichés. 

![](./media/Python_14bb490a.png)

Si le code est correct, connectez le micro:bit à l'ordinateur et cliquez sur “Flash” pour télécharger le code sur la carte micro:bit.

![](./media/Python_a05c33d2.png)

6\.  **Résultat du test2**

Après le téléchargement réussi du code sur la carte, **alimentez via le câble micro USB ou une alimentation externe (placez l'interrupteur DIP sur ON)**, et appuyez sur le bouton de réinitialisation de la carte.

![Img](./media/Python_bb3e1312.png)

Vous constaterez que la matrice 5×5 commence à afficher les chiffres 1, 2, 3, 4 et 5, puis affiche alternativement une flèche vers le bas ![](./media/Python_26c7d8c0.png), “Hello”, un motif de cœur ![](./media/Python_9b18b2b8.png), une flèche vers le nord-est ![](./media/Python_364f2e35.png), puis vers le sud-est
![](./media/Python_fb3ba009.png), puis vers le sud-ouest ![](./media/Python_7ec21961.png) et enfin vers le nord-ouest ![](./media/Python_ced0bb41.png).

7\.  **Explication du code**

![Img](./media/Python_ef42956d.png)


6.  **Référence**

display.scroll() ：

L'affichage défile pour montrer les valeurs ; si c'est un entier ou un flottant, nous utilisons str() pour le convertir en chaîne de caractères.

Pour plus de détails, veuillez vous référer au lien : [https://microbit-micropython.readthedocs.io/en/latest/utime.html](https://microbit-micropython.readthedocs.io/en/latest/utime.html)