### Progetto 17: Sensore di tracciamento della linea

#### Progetto 17.1: Rilevamento del sensore di tracciamento della linea

![](./media/Python_ea7f6c8c.png)

1\. **Descrizione**

La scheda driver dei motori del Keyestudio 4WD Mecanum Robot Car è dotata di un sensore di tracciamento della linea a 3 canali, che utilizza tubi IR TCRT5000 e 3 potenziometri.

Il tubo IR TCRT5000 contiene un emettitore IR e un ricevitore IR. Quando i segnali infrarossi emessi vengono riflessi e ricevuti dal tubo ricevente, la resistenza del ricevitore cambierà, il che si riflette generalmente nella variazione di tensione sul circuito.

La resistenza varia a seconda dell'intensità dei segnali infrarossi ricevuti dal ricevitore, che dipende spesso dal colore della superficie riflettente e dalla distanza tra la superficie riflettente e il ricevitore. Durante il rilevamento, il nero è attivo ad alto livello e il bianco è attivo a basso livello.

2\.  **Principio di funzionamento**

Quando l'auto passa sopra una strada bianca, il tubo emettitore IR installato sotto l'auto emette segnali infrarossi per rilevare la strada e il tubo ricevente riceve i segnali inviando la risposta. Quindi l'uscita fornisce livello basso (0); quando rileva linee nere, fornisce livello alto (1).

La porta integrata del sensore di tracciamento a 3 canali sulla 4WD Mecanum Robot Car è collegata alle porte di raccolta G, 5V, P10, P4 e P3 sulla scheda di espansione micro:bit, e viene controllata da P10, P4 e P3 del micro:bit. La coppia IR TCRT5000 sinistra sul sensore è controllata da P3, quella centrale da P4 e quella destra da P10.

Dopo aver posto un foglio bianco sul fondo della 4WD Mecanum Robot Car, ruoteremo i potenziometri sul sensore di tracciamento a 3 vie. Quando la spia sul modulo sensore è accesa, sollevare l'auto in modo che le due ruote del 4WD Mecanum Robot Car siano sollevate. L'altezza del foglio bianco è di circa 1,5 cm; quando la spia sul modulo sensore si spegne, regolare la sensibilità.

**Nota che poiché la matrice a punti 5*5 usa le porte P3P4P6P7P10, dobbiamo disattivare la funzione della matrice a punti quando si usa il sensore di tracciamento della linea.**

3\.  **Preparazione**

- Inserire la scheda micro:bit nello slot del keyestudio 4WD Mecanum Robot Car V2.0

- Inserire le batterie nel vano porta batterie

- Portare l'interruttore di alimentazione su ON

- Collegare il micro:bit al computer tramite un cavo USB

- Aprire la versione offline di Mu.

4\.  **Codice di prova**

Aprire il software Mu e aprire il file “Line tracking detection\.py” per importare il codice. È anche possibile inserire il codice nella finestra di modifica manualmente.

(**Nota: Tutte le parole e i simboli in inglese devono essere scritti in inglese**.)

Fare clic su “Check” per verificare errori nel codice. Il programma presenterà errori se vengono mostrati sottolineature e cursori.

Se il codice è corretto, collegare il micro:bit al computer e fare clic su “Flash” per caricare il codice sulla scheda micro:bit.

![](./media/Python_2c7b1c21.png)

```python
from microbit import *
display.off()

val_L = 0
val_C = 0
val_R = 0
while True:
    val_L = pin3.read_digital()
    val_C = pin4.read_digital()
    val_R = pin10.read_digital()
    print("digital signal:", end = ' ')
    print(val_L, end = ' ')
    print(val_C, end = ' ')
    print(val_R)
    sleep(200)
```

5\.  **Risultato del test**

Dopo aver caricato correttamente il codice sulla scheda e senza scollegare il cavo USB, fare clic su “REPL” e poi premere il pulsante di reset.

![Img](./media/Python_bb3e1312.png)

Le letture rilevate dal tubo IR TCRT5000 sinistro verranno visualizzate nel monitor.

Quando il tubo IR TCRT5000 sinistro rileva un oggetto bianco, verrà mostrato 0 e il relativo indicatore sarà acceso; quando viene rilevato solo un oggetto nero, verrà visualizzato 1 e l'indicatore sarà spento, come mostrato di seguito:

![](./media/Python_6a25b450.png)

6\.  **Spiegazione del codice**

![Img](./media/Python_5dad345e.png)


#### Progetto 17.2: Auto intelligente con tracciamento

![](./media/Python_f0b62e0f.jpg)

1\. Descrizione

In questa lezione combineremo un sensore di tracciamento della linea con i motori per realizzare un'auto intelligente che segua una linea.

La scheda micro:bit analizzerà i segnali e controllerà l'auto per implementare la funzione di tracciamento della linea.

2\.  **Principio di funzionamento**

L'auto eseguirà movimenti differenti in base ai valori ricevuti dal sensore di tracciamento della linea a 3 canali.

![Img](./media/Python_e672c637.png)

3\.  **Preparazione**

- Inserire la scheda micro:bit nello slot del keyestudio 4WD Mecanum Robot Car V2.0

- Inserire le batterie nel vano porta batterie

- Portare l'interruttore di alimentazione su ON

- Collegare il micro:bit al computer tramite un cavo USB

- Aprire la versione offline di Mu.

**Avvertenza:** Il sensore di tracciamento a 3 vie dovrebbe essere usato in un ambiente privo di interferenze infrarosse come la luce solare. La luce solare contiene molta luce invisibile, come infrarossi e ultravioletti. In un ambiente con forte luce solare il sensore a 3 vie potrebbe non funzionare correttamente.

4\.  **Diagramma di flusso**

![Img](./media/Python_47856ed2.png)

5\.  **Codice di prova**

Aprire il software Mu e aprire il file “Line tracking car\.py” per importare il codice. È anche possibile inserire il codice nella finestra di modifica manualmente.

(**Nota: Tutte le parole e i simboli in inglese devono essere scritti in inglese**.)

Fare clic su “Files” per importare il file libreria “keyes_mecanum_Car.py” nella micro:bit.

Fare clic su “Check” per verificare errori nel codice. Il programma presenterà errori se vengono mostrati sottolineature e cursori.

Se il codice è corretto, collegare il micro:bit al computer e fare clic su “Flash” per caricare il codice sulla scheda micro:bit.

![](./media/Python_bd395cbe.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()
display.off()

val_L = 0
val_C = 0
val_R = 0
while True:
    val_L = pin3.read_digital()
    val_C = pin4.read_digital()
    val_R = pin10.read_digital()
    if val_C == 0:
        if val_L == 0 and val_R == 1:
            mecanumCar.Motor_Upper_L(1, 80)
            mecanumCar.Motor_Lower_L(1, 80)
            mecanumCar.Motor_Upper_R(0, 80)
            mecanumCar.Motor_Lower_R(0, 80)
        elif val_L == 1 and val_R == 0:
            mecanumCar.Motor_Upper_L(0, 80)
            mecanumCar.Motor_Lower_L(0, 80)
            mecanumCar.Motor_Upper_R(1, 80)
            mecanumCar.Motor_Lower_R(1, 80)
        else:
            mecanumCar.Motor_Upper_L(0, 0)
            mecanumCar.Motor_Lower_L(0, 0)
            mecanumCar.Motor_Upper_R(0, 0)
            mecanumCar.Motor_Lower_R(0, 0)
    else :
        if val_L == 0 and val_R == 1:
            mecanumCar.Motor_Upper_L(1, 80)
            mecanumCar.Motor_Lower_L(1, 80)
            mecanumCar.Motor_Upper_R(0, 80)
            mecanumCar.Motor_Lower_R(0, 80)
        elif val_L == 1 and val_R == 0:
            mecanumCar.Motor_Upper_L(0, 80)
            mecanumCar.Motor_Lower_L(0, 80)
            mecanumCar.Motor_Upper_R(1, 80)
            mecanumCar.Motor_Lower_R(1, 80)
        else:
            mecanumCar.Motor_Upper_L(1, 80)
            mecanumCar.Motor_Lower_L(1, 80)
            mecanumCar.Motor_Upper_R(1, 80)
            mecanumCar.Motor_Lower_R(1, 80)
```
6\.  **Risultato del test**

Dopo aver caricato correttamente il codice sulla scheda, fornire alimentazione esterna (**portare l'interruttore DIP su ON**) e premere il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

L'auto di tracciamento si muove in avanti seguendo la linea nera.

**Nota:** （1）La larghezza della linea nera dovrebbe essere uguale o maggiore della larghezza del sensore di tracciamento della linea durante il tracciamento.

（2）Evitare di testare l'auto intelligente sotto luce intensa.


7\.  **Spiegazione del codice**

![Img](./media/Python_b16f9d7b.png)

![Img](./media/Python_35f35a4c.png)