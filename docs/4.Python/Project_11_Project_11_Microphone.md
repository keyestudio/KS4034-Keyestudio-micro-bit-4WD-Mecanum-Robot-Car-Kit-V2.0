### Projekt 11: Mikrofon

![](./media/Python_3073a8af.png)

![](./media/Python_7f074115.png)

1\.  **Beschreibung**

Die Micro: Bit-Hauptplatine verfügt über ein eingebautes Mikrofon, mit dem die Umgebungslautstärke gemessen werden kann. Wenn Sie klatschen, leuchtet die Mikrofon-LED-Anzeige auf. Darüber hinaus kann es die Lautstärke messen, sodass Sie eine Lärmskala oder eine Discobeleuchtung erstellen können, die sich zur Musik ändert.

Das Mikrofon befindet sich auf der gegenüberliegenden Seite der Mikrofon-LED-Anzeige und in der Nähe von Öffnungen, durch die der Schall gelangen kann. Wenn die Platine den Ton erkennt, leuchtet die LED-Anzeige auf.

2\.  **Vorbereitung**

A. Schließen Sie die micro:bit-Hauptplatine mit dem USB-Kabel an Ihren Computer an.

B. Öffnen Sie die Offline-Version von Mu.

3\.  **Testcode1**

Starten Sie die Mu-Software und öffnen Sie die Datei “Microphone-1\.py”, um den Code zu laden. Sie können den Code auch selbst im Bearbeitungsfenster eingeben.

(**Hinweis: Alle Wörter und Zeichen müssen auf Englisch geschrieben sein**.)

![](./media/Python_19b38832.png)

```python
from microbit import *

while True:
    if microphone.current_event() == SoundEvent.LOUD:
        display.show(Image.HEART)
        sleep(200)
    if microphone.current_event() == SoundEvent.QUIET:
        display.show(Image.HEART_SMALL)
```

Klicken Sie auf „Check“, um Fehler im Code zu prüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden. 

![](./media/Python_36a669c7.png)

Wenn der Code korrekt ist, verbinden Sie den micro:bit mit Ihrem Computer und klicken Sie auf „Flash“, um den Code auf die micro:bit-Platine herunterzuladen.

![](./media/Python_0515bf32.png)

4\.  **Testergebnis1**

Nachdem der Code erfolgreich auf die Platine heruntergeladen wurde, **schalten Sie die Stromversorgung über das Micro-USB-Kabel oder eine externe Stromquelle ein (DIP-Schalter auf ON stellen)** und drücken Sie die Reset-Taste am micro:bit.

![Img](./media/Python_bb3e1312.png)

Die LED-Punktmatrix zeigt das Muster „❤“, wenn Sie klatschen, und das Muster ![](./media/04fdfc9060943954e7938bb1a741d626.png), wenn es ruhig ist.

5\.  **Testcode2**

Starten Sie die Mu-Software und öffnen Sie die Datei “Microphone-2\.py”, um den Code zu laden. Sie können den Code auch selbst im Bearbeitungsfenster eingeben.

(**Hinweis: Alle Wörter und Zeichen müssen auf Englisch geschrieben sein.**)

![](./media/Python_f0e5a346.png)

```python
from microbit import *
maxSound = 0
lights = Image("11111:"
              "11111:"
              "11111:"
              "11111:"
              "11111")
# ignore first sound level reading
soundLevel = microphone.sound_level()
sleep(200)

while True:
    if button_a.is_pressed():
        display.scroll(maxSound)
    else:
        soundLevel = microphone.sound_level()
        display.show(lights * soundLevel)
        if soundLevel > maxSound:
            maxSound = soundLevel
```

Klicken Sie auf „Check“, um Fehler im Code zu prüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden. 

![](./media/Python_d0c79871.png)

Wenn der Code korrekt ist, verbinden Sie den micro:bit mit Ihrem Computer und klicken Sie auf „Flash“, um den Code auf die micro:bit-Platine herunterzuladen.

![](./media/Python_d828b9ee.png)

6\.  **Testergebnis2**

Nachdem der Code erfolgreich auf die Platine heruntergeladen wurde, **schalten Sie die Stromversorgung über das Micro-USB-Kabel oder eine externe Stromquelle ein (DIP-Schalter auf ON stellen)** und drücken Sie die Reset-Taste am micro:bit.

![Img](./media/Python_bb3e1312.png)

Wenn die Taste A gedrückt wird, zeigt die LED-Punktmatrix den Wert der größten Lautstärke an ( **bitte beachten Sie, dass die größte Lautstärke über die Reset-Taste auf der anderen Seite der Platine zurückgesetzt werden kann** ). Beim Klatschen gilt: Je lauter der gemessene Ton, desto heller leuchten die 25 LEDs der LED-Punktmatrix.

7\.  **Code-Erklärung**

![Img](./media/Python_980f62b3.png)