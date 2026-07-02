### Projet 13: LED septicolore

![](./media/Python_804e502b.png)

1\.  **Description**

Ce module est composé d'une LED couramment utilisée à 7 couleurs mais d'apparence blanche. Elle peut clignoter automatiquement différentes couleurs pour créer des effets lumineux fantastiques lorsqu'un niveau haut est appliqué, comme pour une LED normale.

2\.  **Préparation**

- Insérez la carte micro:bit dans la fente du keyestudio 4WD Mecanum Robot Car V2.0

- Placez les piles dans le porte-piles

- Tournez l'interrupteur d'alimentation sur la position ON

- Connectez le micro:bit à votre ordinateur via un câble USB

- Ouvrez la version hors ligne de Mu.

3\.  **Code de test**

Ouvrez le logiciel Mu et ouvrez le fichier“Colorful lights\.py”pour importer le code. Vous pouvez également saisir le code vous-même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles doivent être écrits en anglais**.)

![](./media/Python_010a8a12.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *

mecanumCar = Mecanum_Car_Driver_V2()

while True:
    mecanumCar.left_led(1)
    mecanumCar.right_led(1)
    sleep(3000)
    mecanumCar.left_led(0)
    mecanumCar.right_led(0)
    sleep(3000)
```

**Avis important :** Si le fichier de bibliothèque 'keyes_mecanum_Car_V2.py' n'a pas encore été importé sur la carte micro:bit, il est essentiel d'importer d'abord le fichier de bibliothèque sur la carte micro:bit. La méthode d'importation de la bibliothèque se trouve en cliquant sur le lien : [How to Import Library to Micro:bit](https://docs.keyestudio.com/projects/KS4034/en/latest/docs/Python/Python.html#how-mu-import-library-to-micro-bit) et en suivant les instructions fournies ; autrement, le code ne s'exécutera pas.

Après l'importation réussie du fichier de bibliothèque, vous devez également cliquer sur le bouton "Check" pour vérifier le code. Si un curseur ou un soulignement apparaît sur une certaine ligne, alors des erreurs sont présentes dans le programme.

![](./media/Python_ce67f468.png)

Cependant, durant ce processus, l'invite suivante apparaîtra même s'il n'y a pas d'erreur dans le code. Ces invites sont simplement des avertissements et non des messages d'erreur de code.

![](./media/Python_863bb61b.png)

![](./media/Python_ccfbfa56.png)

Si le code est correct, connectez le micro:bit à votre ordinateur et cliquez sur“Flash”pour télécharger le code sur la carte micro:bit.

![](./media/Python_39512a13.png)

Si des erreurs apparaissent après avoir cliqué sur le bouton "Flash", veuillez confirmer si vous avez importé le fichier de bibliothèque fourni "keyes_mecanum_Car_V2.py".

**Remarque :** Avant de programmer avec Micropython, vous devez importer le fichier de bibliothèque "keyes_mecanum_Car_V2.py" dans le micro:bit. Si vous programmez avec un autre micro:bit, le fichier de bibliothèque "keyes_mecanum_Car_V2.py" doit être importé à nouveau sur le nouveau micro:bit.

4\. **Résultat du test**

Après avoir téléchargé le code sur la carte avec succès, **alimentation externe (mettre l'interrupteur DIP sur ON)**, et appuyez sur le bouton de réinitialisation du micro:bit.

![Img](./media/Python_bb3e1312.png)

La LED septicolore clignotera pendant 3s puis s'arrêtera pendant 3s et répétera ce motif.

5\. **Explication du code**

![Img](./media/Python_a4a670c0.png)