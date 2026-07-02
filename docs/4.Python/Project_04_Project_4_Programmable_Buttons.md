### Projekt 4：Programmierbare Tasten

![](./media/Python_06be84fb.png)

1\.  **Beschreibung**

![](./media/Python_b6d60ae2.png)

Tasten können verwendet werden, um Schaltkreise zu steuern. In einem Bauteil mit einem Drucktaster wird der Stromkreis beim Drücken geschlossen und nach dem Loslassen wieder geöffnet.

Beide Enden der Taste sind wie zwei Berge. Dazwischen verläuft ein Fluss. 
Das interne Metallstück verbindet die beiden Seiten, sodass der Strom fließen kann, ähnlich wie eine Brücke, die zwei Berge verbindet.

Der interne Aufbau des Tasters ist wie folgt dargestellt: Vor dem Drücken sind 1, 2, 3 und 4 eingeschaltet. Allerdings sind 1 und 3 oder 1 und 4 oder 2 und 3 oder 2 und 4 getrennt; diese Verbindungen werden erst aktiviert, wenn der Taster gedrückt wird. ![](./media/Python_d2a204e6.png)

Das micro:bit-Hauptboard verfügt über drei Drucktaster: Zwei sind programmierbare Tasten (mit A und B gekennzeichnet) und die auf der anderen Seite ist eine Reset-Taste. Durch Drücken der beiden programmierbaren Tasten können drei verschiedene Signale eingegeben werden. Man kann Taste A oder B einzeln drücken oder beide zusammen; die LED-Punktmatrix zeigt dann entsprechend A, B bzw. AB an. Legen wir los.

2\.  **Vorbereitung**

A. Schließen Sie das micro:bit-Hauptboard über das USB-Kabel an Ihren Computer an.

B. Öffnen Sie die Offline-Version von Mu.

3\.  **Test Code1**

Starten Sie die Mu-Software und öffnen Sie die Datei “Programmable Buttons-1\.py”, um den Code zu laden. Sie können den Code auch selbst im Editor eingeben.

(**Hinweis: Alle Wörter und Symbole müssen in Englisch verfasst sein.**)

![](./media/Python_2637f524.png)

```python
from microbit import *

while True:
    if button_a.is_pressed():
        display.show("A")
    elif button_a.is_pressed() and button_b.is_pressed():
        display.scroll("AB")
    elif button_b.is_pressed():
        display.show("B")
```
Klicken Sie auf „Check“, um den Code auf Fehler zu prüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen oder Cursor angezeigt werden.

![](./media/Python_a0f284f3.png)

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit Ihrem Computer und klicken Sie auf „Flash“, um den Code auf das micro:bit-Board zu übertragen.

![](./media/Python_5694d3ce.png)

4\.  **Testergebnis1**

Nachdem der Code erfolgreich auf das Board heruntergeladen wurde, **schalten Sie die Stromversorgung über das Micro-USB-Kabel oder eine externe Stromversorgung ein (stellen Sie den DIP-Schalter auf ON)** und drücken Sie die Reset-Taste auf dem Board.

![Img](./media/Python_bb3e1312.png)

Die 5*5-LED-Punktmatrix zeigt „A“, wenn Taste A gedrückt wird, dann „B“, wenn Taste B gedrückt wird, und „AB“, wenn A und B gleichzeitig gedrückt werden.

5\.  **Test Code2**

Starten Sie die Mu-Software und öffnen Sie die Datei “Programmable Buttons-2\.py”, um den Code zu laden. Sie können den Code auch selbst im Editor eingeben.

(**Hinweis: Alle Wörter und Symbole müssen in Englisch verfasst sein.**)

![](./media/Python_1a1126f6.png)

![](./media/Python_94849305.png)

```python
from microbit import *
a = 0
b = 0
val1 = Image("00000:""00000:""00000:""00000:""00900")
val2 = Image("00000:""00000:""00000:""00900:""99999")
val3 = Image("00000:""00000:""00900:""99999:""99999")
val4 = Image("00000:""00900:""99999:""99999:""99999")
val5 = Image("00900:""99999:""99999:""99999:""99999")
val6 = Image("99999:""99999:""99999:""99999:""99999")
display.show(val1)

while True:
    while button_a.is_pressed() == True:
        sleep(10)
        if button_a.is_pressed() == False:
            a = a + 1
            if(a >= 5):
                a = 5
            break
    while button_b.is_pressed() == True:
        sleep(10)
        if button_b.is_pressed() == False:
            a = a - 1
            if(a <= 0):
                a = 0
            break
    if a == 0:
        display.show(val1)
    if a == 1:
        display.show(val2)
    if a == 2:
        display.show(val3)
    if a == 3:
        display.show(val4)
    if a == 4:
        display.show(val5)
    if a == 5:
        display.show(val6)
```
Klicken Sie auf „Check“, um den Code auf Fehler zu prüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen oder Cursor angezeigt werden.

![](./media/Python_21771d90.png)

![Img](./media/Python_8d257384.png)

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit Ihrem Computer und klicken Sie auf „Flash“, um den Code auf das micro:bit-Board zu übertragen.

![](./media/Python_84ba8cde.png)

![Img](./media/Python_8d257384.png)

6\.  **Testergebnis2**

Nachdem der Code erfolgreich auf das Board heruntergeladen wurde, **schalten Sie die Stromversorgung über das Micro-USB-Kabel oder eine externe Stromversorgung ein (stellen Sie den DIP-Schalter auf ON)** und drücken Sie die Reset-Taste auf dem Board.

![Img](./media/Python_bb3e1312.png)

Wenn Taste A gedrückt wird, erhöhen sich die rot leuchtenden LEDs; wenn Taste B gedrückt wird, verringern sich die rot leuchtenden LEDs.

7\.  **Code-Erklärung**

![Img](./media/Python_b33858dc.png)

![Img](./media/Python_32bd1cca.png)

---