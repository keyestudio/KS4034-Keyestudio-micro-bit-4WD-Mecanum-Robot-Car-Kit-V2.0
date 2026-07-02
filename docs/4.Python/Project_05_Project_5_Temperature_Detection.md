### Projet 5：Détection de la température

1\.  **Description**

La carte principale Micro:bit n'est pas équipée d'un capteur de température, mais utilise le capteur de température intégré dans la puce NFR52833 pour la détection de la température. Par conséquent, la température détectée est plus proche de la température de la puce et peut présenter un écart par rapport à la température ambiante.

Dans ce projet, nous allons utiliser le capteur pour tester la température de l'environnement courant et afficher les résultats de la mesure sur le dispositif d'affichage. Ensuite, nous contrôlerons la matrice de LED afin d'afficher différents motifs en fonction de la plage de température détectée par le capteur.

**Remarque : le capteur de température de la carte principale Micro:bit est illustré ci‑dessous :**

![](./media/Python_206c8ec1.png)

2\.  **Préparation**

A. Connectez la carte principale micro:bit à votre ordinateur via le câble USB

B. Ouvrez la version hors ligne de Mu.

3\.  **Code de test1**

Ouvrez le logiciel Mu et importez le fichier “Temperature Measurement -1\.py “. Vous pouvez également saisir le code vous‑même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles doivent être écrits en anglais.**)

![](./media/Python_03cbb6e9.png)

```python
from microbit import *

while True:

    Temperature = temperature()

    print("Temperature:", Temperature, "C")

    sleep(500)
```

Cliquez sur “Check” pour vérifier la présence d'erreurs dans le code. Le programme est incorrect si des soulignements et des curseurs apparaissent. 

![](./media/Python_7b437c2d.png)

Si le code est correct, connectez le micro:bit à l'ordinateur et cliquez sur “Flash” pour transférer le code sur la carte micro:bit.

![](./media/Python_193065ab.png)

4\.  **Résultat du test1**

Après avoir téléchargé le code sur la carte avec succès, **alimentez via le câble micro USB ou une alimentation externe (placer l'interrupteur DIP sur ON)**. Cliquez sur “REPL” et appuyez sur le bouton reset du micro:bit.

![Img](./media/Python_bb3e1312.png)

La fenêtre REPL affichera alors la valeur de la température ambiante, comme indiqué ci‑dessous : (C représente l'unité de température)

![](./media/Python_d08386d8.png)

5\.  **Code de test2**

Ouvrez le logiciel Mu et importez le fichier “Temperature Measurement -2\.py “. Vous pouvez également saisir le code vous‑même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles doivent être écrits en anglais.**)

La valeur de température peut être définie en conformité avec la température réelle.

![](./media/Python_c6456d78.png)

```python
from microbit import *

while True:

    if temperature() >= 35:
        display.show(Image.HEART)

    else:
        display.show(Image.HEART_SMALL)
```

Cliquez sur “Check” pour vérifier la présence d'erreurs dans le code. Le programme est incorrect si des soulignements et des curseurs apparaissent. 

![](./media/Python_709d3031.png)

Si le code est correct, connectez le micro:bit à l'ordinateur et cliquez sur “Flash” pour transférer le code sur la carte micro:bit.

![](./media/Python_06f7542e.png)

6\.  **Résultat du test2**

Après avoir téléchargé le code sur la carte avec succès, **alimentez via le câble micro USB ou une alimentation externe (placer l'interrupteur DIP sur ON)**, puis appuyez sur le bouton reset du micro:bit.

![Img](./media/Python_bb3e1312.png)

Lorsque la température ambiante est inférieure à 35℃, la matrice de LED 5×5 affiche ![](./media/Python_034dc0d5.png). Lorsque la température est égale ou supérieure à 35℃, le motif ![](./media/Python_ebfaeac9.png) apparaît.

7\.  **Explication du code**

![Img](./media/Python_d7cdc397.png)

---