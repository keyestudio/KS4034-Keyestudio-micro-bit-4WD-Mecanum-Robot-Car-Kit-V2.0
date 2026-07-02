## Project 19：IR-Fernbedienung

### Project 19.1：IR-Fernbedienung decodieren

![](./media/Makecode_3a3e9860.png)

1\. **Beschreibung**

Es besteht kein Zweifel, dass Infrarot-Fernbedienungen im Alltag allgegenwärtig sind. Sie werden zur Steuerung verschiedener Haushaltsgeräte verwendet, z. B. Fernseher, Stereoanlagen, Videorecorder und Satellitenempfänger. Eine Infrarot-Fernbedienung besteht aus einem Infrarot-Sende- und einem Infrarot-Empfangssystem, also einer Fernbedienung, einem Infrarot-Empfangsmodul und einem dekodierfähigen Ein-Chip-Mikrocomputer.

![](./media/Makecode_9980b41f.png)

Das 38 kHz-Infrarot-Trägersignal, das von der Fernbedienung ausgesendet wird, wird vom Kodierungschip in der Fernbedienung kodiert. Es besteht aus einem Abschnitt Pilotcode, Benutzercode, invertiertem Benutzercode, Datencode und invertiertem Datencode. Das Zeitintervall des Impulses wird genutzt, um zu unterscheiden, ob es sich um ein 0- oder 1-Signal handelt, und die Kodierung besteht aus diesen 0- und 1-Signalen.

Der Benutzercode derselben Fernbedienung bleibt unverändert. Der Datencode unterscheidet die Taste.

Wenn eine Taste auf der Fernbedienung gedrückt wird, sendet die Fernbedienung ein Infrarot-Trägersignal aus. Wenn der IR-Empfänger das Signal empfängt, dekodiert das Programm das Trägersignal und bestimmt, welche Taste gedrückt wurde. Der MCU dekodiert das empfangene 01-Signal und legt so fest, welche Taste der Fernbedienung gedrückt wurde.

Der verwendete Infrarot-Empfänger ist ein Infrarot-Empfangsmodul. Es besteht hauptsächlich aus einem Infrarot-Empfangskopf und ist ein Gerät, das Empfang, Verstärkung und Demodulation integriert. Sein interner IC hat die Demodulation bereits übernommen und kann vom Infrarot-Empfang bis zur Ausgabe arbeiten und ist mit TTL-Signalen kompatibel. Außerdem ist es für Infrarot-Fernbedienungen und Infrarot-Datenübertragung geeignet. Das vom Empfänger gefertigte Infrarot-Empfangsmodul hat nur drei Anschlüsse: Signalleitung, VCC und GND.

Wie im obigen Bild gezeigt, ist der integrierte Anschluss des Infrarot-Empfängers mit dem P9 5V G Anschluss auf der Motorsteuerplatine verbunden und wird von P9 des micro:bit gesteuert.

2\. **Parameter:**

- Betriebsspannung: 3.3-5V（DC）

- Schnittstelle: 3PIN

- Ausgangssignal: digitales Signal

- Empfangswinkel: 90 Grad

- Frequenz: 38khz

- Empfangsreichweite: etwa 5m

3\. **Vorbereitung**

- Setzen Sie das micro:bit-Board in den Steckplatz des keyestudio   4WD Mecanum Robot Car V2.0 ein

- Legen Sie Batterien in das Batteriefach ein

- Schalten Sie den Netzschalter in die Stellung ON

- Verbinden Sie das micro:bit über ein USB-Kabel mit Ihrem Computer

- Öffnen Sie die Web-Version von Makecode


4\. **Testcode**

![](./media/Makecode_2e20f731.png)

Klicken Sie auf „JavaScript“, um in den entsprechenden JavaScript-Code zu wechseln:

![](./media/Makecode_87e18859.png)

**Code-Erklärung:** Wenn keine Tasten gedrückt werden, zeigt der serielle Monitor ständig 0 an; wenn eine Taste gedrückt wird, werden die entsprechenden Tastencodes angezeigt.

**Hinweise：**

Die Fernbedienung in diesem Kit enthält keine Batterien. Wir empfehlen, diese online zu erwerben. (Batterietyp: CR2025).

Stellen Sie sicher, dass die IR-Fernbedienung vor dem Test funktioniert. Hier ein Tipp zum Prüfen:

Öffnen Sie die Handykamera, richten Sie die IR-Fernbedienung auf die Kamera und drücken Sie eine Taste. Wenn Sie auf dem Kamerabildschirm ein violettes Blinklicht sehen, ist die Fernbedienung in Ordnung.

5\. **Testergebnis**

Laden Sie den Code auf das micro:bit-Board und ziehen Sie das USB-Kabel nicht ab. Klicken Sie![](./media/Makecode_e0580d78.png)

![](./media/Makecode_0d3198e0.png)

Richten Sie die IR-Fernbedienung auf den IR-Empfänger und drücken Sie eine Taste. Der serielle Monitor zeigt die entsprechenden Tastencodes an, wie unten dargestellt:

![](./media/Makecode_c7a33a4c.png)

Öffnen Sie CoolTerm, klicken Sie auf Options, um SerialPort auszuwählen. Stellen Sie den COM-Port und die Baudrate 115200 ein. Klicken Sie auf „OK“ und „Connect“.

Der CoolTerm-Seriellmonitor zeigt die Tastencodes wie folgt an:

![Img](./media/Makecode_155c857a.png)

Der Tastencode wird zur Referenz wie folgt angezeigt:

![](./media/Makecode_1fc0d9bb.jpg)

### Project 19.2：IR-Fernbedienung

![Img](./media/Makecode_643cb701.png)

1\. **Beschreibung**

In diesem Projekt kombinieren wir die IR-Fernbedienung mit dem Car Shield, um ein per IR gesteuertes Smart Car zu erstellen. Das Prinzip besteht darin, die Bewegung des Fahrzeugs zu steuern, indem Tastenbefehle von der IR-Fernbedienung an das IR-Empfangsmodul des Car Shields gesendet werden.

2\. **Vorbereitung**

- Setzen Sie das micro:bit-Board in den Steckplatz des keyestudio   4WD Mecanum Robot Car V2.0 ein

- Legen Sie Batterien in das Batteriefach ein

- Schalten Sie den Netzschalter in die Stellung ON

- Verbinden Sie das micro:bit über ein USB-Kabel mit Ihrem Computer

- Öffnen Sie die Web-Version von Makecode

**Hinweis:** Der Infrarotsensor und die IR-Fernbedienung sollten nicht in Umgebungen mit Infrarotstörungen wie direktem Sonnenlicht verwendet werden, da dieses viele unsichtbare Lichtanteile wie Infrarot und Ultraviolett enthält. In einer Umgebung mit starkem Sonnenlicht können sie nicht ordnungsgemäß funktionieren.

3\. **Flussdiagramm**

![Img](./media/Makecode_e5f416e3.png)

4\. **Testcode**

![](./media/Makecode_22d06d74.png)

Klicken Sie auf „JavaScript“, um in den entsprechenden JavaScript-Code zu wechseln:

![](./media/Makecode_e68b6275.png)

![](./media/Makecode_94de6552.png)

5\. **Testergebnis**

Laden Sie den Code auf das micro:bit-Board und stellen Sie den POWER-Schalter auf ON.

Richten Sie die IR-Fernbedienung auf das micro:bit und drücken Sie eine Taste, um das Smart Car zu steuern.

![](./media/Makecode_d55474f3.png) Die Taste macht das Smart Car vorwärts fahren，![](./media/Makecode_5c8a6549.png) steht für Linksdrehen，![](./media/Makecode_41116032.png) bedeutet Rechtsdrehung，![](./media/Makecode_369433f6.png) zeigt Rückwärtsfahrt an，![](./media/Makecode_a8ef4b17.png) stoppt das Auto.

**Hinweis:** Der Abstand zwischen der IR-Fernbedienung und der IR-Empfangseinheit des Smart Cars sollte während des Tests weniger als 5 m betragen.

---