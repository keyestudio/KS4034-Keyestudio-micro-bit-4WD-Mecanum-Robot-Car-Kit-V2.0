### Projet 9 : Haut-parleur

![](./media/Python_ac515b9a.png)

1\.  **Description**

La carte principale micro:bit possède un haut-parleur intégré, ce qui facilite l'ajout de son aux programmes. Elle peut également être programmée pour produire toutes sortes de tonalités, comme jouer la chanson *Ode to Joy*.

2\.  **Préparation**

A. Connectez la carte principale micro:bit à votre ordinateur via le câble USB

B. Ouvrez la version hors ligne de Mu.

3\.  **Code de test**

Ouvrez le logiciel Mu et ouvrez le fichier “Speaker\.py” pour importer le code. Vous pouvez également saisir le code vous-même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles doivent être écrits en anglais**.)

![](./media/Python_eec7f643.png)

```python
from microbit import *

import audio

display.show(Image.MUSIC_QUAVER)

while True:
    audio.play(Sound.GIGGLE)
    sleep(1000)
    audio.play(Sound.HAPPY)
    sleep(1000)
    audio.play(Sound.HELLO)
    sleep(1000)
    audio.play(Sound.YAWN)
    sleep(1000)
```

Cliquez sur “Check” pour vérifier les erreurs dans le code. Le programme est incorrect si des soulignements et des curseurs sont affichés.

![](./media/Python_f8852abf.png)

Si le code est correct, connectez le micro:bit à votre ordinateur et cliquez sur “Flash” pour télécharger le code sur la carte micro:bit.

![](./media/Python_3fd94e43.png)

4\.  **Résultat du test**

Après avoir téléchargé le code sur la carte avec succès, **alimentez via le câble micro USB ou une alimentation externe (mettez l'interrupteur DIP sur ON)**, puis appuyez sur le bouton de réinitialisation du micro:bit.

![Img](./media/Python_bb3e1312.png)

 Le haut-parleur émet un son et la matrice de LED affiche le symbole de la musique.

5\.  **Explication du code**

![Img](./media/Python_18c047bd.png)

---