### Project 15：Servo

![](./media/Python_c4b5e57b.png)

1\.  **Beschreibung**

Bei DIY-Smartcars ist üblicherweise eine Funktion zur automatischen Hindernisvermeidung enthalten. Im DIY-Prozess benötigen wir einen Servo, um das Ultraschallmodul nach links und rechts zu drehen und dann die Entfernung zwischen Auto und Hindernis zu messen, um das Auto zur Vermeidung des Hindernisses zu steuern.

Wenn andere Mikrocontroller zur Steuerung der Servodrehung verwendet werden, muss eine bestimmte Frequenz und Pulsbreite eingestellt werden, um den Servowinkel zu steuern. Wird jedoch das micro:bit-Hauptboard zur Steuerung des Servowinkels verwendet, muss im Entwicklungsumfeld nur der Steuerwinkel eingestellt werden; das entsprechende Puls-Signal wird dann automatisch erzeugt, um die Servodrehung zu steuern. In diesem Projekt lernen Sie, wie man den Servo zwischen 0° und 90° hin- und herrotieren lässt.

Ein Servomotor ist ein positionsgesteuerter Drehaktuator, der hauptsächlich aus Gehäuse, Leiterplatte, kernlosem Motor, Getriebe und Positionssensor besteht. Sein Arbeitsprinzip besteht darin, dass der Servo das vom MCU oder Empfänger gesendete Signal empfängt, ein Referenzsignal mit einer Periode von 20 ms und einer Pulsbreite von 1,5 ms erzeugt, dann die gewonnene Gleichspannungs-Vorspannung mit der Spannung des Potentiometers vergleicht und die Spannungsdifferenz als Ausgang liefert.

Bei dem in diesem Projekt verwendeten Servo ist das braune Kabel Masse, das rote ist Plus und das orange Kabel ist das Signalkabel.

![](./media/Python_69be9581.png)

2\.  **Informationen zum Servo**

Der Drehwinkel des Servomotors wird durch Regulierung des Tastverhältnisses des PWM-(Pulse-Width-Modulation)-Signals gesteuert. Der Standardzyklus des PWM-Signals beträgt 20 ms (50 Hz). Theoretisch verteilt sich die Pulsbreite zwischen 1 ms und 2 ms, in der Praxis liegt sie jedoch zwischen 0,5 ms und 2,5 ms. Die Pulsbreite entspricht einem Drehwinkel von 0° bis 180°. Beachten Sie jedoch, dass bei verschiedenen Marken der gleiche Signalwert unterschiedliche Drehwinkel bewirken kann.

![](./media/Python_0982cb7b.png)

Nach Messung liegt der Pulsbereich des Servos bei 0,65 ms bis 2,5 ms. Für einen 180-Grad-Servo ist die entsprechende Steuerbeziehung wie folgt:


|Time on High Level|Angle of the Servo|Reference Signal Cycle Time（20ms）|
|-|-|-|
|0.65ms|0 degree|0.65ms high level+19.35ms low level|
|1.5ms|90 degrees|1.5ms high level+18.5ms low level|
|2.5ms|180degrees|2.5ms high level+17.5ms low level|


3\.  **Parameter**

- Betriebsspannung: DC 4.8V ~ 6V

- Betriebswinkelbereich: ca. 180 ° (bei 500 → 2500 μsec)

- Abmessungen: 22.9\*12.2\*30mm

- Pulsweitenbereich: 500 → 2500 μsec

- Leerlaufdrehzahl: 0.12 ± 0.01 s / 60 (DC 4.8V), 0.1 ± 0.01 s / 60 (DC 6V)

- Leerlaufstrom: 200 ± 20mA (DC 4.8V), 220 ± 20mA (DC 6V)

- Haltemoment: 1.3 ± 0.01kg · cm (DC 4.8V), 1.5 ± 0.1kg · cm (DC 6V)

- Stillstandsstrom: ≦ 850mA (DC 4.8V) ≦ 1000mA (DC 6V)

- Ruhestrom: 3 ± 1mA (DC 4.8V), 4 ± 1mA (DC 6V)

- Gewicht: 9±1g (ohne Servoarm)

- Arbeitstemperatur: -30℃~60℃

**Hinweis: Verwenden Sie nicht die Stromversorgung eines Computers, da der Servo beschädigt werden kann, wenn die Stromaufnahme größer als 500 mA ist. Es wird empfohlen, eine externe Batterie zur Stromversorgung zu verwenden.**

4\.  **Vorbereitung**

- Setzen Sie das micro:bit-Board in den Steckplatz des keyestudio 4WD Mecanum Robot Car V2.0 ein

- Legen Sie die Batterien in den Batteriehalter ein

- Schalten Sie den Netzschalter auf ON

- Verbinden Sie das micro:bit per USB-Kabel mit dem Computer

- Öffnen Sie die Offline-Version von Mu.

5\.  **Testcode**

Starten Sie die Mu-Software und öffnen Sie die Datei “Servo\.py”, um den Code zu laden. Sie können den Code auch selbst im Editor-Fenster eingeben.

(**Hinweis: Alle englischen Wörter und Symbole müssen auf Englisch geschrieben sein**.)

Klicken Sie auf “Check”, um den Code auf Fehler zu prüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen oder Cursor angezeigt werden.

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit Ihrem Computer und klicken Sie auf “Flash”, um den Code auf das micro:bit-Board zu übertragen.

![](./media/Python_eecf365e.png)

```python
from microbit import *

class Servo:
    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.analog_period = 0
        self.pin = pin
        analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
        self.pin.set_analog_period(analog_period)

    def write_us(self, us):
        us = min(self.max_us, max(self.min_us, us))
        duty = round(us * 1024 * self.freq // 1000000)
        self.pin.write_analog(duty)
        sleep(100)
        self.pin.write_analog(0)

    def write_angle(self, degrees=None):
        if degrees is None:
            degrees = math.degrees(radians)
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.write_us(us)

Servo(pin14).write_angle(0)
display.show(Image.HAPPY)

while True:
        Servo(pin14).write_angle(0)
        sleep(1000)
        Servo(pin14).write_angle(45)
        sleep(1000)
        Servo(pin14).write_angle(90)
        sleep(1000)
        Servo(pin14).write_angle(135)
        sleep(1000)
        Servo(pin14).write_angle(180)
        sleep(1000)

```

4\.  **Testergebnis**

Nachdem der Code erfolgreich auf das Board heruntergeladen wurde, **externe Stromversorgung einschalten (DIP-Schalter auf ON)** und den Reset-Knopf am micro:bit drücken.

![Img](./media/Python_bb3e1312.png)

Die LED-Matrix zeigt ein Smiley-Muster an und der Servo dreht sich im Muster 0°~45°~90°~135°~180°~0°.

---