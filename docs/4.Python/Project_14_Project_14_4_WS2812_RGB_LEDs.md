### Projet 14 : 4 LED RGB WS2812

![](./media/Python_eecf79fe.png)

1\.  **Description**

Le shield pilote 4 LED RGB WS2812, est compatible avec la carte micro:bit et contrôlé par P7. Dans cette leçon, nous ferons afficher aux LED RGB différentes couleurs via P7. Trois jeux de codes de test sont fournis dans cette leçon pour produire différents effets sur les 4 LED WS2812 RGB.

![Img](./media/Python_0be70eda.png)

2\.  **Préparation**

- Insérez la carte micro:bit dans le logement du keyestudio 4WD Mecanum Robot Car V2.0

- Placez les piles dans le porte-piles

- Positionnez l'interrupteur d'alimentation sur ON

- Connectez le micro:bit à votre ordinateur via un câble USB

- Ouvrez la version hors ligne de Mu.

3\.  **Test Code1**

Lancez le logiciel Mu et ouvrez le fichier“4 WS2812 RGB LEDs-1\.py”pour importer le code\ Vous pouvez aussi saisir le code vous-même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles en anglais doivent être écrits en anglais.**)

Cliquez sur“Check”pour vérifier les erreurs dans le code. Le programme est incorrect si des soulignements et des curseurs apparaissent. 

![](./media/Python_5b5266e2.png)

```python
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin7, 4)
while True:
    for pixel_id1 in range(0, len(np)):
        np[pixel_id1] = (255, 0, 0)
        np.show()
    sleep(1000)
    for pixel_id2 in range(0, len(np)):
        np[pixel_id2] = (255, 165, 0)
        np.show()
    sleep(1000)
    for pixel_id3 in range(0, len(np)):
        np[pixel_id3] = (255, 255, 0)
        np.show()
    sleep(1000)
    for pixel_id4 in range(0, len(np)):
        np[pixel_id4] = (0, 255, 0)
        np.show()
    sleep(1000)
    for pixel_id5 in range(0, len(np)):
        np[pixel_id5] = (0, 0, 255)
        np.show()
    sleep(1000)
    for pixel_id6 in range(0, len(np)):
        np[pixel_id6] = (75, 0, 130)
        np.show()
    sleep(1000)
    for pixel_id7 in range(0, len(np)):
        np[pixel_id7] = (238, 130, 238)
        np.show()
    sleep(1000)
    for pixel_id8 in range(0, len(np)):
        np[pixel_id8] = (160, 32, 240)
        np.show()
    sleep(1000)
    for pixel_id9 in range(0, len(np)):
        np[pixel_id9] = (255, 255, 255)
    sleep(1000)
```

Si le code est correct, connectez le micro:bit à votre ordinateur et cliquez sur“Flash”pour télécharger le code sur la carte micro:bit.

![](./media/Python_56a9ab63.png)

4\.  **Résultat du Test1**

Après avoir téléchargé le code sur la carte avec succès, **alimentation externe (mettre l'interrupteur DIP sur ON)**, et appuyez sur le bouton de réinitialisation du micro:bit.

![Img](./media/Python_bb3e1312.png)

Les 4 LED WS2812RGB s'allument tour à tour en différentes couleurs de manière cyclique.

5\.  **Test Code2**

Lancez le logiciel Mu et ouvrez le fichier“4 WS2812 RGB LEDs-2\.py”pour importer le code. Vous pouvez aussi saisir le code vous-même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles en anglais doivent être écrits en anglais**.)

Cliquez sur“Check”pour vérifier les erreurs dans le code. Le programme est incorrect si des soulignements et des curseurs apparaissent. 

Si le code est correct, connectez le micro:bit à votre ordinateur et cliquez sur“Flash”pour télécharger le code sur la carte micro:bit.

![](./media/Python_8cb1dd7c.png)

```python
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin7, 4)
while True:
    for index in range(0, 4):
        np.clear()
        np[index] = (255, 0, 0)
        np.show()
        sleep(100)
    for index1 in range(0, 4):
        np.clear()
        np[index1] = (255, 165, 0)
        np.show()
        sleep(100)
    for index2 in range(0, 4):
        np.clear()
        np[index2] = (255, 255, 0)
        np.show()
        sleep(100)
    for index3 in range(0, 4):
        np.clear()
        np[index3] = (0, 255, 0)
        np.show()
        sleep(100)
    for index4 in range(0, 4):
        np.clear()
        np[index4] = (0, 0, 255)
        np.show()
        sleep(100)
    for index5 in range(0, 4):
        np.clear()
        np[index5] = (75, 0, 130)
        np.show()
        sleep(100)
    for index6 in range(0, 4):
        np.clear()
        np[index6] = (238, 130, 238)
        np.show()
        sleep(100)
    for index7 in range(0, 4):
        np.clear()
        np[index7] = (160, 32, 240)
        np.show()
        sleep(100)
    for index8 in range(0, 4):
        np.clear()
        np[index8] = (255, 255, 255)
        np.show()
        sleep(100)
```

6\.  **Résultat du Test2**

Après avoir téléchargé le code sur la carte avec succès, **alimentation externe (mettre l'interrupteur DIP sur ON)**, et appuyez sur le bouton de réinitialisation du micro:bit.

![Img](./media/Python_bb3e1312.png)

Les LED WS2812RGB affichent un effet de lumière défilante.

7\.  **Test Code3**

Lancez le logiciel Mu et ouvrez le fichier“4 WS2812 RGB LEDs-3\.py”pour importer le code. Vous pouvez aussi saisir le code vous-même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles en anglais doivent être écrits en anglais.**)

Cliquez sur“Check”pour vérifier les erreurs dans le code. Le programme est incorrect si des soulignements et des curseurs apparaissent. 

Si le code est correct, connectez le micro:bit à votre ordinateur et cliquez sur“Flash”pour télécharger le code sur la carte micro:bit.

![](./media/Python_b248f1c5.png)

```python
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin7, 4)
from random import randint
R = 0
G = 0
B = 0
while True:
   for index in range(0, 4):
        R = randint(10, 255)
        G = randint(10, 255)
        B = randint(10, 255)
        np.clear()
        np[index] = (R, G, B)
        np.show()
        sleep(500)
```

8\.  **Résultat du Test3**

Après avoir téléchargé le code sur la carte avec succès, **alimentation externe (mettre l'interrupteur DIP sur ON)**, et appuyez sur le bouton de réinitialisation du micro:bit.

![Img](./media/Python_bb3e1312.png)

Chaque LED WS2812RGB affiche une couleur aléatoire, une par une.

5\.  **Explication du code**

![Img](./media/Python_d1e3977b.png)

---