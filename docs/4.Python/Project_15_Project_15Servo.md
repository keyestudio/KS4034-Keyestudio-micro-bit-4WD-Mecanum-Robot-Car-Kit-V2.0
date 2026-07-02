### Progetto 15：Servo

![](./media/Python_c4b5e57b.png)

1\.  **Descrizione**

Le auto smart fai-da-te di solito includono la funzione di evitamento automatico degli ostacoli. Nel processo di realizzazione, è necessario un servo per controllare il modulo ad ultrasuoni che ruota a sinistra e a destra, e poi misurare la distanza tra l'auto e l'ostacolo, in modo da controllare l'auto per evitare l'ostacolo.

Se si utilizzano altri microcontrollori per controllare la rotazione del servo, bisogna impostare una certa frequenza e larghezza dell'impulso per controllare l'angolo del servo. Ma se si utilizza la scheda principale micro:bit per controllare l'angolo del servo, è sufficiente impostare l'angolo di controllo nell'ambiente di sviluppo: l'impulso corrispondente verrà generato automaticamente per controllare la rotazione del servo. In questo progetto imparerai a controllare il servo per farlo oscillare fra 0° e 90°.

Il servomotore è un attuatore rotativo a controllo di posizione, composto principalmente da chassis, circuito stampato, motore senza nucleo, ingranaggi e sensore di posizione. Il suo principio di funzionamento è che il servo riceve il segnale inviato dal MCU o dal ricevitore, produce un segnale di riferimento con periodo di 20 ms e larghezza di 1,5 ms, poi confronta la tensione continua acquisita con la tensione del potenziometro e ottiene la differenza di tensione in uscita.

Per il servo utilizzato in questo progetto, il filo marrone è la massa, il rosso è il positivo e l'arancione è il filo del segnale.

![](./media/Python_69be9581.png)

2\.  **Informazioni sul Servo**

L'angolo di rotazione del servomotore è controllato regolando il duty cycle del segnale PWM (Pulse-Width Modulation). Il ciclo standard del segnale PWM è di 20 ms (50 Hz). Teoricamente la larghezza è compresa tra 1 ms e 2 ms, ma in realtà è tra 0,5 ms e 2,5 ms. La larghezza corrisponde all'angolo di rotazione da 0° a 180°. Nota che per motori di marche diverse lo stesso segnale può produrre angoli di rotazione differenti.

![](./media/Python_0982cb7b.png)

Dopo misurazioni, l'intervallo di impulso del servo è 0,65 ms ~ 2,5 ms. Per un servo a 180 gradi, la relazione di controllo corrispondente è la seguente:


|Time on High Level|Angle of the Servo|Reference Signal Cycle Time（20ms）|
|-|-|-|
|0.65ms|0 degree|0.65ms high level+19.35ms low level|
|1.5ms|90 degrees|1.5ms high level+18.5ms low level|
|2.5ms|180degrees|2.5ms high level+17.5ms low level|


3\.  **Parametri**

- Tensione di funzionamento: DC 4.8V ~ 6V

- Intervallo di angolo operativo: circa 180 ° (a 500 → 2500 μsec)

- Dimensioni: 22.9\*12.2\*30mm

- Intervallo di larghezza dell'impulso: 500 → 2500 μsec

- Velocità a vuoto: 0.12 ± 0.01 sec / 60 (DC 4.8V), 0.1 ± 0.01 sec / 60 (DC 6V)

- Corrente a vuoto: 200 ± 20mA (DC 4.8V), 220 ± 20mA (DC 6V)

- Coppia di bloccaggio: 1.3 ± 0.01kg · cm (DC 4.8V), 1.5 ± 0.1kg · cm (DC 6V)

- Corrente di stop: ≦ 850mA (DC 4.8V) ≦ 1000mA (DC 6V)

- Corrente di standby: 3 ± 1mA (DC 4.8V), 4 ± 1mA (DC 6V)

- Peso: 9±1g (senza braccio del servo)

- Temperatura di funzionamento: -30℃~60℃

**Si noti di non usare l'alimentazione del computer, poiché se la richiesta di corrente è superiore a 500 mA il servo potrebbe bruciarsi. Si consiglia di utilizzare una batteria esterna per l'alimentazione.**

4\.  **Preparazione**

- Inserire la scheda micro:bit nello slot del keyestudio 4WD Mecanum Robot Car V2.0

- Inserire le batterie nel portabatterie

- Portare l'interruttore di alimentazione su ON

- Collegare il micro:bit al computer tramite cavo USB

- Aprire la versione offline di Mu.

5\.  **Codice di test**

Avviare il software Mu e aprire il file “Servo\.py” per importare il codice. È anche possibile inserire il codice manualmente nella finestra di modifica.

(**Nota: Tutte le parole e i simboli in inglese devono essere scritti in inglese**.)

Fare clic su “Check” per esaminare gli errori nel codice. Il programma è errato se vengono mostrati sottolineature o cursori.

Se il codice è corretto, collegare il micro:bit al computer e fare clic su “Flash” per scaricare il codice sulla scheda micro:bit.

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

4\.  **Risultato del test**

Dopo aver scaricato correttamente il codice sulla scheda, **alimentare esternamente (spostare l'interruttore DIP su ON)** e premere il pulsante reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

La matrice LED mostra un motivo sorridente e il servo ruota seguendo lo schema 0°~45°~90°~135°~180°~0°.

---