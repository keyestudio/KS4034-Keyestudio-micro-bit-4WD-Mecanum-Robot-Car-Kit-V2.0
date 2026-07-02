### Projekt 18：Ultraschallsensor

#### Projekt 18.1：Ultraschall-Entfernungsmessung

1. **Beschreibung**

![](./media/Python_9810ae67.jpg)

Der Ultraschallsensor nutzt Sonar zur Entfernungsbestimmung zu einem Objekt, ähnlich wie Fledermäuse. Er bietet eine hervorragende berührungslose Abstandserkennung mit hoher Genauigkeit und stabilen Messwerten in einem einfach zu verwendenden Modul. Es enthält sowohl Ultraschall-Sender- als auch Empfängermodule.

Der Ultraschallsensor wird in einer Vielzahl von Elektronikprojekten eingesetzt, um Hinderniserkennung und Abstandsmessanwendungen sowie verschiedene andere Anwendungen zu realisieren.

![](./media/Python_0180b169.png)

Das Ultraschallmodul sendet Ultraschallwellen nach einem Trigger-Signal aus. Wenn die Ultraschallwellen auf ein Objekt treffen und zurückreflektiert werden, gibt das Modul ein Echo-Signal aus, sodass es den Abstand des Objekts aus der Zeitdifferenz zwischen Trigger-Signal (TRIG) und Echo-Signal (ECHO) bestimmen kann.

Wie auf dem Bild zu sehen ist, ist es wie zwei Augen. Eines ist der Sendeteil, das andere der Empfangsteil.

Entsprechend dem obigen Anschlussdiagramm ist der integrierte Port des Ultraschallmoduls mit dem 5V G P15 P16 Port auf der micro:bit Motor-Treiber-Platine verbunden. Der Trig (T) Pin wird vom P15 des micro:bit gesteuert und der Echo (E) Pin vom P16.

![](./media/Python_19b45a23.jpg)

2. **Funktionsprinzip**

![](./media/Python_8ff02741.png)

(1) TRIG auf Low ziehen und dann mit mindestens 10 µs einen High-Trigger senden;

(2) Nach dem Trigger sendet das Modul automatisch acht 40 kHz Ultraschallimpulse und prüft, ob ein Rücksignal empfangen wird;

(3) Wenn ein Rücksignal vorhanden ist, gibt ECHO (E) beim Empfang einen High-Pegel aus; die Dauer des High-Levels entspricht der Zeit von Aussenden bis Empfangen der Ultraschallwellen. Dann Entfernung = High-Pegel-Dauer * 340 m/s * 0,5.

3. **Parameter**

- Betriebsspannung: 3-5.5V (DC)
- Betriebsstrom: 15mA
- Arbeitsfrequenz: 40kHz
- Maximale Erkennungsdistanz: ca. 3m
- Minimale Erkennungsdistanz: 2-3cm
- Genauigkeit: bis zu 0,2cm
- Erkennungswinkel: weniger als 15 Grad
- Eingangs-Trigger-Impuls: 10 µs TTL-Pegel
- Ausgangs-Echo-Signal: TTL-Pegel (High), proportional zur Reichweite

4. **Vorbereitung**

- Setzen Sie das micro:bit-Board in den Steckplatz des keyestudio 4WD Mecanum Robot Car V2.0 ein
- Legen Sie die Batterien in das Batteriefach ein
- Schalten Sie den Netzschalter auf die Position ON
- Verbinden Sie das micro:bit mit dem Computer über ein USB-Kabel
- Öffnen Sie die Offline-Version von Mu

5. **Testcode**

Öffnen Sie die Mu-Software und laden Sie die Datei “Ultrasonic Ranging\.py”, um den Code zu importieren. Sie können den Code auch selbst im Editorfenster eingeben.

(Hinweis: Alle englischen Wörter und Symbole müssen in Englisch geschrieben werden.)

Klicken Sie auf “Files”, um die Bibliotheksdatei “keyes_mecanum_Car_V2.py” auf das micro:bit zu importieren.

Klicken Sie auf “Check”, um Fehler im Code zu prüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden.

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit Ihrem Computer und klicken Sie auf “Flash”, um den Code auf das micro:bit-Board zu laden.

![](./media/Python_5a29bde9.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()
import music
tune = ["C4:4"]
distance_val = 0

while True:
    i = 0
    distance_val = mecanumCar.get_distance()
    print("distance:", distance_val)
    if distance_val < 10:
        while i < 1:
            music.play(tune)
            sleep(200)
            music.play(tune)
            sleep(200)
            i += 1

```

6. **Testergebnis**

Nachdem der Code erfolgreich auf das Board geladen wurde und das USB-Kabel nicht getrennt ist, klicken Sie auf “REPL” und drücken dann die Reset-Taste.

![Img](./media/Python_bb3e1312.png)

Der Entfernungswert des Hindernisses wird angezeigt, wie unten dargestellt.

Ist die Entfernung weniger als 10 cm, ertönt der passive Summer des Smart Cars.

![](./media/Python_4dc8054e.png)

7. **Code-Erklärung**

![Img](./media/Python_ebde06e9.png)

#### Projekt 18.2：Ultraschall-Ausweichfahrt

![](./media/Python_aee41f6f.jpg)

1. **Beschreibung**

In diesem Projekt integrieren wir einen Ultraschallsensor in ein Fahrzeug, um ein Ultraschall-Ausweichfahrzeug zu bauen.

Das Prinzip besteht darin, mit dem Ultraschallsensor den Abstand zwischen Fahrzeug und Hindernis zu messen, um die Bewegung des Smart Cars zu steuern.

2. **Vorbereitung**

- Setzen Sie das micro:bit-Board in den Steckplatz des keyestudio 4WD Mecanum Robot Car V2.0 ein
- Legen Sie die Batterien in das Batteriefach ein
- Schalten Sie den Netzschalter auf die Position ON
- Verbinden Sie das micro:bit mit dem Computer über ein USB-Kabel
- Öffnen Sie die Offline-Version von Mu

3. **Flussdiagramm**

![Img](./media/Python_a4efee72.png)

4. **Testcode**

Öffnen Sie die Mu-Software und laden Sie die Datei “Ultrasonic Avoid Smart Car\.py”, um den Code zu importieren. Sie können den Code auch selbst im Editorfenster eingeben.

(Hinweis: Alle englischen Wörter und Symbole müssen in Englisch geschrieben werden.)

Klicken Sie auf “Files”, um die Bibliotheksdatei “keyes_mecanum_Car_V2.py” auf das micro:bit zu importieren.

Klicken Sie auf “Check”, um Fehler im Code zu prüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden.

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit Ihrem Computer und klicken Sie auf “Flash”, um den Code auf das micro:bit-Board zu laden.

![](./media/Python_38f3510c.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()
distance_val = 0
distance_l = 0
distance_r = 0
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

Servo(pin14).write_angle(90)

while True:

    distance_val = mecanumCar.get_distance()

    if distance_val < 20:
        mecanumCar.Motor_Upper_L(0, 0)
        mecanumCar.Motor_Lower_L(0, 0)
        mecanumCar.Motor_Upper_R(0, 0)
        mecanumCar.Motor_Lower_R(0, 0)
        sleep(500)
        Servo(pin14).write_angle(180)
        sleep(500)
        distance_l = mecanumCar.get_distance()
        sleep(500)

        Servo(pin14).write_angle(0)
        sleep(500)
        distance_r = mecanumCar.get_distance()
        sleep(500)

        if distance_l > distance_r:
            mecanumCar.Motor_Upper_L(0, 100)
            mecanumCar.Motor_Lower_L(0, 100)
            mecanumCar.Motor_Upper_R(1, 100)
            mecanumCar.Motor_Lower_R(1, 100)
            Servo(pin14).write_angle(90)
            sleep(300)
        else:
            mecanumCar.Motor_Upper_L(1, 100)
            mecanumCar.Motor_Lower_L(1, 100)
            mecanumCar.Motor_Upper_R(0, 100)
            mecanumCar.Motor_Lower_R(0, 100)
            Servo(pin14).write_angle(90)
            sleep(300)

    else:
        mecanumCar.Motor_Upper_L(1, 100)
        mecanumCar.Motor_Lower_L(1, 100)
        mecanumCar.Motor_Upper_R(1, 100)
        mecanumCar.Motor_Lower_R(1, 100)
```

5. **Testergebnis**

Nachdem der Code erfolgreich auf das Board geladen wurde, externe Stromversorgung anschließen (DIP-Schalter auf ON stellen) und die Reset-Taste am micro:bit drücken.

![Img](./media/Python_bb3e1312.png)

Ist der Hindernisabstand größer als 20 cm, fährt das Auto vorwärts; andernfalls dreht das Smart Car nach links.

6. **Code-Erklärung**

![Img](./media/Python_9e28cce7.png)

![Img](./media/Python_c33a22a8.png)

#### Projekt 18.3：Ultraschall-Folgefahrt

![](./media/Python_28806167.jpg)

1. **Beschreibung**

In der vorherigen Lektion haben wir das Grundprinzip des Linienfolgesensors kennengelernt. Als Nächstes kombinieren wir den Ultraschallsensor mit dem Fahrzeug, um ein Ultraschall-Folgeauto zu bauen.

Der Ultraschallsensor ermittelt den Hindernisabstand und steuert damit die Bewegungszustände des Fahrzeugs.

2. **Vorbereitung**

- Setzen Sie das micro:bit-Board in den Steckplatz des keyestudio 4WD Mecanum Robot Car V2.0 ein
- Legen Sie die Batterien in das Batteriefach ein
- Schalten Sie den Netzschalter auf die Position ON
- Verbinden Sie das micro:bit mit dem Computer über ein USB-Kabel
- Öffnen Sie die Offline-Version von Mu

2. **Flussdiagramm**

![Img](./media/Python_53a30906.png)

3. **Testcode**

Öffnen Sie die Mu-Software und laden Sie die Datei “Ultrasonic Follow Smart Car\.py”, um den Code zu importieren. Sie können den Code auch selbst im Editorfenster eingeben.

(Hinweis: Alle englischen Wörter und Symbole müssen in Englisch geschrieben werden.)

Klicken Sie auf “Files”, um die Bibliotheksdatei “keyes_mecanum_Car_V2.py” auf das micro:bit zu importieren.

Klicken Sie auf “Check”, um Fehler im Code zu prüfen. Das Programm ist fehlerhaft, wenn Unterstreichungen und Cursor angezeigt werden.

Wenn der Code korrekt ist, verbinden Sie das micro:bit mit Ihrem Computer und klicken Sie auf “Flash”, um den Code auf das micro:bit-Board zu laden.

![](./media/Python_f586f3f7.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *
import neopixel
display.off()

mecanumCar = Mecanum_Car_Driver_V2()
np = neopixel.NeoPixel(pin7, 4)

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

Servo(pin14).write_angle(90)

while True:
    distance_val = 0
    distance_val = mecanumCar.get_distance()
    if distance_val >= 20 and distance_val <= 40:
        mecanumCar.Motor_Upper_L(1, 80)
        mecanumCar.Motor_Lower_L(1, 80)
        mecanumCar.Motor_Upper_R(1, 80)
        mecanumCar.Motor_Lower_R(1, 80)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 0, 0)
            np.show()
    if distance_val <= 10:
        mecanumCar.Motor_Upper_L(0, 80)
        mecanumCar.Motor_Lower_L(0, 80)
        mecanumCar.Motor_Upper_R(0, 80)
        mecanumCar.Motor_Lower_R(0, 80)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 255, 0)
            np.show()
    if distance_val > 10 and distance_val < 20 or distance_val > 40:
        mecanumCar.Motor_Upper_L(0, 0)
        mecanumCar.Motor_Lower_L(0, 0)
        mecanumCar.Motor_Upper_R(0, 0)
        mecanumCar.Motor_Lower_R(0, 0)
        for pixel_id1 in range(0, len(np)):
            np[pixel_id1] = (255, 255, 255)
            np.show()
```

4. **Testergebnis**

Nachdem der Code erfolgreich auf das Board geladen wurde, externe Stromversorgung anschließen (DIP-Schalter auf ON stellen) und die Reset-Taste am micro:bit drücken.

![Img](./media/Python_bb3e1312.png)

Das Smart Car kann dem Hindernis folgen und die 4 WS2812 RGB-LEDs zeigen unterschiedliche Farben an.

Hinweis: Das Hindernis darf sich nur vor dem Smart Car bewegen.

5. **Code-Erklärung**

![Img](./media/Python_930a04fa.png)

![Img](./media/Python_26371a4d.png)