## Projekt 6: Geomagnetischer Sensor

[Klicken Sie hier, um den Code 1 für diese Lektion herunterzuladen](./Code/Geomagnetic-Sensor.hex)

[Klicken Sie hier, um den Code 2 für diese Lektion herunterzuladen](./Code/Geomagnetic-Sensor2.hex)

### (1)Projektbeschreibung:

(1) Projektbeschreibung: Dieses Projekt erklärt die Verwendung des Micro:bit-Geomagnetfeldsensors, der nicht nur die Stärke des geomagnetischen Feldes erkennen, sondern auch als Kompass zur Ermittlung von Richtungen verwendet werden kann. Er ist außerdem ein wichtiger Bestandteil des Attitude and Heading Reference System (AHRS). Das Micro:bit main board V2 verwendet den LSM303AGR-Geomagnetfeldsensor, und der Dynamikbereich des Magnetfeldes beträgt ± 50 Gauss. Auf dem Board wird das Magnetometer-Modul sowohl zur Magnetfeldmessung als auch als Kompass eingesetzt. In diesem Experiment wird zunächst der Kompass vorgestellt und anschließend die Rohdaten des Magnetometers überprüft. Die Hauptkomponente eines herkömmlichen Kompasses ist eine Magnetnadel, die vom geomagnetischen Feld gedreht werden kann und zur Bestimmung der Richtung zum geomagnetischen Nordpol (der in der Nähe des geografischen Südpols liegt) zeigt.

### (2)Benötigte Komponenten:

Micro:bit main board V2

 Micro USB-Kabel

### (3)Testcode 1 :

Verbinden Sie den Computer mit dem Micro:bit-Board über ein Micro-USB-Kabel und programmieren Sie im MakeCode-Editor.

![](./media/Makecode_5805c7de.gif)

Vollständiges Programm :

![](./media/Makecode_5a958132.png)

### (4)Testergebnisse 1 :

Nachdem der Testcode auf das Micro:bit main board V2 hochgeladen und das Board über das USB-Kabel mit Strom versorgt wurde, und nach dem Drücken der Taste A fordert das Board zur Kalibrierung des Kompasses auf und die LED-Punktmatrix zeigt "TILT TO FILL SCREEN" an. Dann gelangt man zur Kalibrierungsseite. Drehen Sie das Board, bis alle 25 LEDs wie unten gezeigt rot leuchten.

![](./media/Makecode_b0a4ebf1.jpg)

Kompass kalibrieren:

![](./media/Makecode_05a88e21.gif)

Danach erscheint ein Smiley-Muster ![](./media/Makecode_74a69436.png), was darauf hinweist, dass die Kalibrierung abgeschlossen ist. Wenn der Kalibrierungsprozess abgeschlossen ist, zeigt ein Druck auf die Taste A die Magnetometer-Messwerte direkt auf dem Bildschirm an. Und die Richtungen Norden, Osten, Süden und Westen entsprechen jeweils 0°, 90°, 180° und 270°.

![](./media/Makecode_23b07bfb.gif)

### (5) Testcode 2:

Dieses Modul kann weiterhin Daten lesen, um die Richtung zu bestimmen, und zeigt daher mit einem Pfeil auf den aktuellen magnetischen Nordpol.

Verbinden Sie den Computer mit dem Micro:bit-Board über ein Micro-USB-Kabel und programmieren Sie im MakeCode-Editor,

![](./media/Makecode_db8b2d7e.gif)

Vollständiges Programm :

![](./media/Makecode_ef823069.png)

### (6) Testergebnisse 2

Laden Sie Code 2 hoch. Nach der Kalibrierung neigen Sie das Micro:bit-Board, und die LED-Punktmatrix zeigt die Richtungssymbole an.

![](./media/Makecode_d8944d5f.gif)

---