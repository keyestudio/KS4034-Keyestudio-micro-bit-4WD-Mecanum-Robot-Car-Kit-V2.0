### Projekt 12: Lautsprecher steuern

1\.  **Beschreibung**

In den vorherigen Projekten haben wir jeweils das berührungsempfindliche Logo und den Lautsprecher kennengelernt. In diesem Projekt werden wir diese beiden Komponenten kombinieren, um Musik abzuspielen.

2\.  **Benötigte Komponenten**

|![](./media/Python_021507bd.png)|![](./media/Python_84cdea05.jpg)|
|-|-|
|Micro:bit main board \*1|USB cable\*1|


3\.  **Schaltplan**

Verbinden Sie das Micro:bit main board über das USB-Kabel mit Ihrem Computer.

![](./media/Python_611b2c4e.png)

4\.  **Testcode**

Starten Sie die Mu-Software und öffnen Sie die Datei “Touch the Logo to control the speaker\.py”, um den Code zu importieren. Sie können den Code auch direkt im Editorfenster eingeben.

(**Hinweis: Alle Wörter und Symbole müssen in Englisch geschrieben sein**.)

![](./media/Python_600c8fa6.png)

```python
from microbit import *

import music

display.show(Image.MUSIC_QUAVER)

while True:

    if pin_logo.is_touched():
        music.play(music.BIRTHDAY)
```

Klicken Sie auf “Check”, um nach Fehlern im Code zu suchen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden.

![](./media/Python_dcc17127.png)

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit Ihrem Computer und klicken Sie auf “Flash”, um den Code auf das micro:bit-Board zu übertragen.

![](./media/Python_be3d4ee9.png)

5\.  **Testergebnis**

Nachdem der Code erfolgreich auf das Board geladen wurde, **schalten Sie die Stromversorgung über das Micro-USB-Kabel oder eine externe Stromquelle ein (schieben Sie den DIP-Schalter auf ON)** und drücken Sie die Reset-Taste am micro:bit.

![Img](./media/Python_bb3e1312.png)

Der Lautsprecher spielt das Lied „*Happy Birthday to You*“, wenn das Logo berührt wird.

6\.  **Code-Erklärung**

![Img](./media/Python_852be78f.png)

**Bluetooth-Funkkommunikation**

Das micro:bit verfügt über ein stromsparendes Bluetooth-Modul zur Kommunikation, hat jedoch nur 16 KB RAM. Der BLE-Heap-Stack belegt jedoch 12 KB RAM, sodass nicht genügend Speicherplatz vorhanden ist, um microPython auszuführen.

Derzeit unterstützt microPython den Bluetooth-Dienst nicht.

[https://microbit-micropython.readthedocs.io/en/latest/ble.html](https://microbit-micropython.readthedocs.io/en/latest/ble.html)

Die vorherigen Projekte sind eine Einführung in Sensoren und Module. Die weiteren Lektionen sind für Neueinsteiger anspruchsvoller.

(**Hinweis: Um ein Durchbrennen des micro:bit-Boards zu vermeiden, trennen Sie vor der Montage auf der Car-Expansion-Platine das Micro-USB-Kabel und schalten Sie die Stromversorgung der micro:bit Motor Driver Base Plate aus, indem Sie den POWER-Schalter auf OFF stellen. Ebenso trennen Sie vor dem Entfernen des Main Boards von der Car-Expansion-Platine das Micro-USB-Kabel und schalten die Stromversorgung der micro:bit Motor Driver Base Plate aus.**)