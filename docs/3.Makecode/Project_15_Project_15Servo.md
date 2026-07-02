## Projekt 15：Servo

![](./media/Makecode_215da878.png)

1\.  **Beschreibung**

Bei DIY-Smartcars ist häufig eine automatische Hindernisvermeidung integriert. Im DIY-Prozess wird ein Servomotor verwendet, um das Ultraschallmodul nach links und rechts zu drehen und so den Abstand zwischen dem Fahrzeug und einem Hindernis zu messen, damit das Fahrzeug dem Hindernis ausweichen kann. Wenn andere Mikrocontroller zur Steuerung der Servodrehung verwendet werden, müssen bestimmte Frequenzen und Pulsbreiten eingestellt werden, um den Servowinkel zu steuern.

Wird jedoch das micro:bit-Hauptboard zur Steuerung des Servowinkels verwendet, muss im Entwicklungsumgebung nur der Steuerwinkel eingestellt werden; das entsprechende Steuersignal (Puls) wird dann automatisch erzeugt, um die Servodrehung zu steuern. In diesem Projekt lernen Sie, wie der Servo zwischen 0° und 90° hin und her gesteuert wird.

2\.  **Informationen zum Servo**

Ein Servomotor ist ein drehbarer Aktuator zur Positionsregelung. Er besteht hauptsächlich aus Gehäuse, Leiterplatte, kernlosem Motor, Getriebe und Positionssensor. Das Funktionsprinzip besteht darin, dass der Servo das vom MCU oder Empfänger gesendete Signal empfängt, ein Referenzsignal mit einer Periode von 20 ms und einer Breite von 1,5 ms erzeugt, dann die erhaltene Gleichspannungs-Vorspannung mit der Spannung des Potentiometers vergleicht und die Spannungsdifferenz als Ausgang liefert.

![](./media/Makecode_87b41036.png)

Bei dem in diesem Projekt verwendeten Servo ist das braune Kabel Masse, das rote Kabel die Stromversorgung (V+) und das orangefarbene Kabel das Signalsignal.

Der Drehwinkel des Servomotors wird durch Regelung des Tastverhältnisses des PWM- (Pulse-Width Modulation) Signals gesteuert. Der Standardzyklus des PWM-Signals beträgt 20 ms (50 Hz). Theoretisch liegt die Pulsbreite zwischen 1 ms und 2 ms, in der Praxis jedoch zwischen 0,5 ms und 2,5 ms. Die Pulsbreite entspricht dem Drehwinkel von 0° bis 180°. Beachten Sie jedoch, dass bei Motoren verschiedener Hersteller dasselbe Signal zu unterschiedlichen Drehwinkeln führen kann.

![](./media/Makecode_49467dfa.png)

Mehr Details:

![](./media/Makecode_b167d550.png)

3\.  **Parameter**

- Arbeitsspannung: DC 4.8V ~ 6V

- Einstellbarer Winkelbereich: ca. 180 ° (bei 500 → 2500 μsec)

- Pulsbreitenbereich: 500 → 2500 μsec

- Leerlaufdrehzahl: 0.12 ± 0.01 s / 60 (DC 4.8V) 0.1 ± 0.01 s / 60 (DC 6V)

- Leerlaufstrom: 200 ± 20mA (DC 4.8V) 220 ± 20mA (DC 6V)

- Haltemoment (Stoppmoment): 1.3 ± 0.01kg·cm (DC 4.8V) 1.5 ± 0.1kg·cm (DC 6V)

- Stoppstrom: ≦ 850mA (DC 4.8V) ≦ 1000mA (DC 6V)

- Bereitschaftsstrom: 3 ± 1mA (DC 4.8V) 4 ± 1mA (DC 6V)

4\.  **Vorbereitung**

- Setzen Sie das micro:bit-Board in den Steckplatz des keyestudio   4WD Mecanum Robot Car V2.0 ein

- Legen Sie Batterien in den Batteriehalter ein

- Schalten Sie den Powerschalter auf die ON-Stellung

- Verbinden Sie das micro:bit per USB-Kabel mit Ihrem Computer

- Öffnen Sie die Web-Version von Makecode


5\.  **Testcode**

![](./media/Makecode_087e1822.png)

Klicken Sie auf "JavaScript", um den entsprechenden JavaScript-Code anzuzeigen:

![](./media/Makecode_2354311f.png)

6.  **Testergebnis**

Nach dem Hochladen des Testcodes und Einschalten des POWER-Schalters dreht sich der Servo von 0 Grad bis 180 Grad.