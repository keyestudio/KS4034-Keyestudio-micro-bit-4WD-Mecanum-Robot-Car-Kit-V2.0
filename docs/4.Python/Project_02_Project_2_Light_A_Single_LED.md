### Projekt 2：Eine einzelne LED zum Leuchten bringen

![](./media/Python_b855274f.png)

1\.  **Beschreibung**

Die LED-Punktmatrix besteht aus 25 Dioden, die in einem 5 × 5-Quadrat angeordnet und an den Kreuzungspunkten der Zeilenleitungen (X) und Spaltenleitungen (Y) platziert sind. Wir können eine der 25 LEDs durch Festlegen von Koordinaten ansteuern. Zum Beispiel befindet sich die erste LED in der ersten Zeile bei (0,0) und die dritte LED in der ersten Zeile bei (2,0) und so weiter.

![](./media/Python_094d5908.png)

2\.  **Vorbereitung**

A. Schließen Sie das micro:bit-Hauptboard mit dem USB-Kabel an Ihren Computer an.

B. Öffnen Sie die Offline-Version von Mu.

3\.  **Testcode**

Starten Sie die Mu-Software und öffnen Sie die Datei “Single LED display\.py.”, um den Code zu importieren. Sie können den Code auch selbst im Editorfenster eingeben.

(**Hinweis: Alle englischen Wörter und Symbole müssen auf Englisch geschrieben werden**)

![](./media/Python_9545233e.png)

```python
from microbit import *

val1 = Image("09000:""00000:""00000:""00000:""00000:")
val2 = Image("00000:""00000:""00000:""00000:""00090:")
val3 = Image("00000:""00000:""00000:""00000:""00000:")

while True:
    display.show(val1)
    sleep(500)
    display.show(val3)
    sleep(500)
    display.show(val2)
    sleep(500)
    display.show(val3)
    sleep(500)

```

Klicken Sie auf “Check”, um den Code auf Fehler zu prüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden.

![](./media/Python_d205be08.png)

Ist der Code korrekt, verbinden Sie das micro:bit mit Ihrem Computer und klicken Sie auf “Flash”, um den Code auf das micro:bit-Board zu übertragen.

![](./media/Python_86dd6eea.png)

4\.  **Testergebnis**

Nachdem der Code erfolgreich auf das Board heruntergeladen wurde, **schalten Sie die Stromversorgung über das micro-USB-Kabel oder eine externe Stromversorgung ein (schalten Sie den DIP-Schalter auf ON)** und drücken Sie die Reset-Taste auf dem Board.

![Img](./media/Python_bb3e1312.png)

Die LED an (1,0) wird 0,5 s an- und ausgeschaltet, dann die LED an (3,4) ebenfalls 0,5 s an- und ausgeschaltet und dieses Sequenz wiederholt sich.

5\.  **Code-Erklärung**

![Img](./media/Python_c79b7922.png)

6\.  **Referenz**

sleep(ms) : Verzögerungszeit

Für weitere Details zur Verzögerung siehe den Link: [https://microbit-micropython.readthedocs.io/en/latest/utime.html](https://microbit-micropython.readthedocs.io/en/latest/utime.html)