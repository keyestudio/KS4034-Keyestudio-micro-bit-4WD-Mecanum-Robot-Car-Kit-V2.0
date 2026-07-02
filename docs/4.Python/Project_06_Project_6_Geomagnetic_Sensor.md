### Projet 6：Geomagnetic Sensor

![](./media/Python_26d107ae.png)

1\.  **Description**

Ce projet présente principalement l’utilisation du capteur géomagnétique du micro:bit. En plus de détecter l’intensité du champ magnétique, il peut également servir à déterminer la direction, ce qui constitue une partie importante du système de référence d’orientation (AHRS).

Il utilise le magnétomètre triaxial FreescaleMAG3110. Son interface I2C communique avec l’extérieur, la plage est ±1000µT et la fréquence maximale de mise à jour des données est de 80Hz. Combiné avec un accéléromètre, il peut calculer la position. De plus, il est utilisé pour la détection magnétique et les blocs boussole.

Ensuite, nous pouvons lire la valeur détectée par celui-ci pour déterminer la position. Il est nécessaire d’étalonner (calibrer) la carte micro:bit lorsque le capteur magnétique fonctionne. La méthode correcte de calibration consiste à faire tourner la carte micro:bit.

De plus, les objets à proximité peuvent affecter la précision des relevés et de la calibration.

2\.  **Préparation**

A. Connectez la carte principale micro:bit à votre ordinateur via le câble USB

B. Ouvrez la version hors ligne de Mu.

3\.  **Test Code1**

Lancez le logiciel Mu et ouvrez le fichier “Magnetic sensor -1\.py” pour importer le code. Vous pouvez aussi saisir le code directement dans la fenêtre d’édition.

(**Remarque : Tous les mots et symboles doivent être écrits en anglais**.)

![](./media/Python_1366c5ed.png)

```python
from microbit import *

compass.calibrate()

while True:

    if button_a.is_pressed():
        display.scroll(compass.heading())
```
Cliquez sur “Check” pour vérifier les erreurs dans le code. Le programme est incorrect si des soulignements et des curseurs sont affichés. 

![](./media/Python_5bfe40c4.png)

Si le code est correct, connectez le micro:bit à l’ordinateur et cliquez sur “Flash” pour transférer le code sur la carte micro:bit.

![](./media/Python_695d8f29.png)

4\.  **Résultat du test1**

Après avoir téléchargé le code sur la carte avec succès, **mettez sous tension via le câble micro USB ou une alimentation externe (positionnez l’interrupteur DIP sur ON)**, puis appuyez sur le bouton Reset du micro:bit.

![Img](./media/Python_bb3e1312.png)

 La matrice de LED affiche “TILT TO FILL SCREEN”. En appuyant sur le bouton A, la carte demande de calibrer la boussole. Ensuite, entrez dans la page de calibration. Faites tourner la carte jusqu’à ce que les 25 LED rouges soient allumées, comme montré ci‑dessous.

![](./media/Python_c8fd6670.jpg)

Après cela, un motif sourire ![](./media/Python_a3b91e3e.png) apparaît, ce qui implique que la calibration est terminée. Lorsque le processus de calibration est terminé, l’appui sur le bouton A affichera directement la lecture du magnétomètre sur l’écran. Les directions nord, est, sud et ouest correspondent respectivement à 0°, 90°, 180° et 270°.

5\.  **Test Code2**

Pour l’image ci‑dessous, la flèche pointera vers le haut à droite lorsque la valeur est comprise entre 292,5 et 337,5. Comme 0,5 ne peut pas être entré dans le code, les valeurs que nous utilisons sont 293 et 338.

Ajoutez ensuite d’autres instructions pour constituer un code complet.

![](./media/Python_d1a4e9f6.png)

Lancez le logiciel Mu et ouvrez le fichier “Magnetic sensor -2\.py” pour importer le code. Vous pouvez aussi saisir le code directement dans la fenêtre d’édition.

(**Remarque : Tous les mots et symboles doivent être écrits en anglais.**)

![](./media/Python_5b0d8e26.png)

```python
from microbit import *
compass.calibrate()
x = 0
while True:
    x = compass.heading()
    if x >= 293 and x < 338:
        display.show(Image("00999:""00099:""00909:""09000:""90000"))
    elif x >= 23 and x < 68:
        display.show(Image("99900:""99000:""90900:""00090:""00009"))
    elif x >= 68 and x < 113:
        display.show(Image("00900:""09000:""99999:""09000:""00900"))
    elif x >= 113 and x < 158:
        display.show(Image("00009:""00090:""90900:""99000:""99900"))
    elif x >= 158 and x < 203:
        display.show(Image("00900:""00900:""90909:""09990:""00900"))
    elif x >= 203 and x < 248:
        display.show(Image("90000:""09000:""00909:""00099:""00999"))
    elif x >= 248 and x < 293:
        display.show(Image("00900:""00090:""99999:""00090:""00900"))
    else:
        display.show(Image("00900:""09990:""90909:""00900:""00900"))

```

Cliquez sur “Check” pour vérifier les erreurs dans le code. Le programme est incorrect si des soulignements et des curseurs sont affichés. 

![](./media/Python_42389bcf.png)

Si le code est correct, connectez le micro:bit à votre ordinateur et cliquez sur “Flash” pour transférer le code sur la carte micro:bit.

![](./media/Python_bedc607a.png)

6\.  **Résultat du test**

Après avoir téléchargé le code sur la carte avec succès, **mettez sous tension via le câble micro USB ou une alimentation externe (positionnez l’interrupteur DIP sur ON)**, puis appuyez sur le bouton Reset du micro:bit.

![Img](./media/Python_bb3e1312.png)

Après la calibration, faites tourner la carte micro:bit, puis la matrice de LED affiche les indicateurs de direction. 

7\.  **Explication du code**

![Img](./media/Python_76f66bb0.png)

---