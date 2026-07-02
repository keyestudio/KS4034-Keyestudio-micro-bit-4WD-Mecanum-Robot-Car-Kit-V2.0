### Projekt 5：Temperaturerkennung

1\.  **Beschreibung**

Das Micro:bit-Hauptboard ist nicht mit einem eigenen Temperatursensor ausgestattet, sondern verwendet den integrierten Temperatursensor im NFR52833-Chip zur Temperaturmessung. Daher entspricht die gemessene Temperatur eher der Temperatur des Chips und kann von der Umgebungstemperatur abweichen.

In diesem Projekt verwenden wir den Sensor, um die Temperatur in der aktuellen Umgebung zu messen und die Messergebnisse auf dem Displaygerät anzuzeigen. Anschließend steuern wir die LED-Punktmatrix, sodass durch Festlegen eines Temperaturbereichs unterschiedliche Muster angezeigt werden.

**Hinweis: Der Temperatursensor des Micro:bit-Hauptboards ist unten dargestellt:**

![](./media/Python_206c8ec1.png)

2\.  **Vorbereitung**

A. Verbinden Sie das Micro:bit-Hauptboard über das USB-Kabel mit Ihrem Computer

B. Öffnen Sie die Offline-Version von Mu.

3\.  **Testcode1**

Starten Sie die Mu-Software und öffnen Sie die Datei “Temperature Measurement -1\.py “, um den Code zu importieren. Sie können den Code auch selbst im Bearbeitungsfenster eingeben.

(**Hinweis: Alle Wörter und Symbole müssen in englischer Sprache geschrieben werden.**)

![](./media/Python_03cbb6e9.png)

```python
from microbit import *

while True:

    Temperature = temperature()

    print("Temperature:", Temperature, "C")

    sleep(500)
```

Klicken Sie auf “Check”, um den Code auf Fehler zu prüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden. 

![](./media/Python_7b437c2d.png)

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit dem Computer und klicken Sie auf “Flash”, um den Code auf das micro:bit-Board zu laden.

![](./media/Python_193065ab.png)

4\.  **Testergebnis1**

Nachdem der Code erfolgreich auf das Board heruntergeladen wurde, **schalten Sie die Stromversorgung über das Micro-USB-Kabel oder eine externe Stromquelle ein (DIP-Schalter auf ON stellen)**. Klicken Sie auf “REPL” und drücken Sie die Reset-Taste am micro:bit.

![Img](./media/Python_bb3e1312.png)

Im REPL-Fenster wird dann der Umgebungswert der Temperatur angezeigt, wie unten gezeigt: (C steht für Temperatureinheit)

![](./media/Python_d08386d8.png)

5\.  **Testcode2**

Starten Sie die Mu-Software und öffnen Sie die Datei “Temperature Measurement -2\.py “, um den Code zu importieren. Sie können den Code auch selbst im Bearbeitungsfenster eingeben.

(**Hinweis: Alle Wörter und Symbole müssen in englischer Sprache geschrieben werden.**)

Der Temperaturwert kann entsprechend der tatsächlichen Temperatur eingestellt werden.

![](./media/Python_c6456d78.png)

```python
from microbit import *

while True:

    if temperature() >= 35:
        display.show(Image.HEART)

    else:
        display.show(Image.HEART_SMALL)
```

Klicken Sie auf “Check”, um den Code auf Fehler zu prüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden. 

![](./media/Python_709d3031.png)

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit dem Computer und klicken Sie auf “Flash”, um den Code auf das micro:bit-Board zu laden.

![](./media/Python_06f7542e.png)

6\.  **Testergebnis2**

Nachdem der Code erfolgreich auf das Board heruntergeladen wurde, **schalten Sie die Stromversorgung über das Micro-USB-Kabel oder eine externe Stromquelle ein (DIP-Schalter auf ON stellen)** und drücken Sie die Reset-Taste am micro:bit.

![Img](./media/Python_bb3e1312.png)

Wenn die Umgebungstemperatur unter 35℃ liegt, zeigt die 5×5-LED-Punktmatrix ![](./media/Python_034dc0d5.png) an. Wenn die Temperatur gleich oder größer als 35℃ ist, erscheint das Muster ![](./media/Python_ebfaeac9.png).

7\.  **Code-Erklärung**

![Img](./media/Python_d7cdc397.png)

---