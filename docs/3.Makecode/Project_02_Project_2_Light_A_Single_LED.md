## Project 2: Light A Single LED

![](./media/Makecode_2423afc6.jpg)

[Klicken Sie hier, um den Code für diese Lektion herunterzuladen](./Code/Light-A-Single-LED.hex)

### (1)Projektbeschreibung:

(1)Projektbeschreibung: Die LED-Punktmatrix besteht aus 25 LEDs, angeordnet in einem 5 × 5-Quadrat. Um die LEDs schnell zu lokalisieren, können wir diese Matrix, wie in der untenstehenden Abbildung gezeigt, als Koordinatensystem betrachten und zwei Achsen erstellen, indem wir die Zeilen von 0 bis 4 von oben nach unten und die Spalten von 0 bis 4 von links nach rechts nummerieren. Daher befindet sich die LED in der zweiten Position der ersten Zeile bei (1,0) und die LED in der fünften Position der vierten Spalte bei (3,4), ebenso für die anderen.

![](./media/Makecode_4ab9ecab.png)

### (2)Benötigte Komponenten:

Micro:bit main board V2

Micro USB-Kabel

### (3)Testcode:

Schließen Sie das Micro:bit main board V2 mit dem Micro USB-Kabel an Ihren Computer an und beginnen Sie mit dem Bearbeiten.

![](./media/Makecode_1bbd8a3b.gif)

Vollständiges Programm:

![](./media/Makecode_da248db5.png)

### (4)Testergebnisse

Nachdem Sie den Code hochgeladen haben, zeigt das Micro:bit-Board folgende Anzeige: (1,0) leuchtet 0,5 Sekunden lang auf und erlischt dann, gefolgt von (3,4), das ebenfalls 0,5 Sekunden lang leuchtet und dann erlischt. Dieser Ablauf wiederholt sich in einer Schleife.

![](./media/Makecode_301232e3.gif)