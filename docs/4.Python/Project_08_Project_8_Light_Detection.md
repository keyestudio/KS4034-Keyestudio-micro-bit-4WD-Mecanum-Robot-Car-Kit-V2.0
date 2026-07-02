### Projet 8：Détection de la lumière

![](./media/Python_b855274f.png)

1\.  **Description**

Dans ce projet, nous nous concentrerons sur la fonction de détection de la lumière de la carte principale Micro: Bit. Cela est réalisé par la LED dot matrix car la carte principale n'est pas équipée d'une photorésistance.

2\.  **Préparation**

A. Branchez le micro:bit main board à votre ordinateur via le câble USB

B. Ouvrez la version hors ligne de Mu.

3\.  **Code de test**

Lancez le logiciel Mu et ouvrez le fichier “Detect Light Intensity by Microbit\.py” pour importer le code. Vous pouvez également saisir le code vous-même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles en anglais doivent être écrits en anglais.**)

![](./media/Python_b4f06503.png)

```python
from microbit import *

while True:

    Lightintensity = display.read_light_level()

    print("Light intensity:", Lightintensity)

    sleep(100)
```
Cliquez sur “Check” pour vérifier les erreurs dans le code. Le programme est erroné si des soulignements et des curseurs sont affichés.

![](./media/Python_b41eeb0f.png)

Si le code est correct, connectez le micro:bit à votre ordinateur et cliquez sur “Flash” pour télécharger le code sur la carte micro:bit.

![](./media/Python_7baa2190.png)

4\.  **Résultat du test**

Après avoir téléchargé le code sur la carte avec succès, **alimentez via le câble micro USB ou une alimentation externe (turn the DIP switch to ON)**. Cliquez sur “REPL” et appuyez sur le bouton de réinitialisation du micro:bit.

![Img](./media/Python_bb3e1312.png)

Ensuite, la fenêtre REPL affichera la valeur de l'intensité lumineuse, comme indiqué ci-dessous.

Lorsque la LED dot matrix est couverte par la main, l'intensité lumineuse indiquée est d'environ 0 ; lorsque la LED dot matrix est exposée à la lumière, l'intensité lumineuse affichée augmente avec l'intensité lumineuse.

![](./media/Python_778d89d6.png)

5\.  **Explication du code**

![Img](./media/Python_dcdc4536.png)

---