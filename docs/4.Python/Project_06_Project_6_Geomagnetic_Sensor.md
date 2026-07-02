### Project 6：Geomagnetic Sensor

![](./media/Python_26d107ae.png)

1\.  **Beschreibung**

Dieses Projekt führt hauptsächlich in die Verwendung des geomagnetischen Sensors des micro:bit ein. Neben der Messung der Stärke des Magnetfelds kann er auch zur Bestimmung der Richtung verwendet werden, was ebenfalls ein wichtiger Bestandteil eines Heading- und Attitude-Reference-Systems (AHRS) ist.

Verwendet wird der FreescaleMAG3110 Dreiachsen-Magnetometer. Seine I2C-Schnittstelle kommuniziert nach außen, der Messbereich beträgt ±1000µT, die maximale Aktualisierungsrate der Daten liegt bei 80Hz. In Kombination mit einem Beschleunigungssensor kann die Position berechnet werden. Zusätzlich wird er für Magneterkennung und Kompassmodule eingesetzt.

Anschließend können wir die von ihm erfassten Werte auslesen, um die Lage zu bestimmen. Wenn der Magnetsensor arbeitet, muss das micro:bit-Board kalibriert werden. Die korrekte Kalibrierungsmethode besteht darin, das micro:bit-Board zu drehen.

Außerdem können nahegelegene Objekte die Genauigkeit der Messwerte und der Kalibrierung beeinflussen.

2\.  **Vorbereitung**

A. Schließen Sie das micro:bit-Hauptboard mit dem USB-Kabel an Ihren Computer an

B. Öffnen Sie die Offline-Version von Mu.

3\.  **Test Code1**

Starten Sie die Mu-Software und öffnen Sie die Datei “Magnetic sensor -1\.py“, um den Code zu laden. Sie können den Code auch direkt im Bearbeitungsfenster eingeben.

(**Hinweis: Alle Wörter und Symbole müssen in Englisch geschrieben sein**.)

![](./media/Python_1366c5ed.png)

```python
from microbit import *

compass.calibrate()

while True:

    if button_a.is_pressed():
        display.scroll(compass.heading())
```
Klicken Sie auf “Check”, um den Code auf Fehler zu prüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden. 

![](./media/Python_5bfe40c4.png)

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit dem Computer und klicken Sie auf “Flash”, um den Code auf das micro:bit-Board zu übertragen.

![](./media/Python_695d8f29.png)

4\.  **Testergebnis1**

Nachdem der Code erfolgreich auf das Board geladen wurde, **schalten Sie die Stromversorgung über das Micro-USB-Kabel oder eine externe Stromversorgung ein (DIP-Schalter auf ON stellen)** und drücken Sie die Reset-Taste am micro:bit.

![Img](./media/Python_bb3e1312.png)

 Die LED-Punktmatrix zeigt “TILT TO FILL SCREEN” an. Wenn Sie die Taste A drücken, fordert das Board zur Kalibrierung des Kompasses auf. Dann gelangen Sie zur Kalibrierungsseite. Drehen Sie das Board, bis alle 25 roten LEDs leuchten, wie unten dargestellt.

![](./media/Python_c8fd6670.jpg)

Danach erscheint ein Smiley-Muster ![](./media/Python_a3b91e3e.png), das anzeigt, dass die Kalibrierung abgeschlossen ist. Wenn der Kalibrierungsvorgang beendet ist, zeigt das Drücken der Taste A die Messwerte des Magnetometers direkt auf dem Bildschirm an. Die Richtungen Norden, Osten, Süden und Westen entsprechen dabei 0°, 90°, 180° bzw. 270°.

5\.  **Test Code2**

Für das Bild unten zeigt der Pfeil nach oben rechts, wenn der Wert im Bereich von 292,5 bis 337,5 liegt. Da 0,5 nicht im Code eingegeben werden kann, verwenden wir die Werte 293 und 338.

Ergänzen Sie anschließend weitere Anweisungen, um einen vollständigen Code zu erstellen.

![](./media/Python_d1a4e9f6.png)

Starten Sie die Mu-Software und öffnen Sie die Datei “Magnetic sensor -2\.py“, um den Code zu laden. Sie können den Code auch direkt im Bearbeitungsfenster eingeben.

(**Hinweis: Alle Wörter und Symbole müssen in Englisch geschrieben sein.**)

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

Klicken Sie auf “Check”, um den Code auf Fehler zu prüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden. 

![](./media/Python_42389bcf.png)

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit Ihrem Computer und klicken Sie auf “Flash”, um den Code auf das micro:bit-Board zu übertragen.

![](./media/Python_bedc607a.png)

6\.  **Testergebnis**

Nachdem der Code erfolgreich auf das Board geladen wurde, **schalten Sie die Stromversorgung über das Micro-USB-Kabel oder eine externe Stromversorgung ein (DIP-Schalter auf ON stellen)** und drücken Sie die Reset-Taste am micro:bit.

![Img](./media/Python_bb3e1312.png)

Nach der Kalibrierung drehen Sie das micro:bit-Board, dann zeigt die LED-Punktmatrix die Richtungssymbole an. 

7\.  **Code-Erklärung**

![Img](./media/Python_76f66bb0.png)

---