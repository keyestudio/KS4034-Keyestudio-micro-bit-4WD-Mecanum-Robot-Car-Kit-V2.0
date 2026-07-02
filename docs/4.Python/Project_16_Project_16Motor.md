### Projet 16：Moteur

![](./media/Python_32655f47.png)

1\.  **Description**

Le Keyestudio 4WD Mecanum Robot Car est équipé de 4 moteurs CC à réduction, également appelés moteurs à engrenages, qui sont dérivés du moteur CC ordinaire. Ils disposent d'une boîte de réduction d'engrenage assortie qui fournit une vitesse plus faible mais un couple plus élevé. De plus, différents rapports de réduction de la boîte peuvent fournir différentes vitesses et couples.

Le moteur à engrenages est l'intégration d'un réducteur et d'un moteur, largement utilisé dans les industries sidérurgique et mécanique.

Le shield pilote de moteur pour micro:bit intègre une puce STC8G et une puce HR8833. Afin d'économiser les ressources des ports E/S, nous contrôlons la direction de rotation et la vitesse des 4 moteurs CC à engrenages avec la puce HR8833.

**Détails sur les puces :**

![](./media/Python_d7132b53.jpg)

Avant

![](./media/Python_4919ce3b.png)

Arrière

![](./media/Python_fbfa17f7.png)

Circuit de la puce STC8G1K08

![](./media/Python_47cdde6b.png)

Circuit du pilote moteur HR8833

2\. **Préparation**

- Insérez la carte micro:bit dans l'emplacement du Keyestudio 4WD Mecanum Robot CarV2.0

- Placez les piles dans le porte-piles

- Mettez l'interrupteur d'alimentation sur la position ON

- Connectez la micro:bit à l'ordinateur via un câble USB

- Ouvrez la version hors ligne de Mu.

3\. **Test Code1**

Entrez dans le logiciel Mu et ouvrez le fichier “microbit-Motor Driving-1\.py” pour importer le code. Vous pouvez aussi saisir le code vous-même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles en anglais doivent être écrits en anglais**.)

Cliquez sur “Files” pour importer le fichier de bibliothèque “keyes_mecanum_Car.py” sur la micro:bit. 

Cliquez sur “Check” pour vérifier les erreurs dans le code. Le programme est erroné si des soulignements et des curseurs sont affichés. 

Si le code est correct, connectez la micro:bit à votre ordinateur et cliquez sur “Flash” pour télécharger le code sur la carte micro:bit.

![](./media/Python_71476377.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()
while True:
    display.show(Image.ARROW_S)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    display.show(Image.ARROW_N)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(0, 100)
    mecanumCar.Motor_Lower_R(0, 100)
    sleep(1000)
    display.show(Image.ARROW_E)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    display.show(Image.ARROW_W)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(0, 100)
    mecanumCar.Motor_Lower_R(0, 100)
    sleep(1000)
    display.show(Image("00900:""09990:""99999:""99999:""09090"))
    mecanumCar.Motor_Upper_L(0, 0)
    mecanumCar.Motor_Lower_L(0, 0)
    mecanumCar.Motor_Upper_R(0, 0)
    mecanumCar.Motor_Lower_R(0, 0)
    sleep(1000)
```

4\. **Résultat du test 1**

Après avoir téléchargé le code sur la carte avec succès, **alimentation externe (placez l'interrupteur DIP sur ON)**, et appuyez sur le bouton reset de la micro:bit.

![Img](./media/Python_bb3e1312.png)

Ensuite, la voiture avancera pendant 1 s, reculera pendant 1 s, tournera à gauche pendant 1 s, tournera à droite pendant 1 s, tournera dans le sens antihoraire pendant 1 s, dans le sens horaire pendant 1 s, puis s'arrêtera pendant 1 s. La matrice affiche également les motifs.

5\. **Test Code2**

Entrez dans le logiciel Mu et ouvrez le fichier “microbit-Motor Driving-2\.py” pour importer le code. Vous pouvez aussi saisir le code vous-même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles en anglais doivent être écrits en anglais**.)

Cliquez sur “Files” pour importer le fichier de bibliothèque “keyes_mecanum_Car.py” sur la micro:bit. 

Cliquez sur “Check” pour vérifier les erreurs dans le code. Le programme est erroné si des soulignements et des curseurs sont affichés. 

Si le code est correct, connectez la micro:bit à votre ordinateur et cliquez sur “Flash” pour télécharger le code sur la carte micro:bit.

![](./media/Python_96230faf.png)

```python
from microbit import button_a, button_b, display, Image, sleep
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()

show_L = Image("90000:""90000:""90000:""90000:""99999")
show_O = Image("09990:""90009:""90009:""90009:""09990")
a = 0
b = 0
def run_L():
    global b
    sleep(1000)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(650)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 0)
    mecanumCar.Motor_Lower_L(0, 0)
    mecanumCar.Motor_Upper_R(0, 0)
    mecanumCar.Motor_Lower_R(0, 0)
    b = 0
def run_O():
    global b
    sleep(1000)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(620)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(620)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 100)
    mecanumCar.Motor_Lower_L(0, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(620)
    mecanumCar.Motor_Upper_L(1, 100)
    mecanumCar.Motor_Lower_L(1, 100)
    mecanumCar.Motor_Upper_R(1, 100)
    mecanumCar.Motor_Lower_R(1, 100)
    sleep(1000)
    mecanumCar.Motor_Upper_L(0, 0)
    mecanumCar.Motor_Lower_L(0, 0)
    mecanumCar.Motor_Upper_R(0, 0)
    mecanumCar.Motor_Lower_R(0, 0)
    b = 0
while True:
    if button_a.was_pressed():
        a = a + 1
        if a >= 3:
            a = 0
    if button_b.was_pressed():
        b = 1
    if (a == 1):
        display.show(show_L)
        if b == 1:
            run_L()
    elif a == 2:
        display.show(show_O)
        if b == 1:
            run_O()
```

6\. **Résultat du test 2**

Après avoir téléchargé le code sur la carte avec succès, **alimentation externe (placez l'interrupteur DIP sur ON)**, et appuyez sur le bouton reset de la micro:bit.

![Img](./media/Python_bb3e1312.png)

Lorsque les boutons A et B sont pressés pour la première fois, la micro:bit affichera “L”, la trajectoire de la voiture est en forme de “L”. Lorsqu'ils sont pressés à nouveau, “口” s'affiche sur la micro:bit, et la trajectoire de la voiture est en forme de “口”. La voiture répétera ce schéma.

7\.  **Explication du code**

![Img](./media/Python_70b4e70f.png)

![Img](./media/Python_e3250a8a.png)