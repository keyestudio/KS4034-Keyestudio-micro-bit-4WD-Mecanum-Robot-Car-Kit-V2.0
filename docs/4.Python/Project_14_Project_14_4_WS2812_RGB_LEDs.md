### Projekt 14: 4 WS2812 RGB LEDs

![](./media/Python_eecf79fe.png)

1\.  **Beschreibung**

Das Treiber-Shield unterstützt 4 Stück WS2812 RGB-LEDs, ist mit dem micro:bit kompatibel und wird über P7 gesteuert. In dieser Lektion lassen wir die RGB-LEDs über P7 verschiedene Farben anzeigen. Es werden drei Sätze Testcode bereitgestellt, mit denen die 4 WS2812 RGB-LEDs unterschiedliche Effekte anzeigen können.

![Img](./media/Python_0be70eda.png)

2\.  **Vorbereitung**

- Setzen Sie das micro:bit-Board in den Steckplatz des keyestudio 4WD Mecanum Robot Car V2.0 ein

- Legen Sie die Batterien in den Batteriehalter

- Schalten Sie den Netzschalter auf die ON-Position

- Verbinden Sie das micro:bit über ein USB-Kabel mit Ihrem Computer

- Öffnen Sie die Offline-Version von Mu.

3\.  **Test Code1**

Starten Sie die Mu-Software und öffnen Sie die Datei“4 WS2812 RGB LEDs-1\.py”um den Code zu importieren\ Sie können den Code auch selbst im Bearbeitungsfenster eingeben.

(**Hinweis: Alle englischen Wörter und Symbole müssen in Englisch geschrieben werden.**)

Klicken Sie auf“Check”um Fehler im Code zu prüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden. 

![](./media/Python_5b5266e2.png)

```python
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin7, 4)
while True:
    for pixel_id1 in range(0, len(np)):
        np[pixel_id1] = (255, 0, 0)
        np.show()
    sleep(1000)
    for pixel_id2 in range(0, len(np)):
        np[pixel_id2] = (255, 165, 0)
        np.show()
    sleep(1000)
    for pixel_id3 in range(0, len(np)):
        np[pixel_id3] = (255, 255, 0)
        np.show()
    sleep(1000)
    for pixel_id4 in range(0, len(np)):
        np[pixel_id4] = (0, 255, 0)
        np.show()
    sleep(1000)
    for pixel_id5 in range(0, len(np)):
        np[pixel_id5] = (0, 0, 255)
        np.show()
    sleep(1000)
    for pixel_id6 in range(0, len(np)):
        np[pixel_id6] = (75, 0, 130)
        np.show()
    sleep(1000)
    for pixel_id7 in range(0, len(np)):
        np[pixel_id7] = (238, 130, 238)
        np.show()
    sleep(1000)
    for pixel_id8 in range(0, len(np)):
        np[pixel_id8] = (160, 32, 240)
        np.show()
    sleep(1000)
    for pixel_id9 in range(0, len(np)):
        np[pixel_id9] = (255, 255, 255)
    sleep(1000)
```

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit Ihrem Computer und klicken Sie auf“Flash”um den Code auf das micro:bit-Board zu übertragen.

![](./media/Python_56a9ab63.png)

4\.  **Testergebnis1**

Nachdem der Code erfolgreich auf das Board geladen wurde, **externe Stromversorgung (DIP-Schalter auf ON stellen)** und drücken Sie die Reset-Taste am micro:bit.

![Img](./media/Python_bb3e1312.png)

Die 4 WS2812RGB-LEDs leuchten nacheinander zyklisch in unterschiedlichen Farben.

5\.  **Test Code2**

Starten Sie die Mu-Software und öffnen Sie die Datei“4 WS2812 RGB LEDs-2\.py”um den Code zu importieren. Sie können den Code auch selbst im Bearbeitungsfenster eingeben.

(**Hinweis: Alle englischen Wörter und Symbole müssen in Englisch geschrieben werden**.)

Klicken Sie auf“Check”um Fehler im Code zu prüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden. 

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit Ihrem Computer und klicken Sie auf“Flash”um den Code auf das micro:bit-Board zu übertragen.

![](./media/Python_8cb1dd7c.png)

```python
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin7, 4)
while True:
    for index in range(0, 4):
        np.clear()
        np[index] = (255, 0, 0)
        np.show()
        sleep(100)
    for index1 in range(0, 4):
        np.clear()
        np[index1] = (255, 165, 0)
        np.show()
        sleep(100)
    for index2 in range(0, 4):
        np.clear()
        np[index2] = (255, 255, 0)
        np.show()
        sleep(100)
    for index3 in range(0, 4):
        np.clear()
        np[index3] = (0, 255, 0)
        np.show()
        sleep(100)
    for index4 in range(0, 4):
        np.clear()
        np[index4] = (0, 0, 255)
        np.show()
        sleep(100)
    for index5 in range(0, 4):
        np.clear()
        np[index5] = (75, 0, 130)
        np.show()
        sleep(100)
    for index6 in range(0, 4):
        np.clear()
        np[index6] = (238, 130, 238)
        np.show()
        sleep(100)
    for index7 in range(0, 4):
        np.clear()
        np[index7] = (160, 32, 240)
        np.show()
        sleep(100)
    for index8 in range(0, 4):
        np.clear()
        np[index8] = (255, 255, 255)
        np.show()
        sleep(100)
```

6\.  **Testergebnis2**

Nachdem der Code erfolgreich auf das Board geladen wurde, **externe Stromversorgung (DIP-Schalter auf ON stellen)** und drücken Sie die Reset-Taste am micro:bit.

![Img](./media/Python_bb3e1312.png)

Die WS2812RGB-LEDs zeigen einen Lauflichteffekt.

7\.  **Test Code3**

Starten Sie die Mu-Software und öffnen Sie die Datei“4 WS2812 RGB LEDs-3\.py”um den Code zu importieren. Sie können den Code auch selbst im Bearbeitungsfenster eingeben.

(**Hinweis: Alle englischen Wörter und Symbole müssen in Englisch geschrieben werden.**)

Klicken Sie auf“Check”um Fehler im Code zu prüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden. 

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit Ihrem Computer und klicken Sie auf“Flash”um den Code auf das micro:bit-Board zu übertragen.

![](./media/Python_b248f1c5.png)

```python
from microbit import *
import neopixel
np = neopixel.NeoPixel(pin7, 4)
from random import randint
R = 0
G = 0
B = 0
while True:
   for index in range(0, 4):
        R = randint(10, 255)
        G = randint(10, 255)
        B = randint(10, 255)
        np.clear()
        np[index] = (R, G, B)
        np.show()
        sleep(500)
```

8\.  **Testergebnis3**

Nachdem der Code erfolgreich auf das Board geladen wurde, **externe Stromversorgung (DIP-Schalter auf ON stellen)** und drücken Sie die Reset-Taste am micro:bit.

![Img](./media/Python_bb3e1312.png)

Jede WS2812RGB-LED zeigt nacheinander eine zufällige Farbe.

5\.  **Code-Erklärung**

![Img](./media/Python_d1e3977b.png)

---