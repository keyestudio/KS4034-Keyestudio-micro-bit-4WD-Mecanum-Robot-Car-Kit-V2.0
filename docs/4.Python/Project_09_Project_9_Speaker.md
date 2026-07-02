### Projekt 9: Lautsprecher

![](./media/Python_ac515b9a.png)

1\.  **Beschreibung**

Das micro:bit-Hauptboard verfügt über einen eingebauten Lautsprecher, wodurch das Hinzufügen von Ton zu Programmen einfacher wird. Es kann auch so programmiert werden, dass es alle Arten von Tönen erzeugt, z. B. das Spielen des Liedes *Ode to Joy*.

2\.  **Vorbereitung**

A. Verbinden Sie das micro:bit-Hauptboard über das USB-Kabel mit Ihrem Computer

B. Öffnen Sie die Offline-Version von Mu.

3\.  **Testcode**

Starten Sie die Mu-Software und öffnen Sie die Datei “Speaker\.py”, um den Code zu importieren. Sie können den Code auch selbst im Editierfenster eingeben.

(**Hinweis: Alle Wörter und Symbole müssen in Englisch geschrieben sein**.)

![](./media/Python_eec7f643.png)

```python
from microbit import *

import audio

display.show(Image.MUSIC_QUAVER)

while True:
    audio.play(Sound.GIGGLE)
    sleep(1000)
    audio.play(Sound.HAPPY)
    sleep(1000)
    audio.play(Sound.HELLO)
    sleep(1000)
    audio.play(Sound.YAWN)
    sleep(1000)
```

Klicken Sie auf “Check”, um Fehler im Code zu überprüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden.

![](./media/Python_f8852abf.png)

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit Ihrem Computer und klicken Sie auf “Flash”, um den Code auf das micro:bit-Board herunterzuladen.

![](./media/Python_3fd94e43.png)

4\.  **Testergebnis**

Nachdem der Code erfolgreich auf das Board heruntergeladen wurde, **schalten Sie die Stromversorgung über das Micro-USB-Kabel oder eine externe Stromversorgung ein (DIP-Schalter auf ON stellen)** und drücken Sie die Reset-Taste am micro:bit.

![Img](./media/Python_bb3e1312.png)

 Der Lautsprecher gibt einen Ton von sich und die LED-Punktmatrix zeigt das Musik-Symbol.

5\.  **Code-Erklärung**

![Img](./media/Python_18c047bd.png)

---