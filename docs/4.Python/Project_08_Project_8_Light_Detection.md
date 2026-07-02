### Projekt 8：Lichtdetektion

![](./media/Python_b855274f.png)

1\.  **Beschreibung**

In diesem Projekt konzentrieren wir uns auf die Lichtdetektionsfunktion des micro:bit main board. Diese wird über die LED dot matrix realisiert, da das main board nicht mit einem Fotowiderstand ausgestattet ist.

2\.  **Vorbereitung**

A. Verbinden Sie das micro:bit main board über das USB-Kabel mit Ihrem Computer.

B. Öffnen Sie die Offline-Version von Mu.

3\.  **Testcode**

Starten Sie die Mu-Software und öffnen Sie die Datei “Detect Light Intensity by Microbit\.py”, um den Code zu importieren. Sie können den Code auch selbst in das Editorfenster eingeben.

(**Hinweis: Alle englischen Wörter und Symbole müssen in englischer Sprache geschrieben sein.**)

![](./media/Python_b4f06503.png)

```python
from microbit import *

while True:

    Lightintensity = display.read_light_level()

    print("Light intensity:", Lightintensity)

    sleep(100)
```
Klicken Sie auf “Check”, um Fehler im Code zu überprüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden.

![](./media/Python_b41eeb0f.png)

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit Ihrem Computer und klicken Sie auf “Flash”, um den Code auf das micro:bit board zu übertragen.

![](./media/Python_7baa2190.png)

4\.  **Testergebnis**

Nachdem der Code erfolgreich auf das Board heruntergeladen wurde, **schalten Sie die Stromversorgung über das Micro-USB-Kabel oder eine externe Stromquelle ein (turn the DIP switch to ON)**. Klicken Sie auf “REPL” und drücken Sie die Reset-Taste am micro:bit.

![Img](./media/Python_bb3e1312.png)

Im REPL-Fenster wird dann der Wert der Lichtintensität angezeigt, wie unten zu sehen.

Wenn die LED dot matrix mit der Hand abgedeckt wird, zeigt die Lichtintensität etwa 0 an; wenn die LED dot matrix dem Licht ausgesetzt ist, wird der angezeigte Lichtintensitätswert mit zunehmendem Licht stärker.

![](./media/Python_778d89d6.png)

5\.  **Code-Erklärung**

![Img](./media/Python_dcdc4536.png)

---