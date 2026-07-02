### Projet 11 : Microphone

![](./media/Python_3073a8af.png)

![](./media/Python_7f074115.png)

1\.  **Description**

La carte principale Micro: Bit possède un microphone intégré, qui peut mesurer le volume de l'environnement ambiant. Lorsque vous applaudissez, le témoin LED du microphone s'allume. De plus, il peut mesurer l'intensité du son, vous permettant ainsi de créer une échelle de bruit ou un éclairage de type discothèque changeant au rythme de la musique.

Le microphone est placé du côté opposé au témoin LED du microphone et à proximité d'ouvertures laissant passer le son. Lorsque la carte détecte un son, le témoin LED s'allume.

2\.  **Préparation**

A. Branchez la carte principale micro:bit à votre ordinateur via le câble USB

B. Ouvrez la version hors ligne de Mu.

3\.  **Code de test1**

Ouvrez le logiciel Mu et ouvrez le fichier “Microphone-1\.py” pour importer le code. Vous pouvez également saisir le code vous-même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles doivent être écrits en anglais**.)

![](./media/Python_19b38832.png)

```python
from microbit import *

while True:
    if microphone.current_event() == SoundEvent.LOUD:
        display.show(Image.HEART)
        sleep(200)
    if microphone.current_event() == SoundEvent.QUIET:
        display.show(Image.HEART_SMALL)
```

Cliquez sur “Check” pour vérifier les erreurs dans le code. Le programme est incorrect si des soulignements et des curseurs sont affichés. 

![](./media/Python_36a669c7.png)

Si le code est correct, connectez le micro:bit à votre ordinateur et cliquez sur “Flash” pour télécharger le code sur la carte micro:bit.

![](./media/Python_0515bf32.png)

4\.  **Résultat du test1**

Après avoir téléchargé le code avec succès sur la carte, **alimentez via le câble micro USB ou une alimentation externe (positionnez l'interrupteur DIP sur ON)**, et appuyez sur le bouton de réinitialisation du micro:bit.

![Img](./media/Python_bb3e1312.png)

La matrice de LED affiche le motif “❤” lorsque vous applaudissez et le motif ![](./media/04fdfc9060943954e7938bb1a741d626.png) lorsqu'il fait silence autour.

5\.  **Code de test2**

Ouvrez le logiciel Mu et ouvrez le fichier “Microphone-2\.py” pour importer le code. Vous pouvez également saisir le code vous-même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles doivent être écrits en anglais.**)

![](./media/Python_f0e5a346.png)

```python
from microbit import *
maxSound = 0
lights = Image("11111:"
              "11111:"
              "11111:"
              "11111:"
              "11111")
# ignore first sound level reading
soundLevel = microphone.sound_level()
sleep(200)

while True:
    if button_a.is_pressed():
        display.scroll(maxSound)
    else:
        soundLevel = microphone.sound_level()
        display.show(lights * soundLevel)
        if soundLevel > maxSound:
            maxSound = soundLevel
```

Cliquez sur “Check” pour vérifier les erreurs dans le code. Le programme est incorrect si des soulignements et des curseurs sont affichés. 

![](./media/Python_d0c79871.png)

Si le code est correct, connectez le micro:bit à votre ordinateur et cliquez sur “Flash” pour télécharger le code sur la carte micro:bit.

![](./media/Python_d828b9ee.png)

6\.  **Résultat du test2**

Après avoir téléchargé le code avec succès sur la carte, **alimentez via le câble micro USB ou une alimentation externe (positionnez l'interrupteur DIP sur ON)**, et appuyez sur le bouton de réinitialisation du micro:bit.

![Img](./media/Python_bb3e1312.png)

Lorsque le bouton A est enfoncé, la matrice de LED affiche la valeur du volume maximal ( **veuillez noter que le volume maximal peut être réinitialisé via le bouton Reset de l'autre côté de la carte** ). Lors d'un applaudissement, plus le son testé est fort, plus les 25 LED de l'écran matriciel s'illuminent.

7\.  **Explication du code**

![Img](./media/Python_980f62b3.png)