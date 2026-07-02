### Projet 10 : Logo tactile

![](./media/Python_64469585.png)

1\.  **Description**

La carte principale micro:bit V2 est équipée d'un logo tactile doré, qui peut agir comme un composant d'entrée similaire à un bouton.

Il contient un capteur tactile capacitif qui détecte de petits changements du champ électrique lorsqu'il est pressé (ou touché), tout comme l'écran de votre téléphone ou tablette. Lorsque vous l'appuyez, le programme peut être activé.

2\.  **Préparation**

A. Connectez la carte principale micro:bit à votre ordinateur via le câble USB.

B. Ouvrez la version hors ligne de Mu.

3\.  **Code de test**

Lancez le logiciel Mu et ouvrez le fichier “Touch-sensitive Logo\.py” pour importer le code. Vous pouvez également saisir le code vous-même dans la fenêtre d'édition.

(**Remarque : Tous les mots et symboles en anglais doivent être écrits en anglais**.)

![](./media/Python_0c54cbe5.png)

```python
from microbit import *
time = 0
start = 0
running = False

while True:

    if button_a.was_pressed():
        running = True
        start = running_time()
    if button_b.was_pressed():
        if running:
            time += running_time() - start
        running = False
    if pin_logo.is_touched():
        if not running:
            display.scroll(int(time/1000))

    if running:
        display.show(Image.HEART)
        sleep(300)
        display.show(Image.HEART_SMALL)
        sleep(300)
    else:
        display.show(Image.ASLEEP)
```

**Comment fonctionne le Micro:bit ?**

A\. Le temps d'exécution est enregistré en millisecondes (ms).

B\. Lorsque vous appuyez sur le bouton A, une variable nommée start est définie sur le temps d'exécution actuel.

C\. Lorsque vous appuyez sur le bouton B, le temps de départ est soustrait du nouveau temps d'exécution pour calculer le temps écoulé depuis le démarrage du chronomètre. Cette différence est ajoutée au temps total, qui est stocké dans une variable nommée time.

D\. Si vous appuyez sur le logo doré, le programme affichera le temps total écoulé sur l'affichage LED. Il convertit le temps de millisecondes (millièmes de seconde) en secondes en divisant par 1000. Il utilise l'opérateur de division entière pour donner un résultat entier.

E\. Le programme est également contrôlé par une variable booléenne nommée running. Une variable booléenne n'a que deux valeurs : true ou false. Si "running" est "true", cela signifie que le chronomètre a démarré. Si "running" est false, cela signifie que le chronomètre n'a pas démarré ou s'est arrêté.

F\. Si "running" est true, le motif de coeur battant sera affiché sur la matrice de LED.

G\. (7) Si le chronomètre est arrêté et que "running" est false, lorsque vous appuyez sur le logo doré, il n'affichera que le temps.

H\. Si le chronomètre a été démarré et que "running" est true, il suffit de s'assurer que la variable time changera lorsque le bouton B est pressé, et le code peut également empêcher les lectures incorrectes.

Cliquez sur “Check” pour vérifier les erreurs dans le code. Le programme est incorrect si des soulignements et des curseurs sont affichés.

![](./media/Python_1766a28c.png)

Si le code est correct, connectez le micro:bit à votre ordinateur et cliquez sur “Flash” pour télécharger le code sur la carte micro:bit.

![](./media/Python_a3d6e994.png)

4\.  **Résultat du test**

Après avoir téléchargé le code sur la carte avec succès, **alimentez via le câble micro USB ou une alimentation externe (mettez l'interrupteur DIP sur ON)**, puis appuyez sur le bouton de réinitialisation du micro:bit.

![Img](./media/Python_bb3e1312.png)

Appuyez sur le bouton A pour démarrer le chronomètre. Pendant le chronométrage, le motif de coeur battant sera affiché sur la matrice de LED. Appuyez sur le bouton B pour l'arrêter ; vous pouvez démarrer et arrêter à tout moment.

Il continuera d'enregistrer le temps, comme un véritable chronomètre. Appuyez sur le logo doré à l'avant du micro:bit pour afficher le temps mesuré en secondes. Et le temps peut être réinitialisé à zéro en appuyant sur le bouton de réinitialisation à l'arrière.

---