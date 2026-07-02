### Progetto 6：Geomagnetic Sensor

![](./media/Python_26d107ae.png)

1\.  **Descrizione**

Questo progetto introduce principalmente l’uso del sensore geomagnetico del micro:bit. Oltre a rilevare l’intensità del campo magnetico, può anche essere usato per determinare la direzione, che è una parte importante del sistema di riferimento di rotta e assetto (AHRS).

Utilizza il magnetometro triassiale FreescaleMAG3110. La sua interfaccia I2C comunica con l’esterno, l’intervallo è ±1000µT e la velocità massima di aggiornamento dei dati è 80Hz. In combinazione con un accelerometro, può calcolare la posizione. Inoltre è applicato al rilevamento magnetico e ai blocchi bussola.

Possiamo poi leggere il valore rilevato per determinare l’orientamento. È necessario calibrare la scheda micro:bit quando il sensore magnetico è in funzione. Il metodo di calibrazione corretto è ruotare la scheda micro:bit.

Inoltre, gli oggetti nelle vicinanze possono influenzare la precisione delle letture e della calibrazione.

2\.  **Preparazione**

A. Collegare la scheda principale micro:bit al computer tramite il cavo USB

B. Aprire la versione offline di Mu.

3\.  **Test Code1**

Avviare il software Mu e aprire il file “Magnetic sensor -1\.py” per importare il codice. È anche possibile inserire il codice direttamente nella finestra di modifica.

(**Nota: Tutte le parole e i simboli devono essere scritti in inglese**.)

![](./media/Python_1366c5ed.png)

```python
from microbit import *

compass.calibrate()

while True:

    if button_a.is_pressed():
        display.scroll(compass.heading())
```
Fare clic su “Check” per esaminare gli errori nel codice. Il programma è errato se vengono mostrati sottolineature e cursori. 

![](./media/Python_5bfe40c4.png)

Se il codice è corretto, collegare il micro:bit al computer e fare clic su “Flash” per scaricare il codice sulla scheda micro:bit.

![](./media/Python_695d8f29.png)

4\.  **Risultato del test1**

Dopo aver scaricato correttamente il codice sulla scheda, **alimentare tramite cavo micro USB o alimentazione esterna (portare l’interruttore DIP su ON)** e premere il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

 La matrice di LED mostra “TILT TO FILL SCREEN”. Premendo il pulsante A, la scheda richiede di calibrare la bussola. Quindi si accede alla pagina di calibrazione. Ruotare la scheda finché tutti i 25 LED rossi sono accesi, come mostrato di seguito.

![](./media/Python_c8fd6670.jpg)

Dopo ciò appare un motivo a sorriso ![](./media/Python_a3b91e3e.png), che implica che la calibrazione è completata. Quando il processo di calibrazione è terminato, premendo il pulsante A la lettura del magnetometro verrà mostrata direttamente sullo schermo. Le direzioni nord, est, sud e ovest corrispondono rispettivamente a 0°, 90°, 180° e 270°.

5\.  **Test Code2**

Per l’immagine sottostante, la freccia punterà in alto a destra quando il valore è compreso tra 292,5 e 337,5. Poiché 0,5 non può essere inserito nel codice, i valori che utilizziamo sono 293 e 338.

Aggiungere poi altre istruzioni per creare un codice completo.

![](./media/Python_d1a4e9f6.png)

Avviare il software Mu e aprire il file “Magnetic sensor -2\.py” per importare il codice. È anche possibile inserire il codice direttamente nella finestra di modifica.

(**Nota: Tutte le parole e i simboli devono essere scritti in inglese.**)

![](./media/Python_5b0d8e26.png)

```python
from microbit import *
compass.calibrate()
x = 0
while True:
    x = compass.heading()
    if x >= 293 and x < 338:
        display.show(Image("00999:""00099:""00909:""09000:""90000"))
    elif x >= 23 and x < 68:
        display.show(Image("99900:""99000:""90900:""00090:""00009"))
    elif x >= 68 and x < 113:
        display.show(Image("00900:""09000:""99999:""09000:""00900"))
    elif x >= 113 and x < 158:
        display.show(Image("00009:""00090:""90900:""99000:""99900"))
    elif x >= 158 and x < 203:
        display.show(Image("00900:""00900:""90909:""09990:""00900"))
    elif x >= 203 and x < 248:
        display.show(Image("90000:""09000:""00909:""00099:""00999"))
    elif x >= 248 and x < 293:
        display.show(Image("00900:""00090:""99999:""00090:""00900"))
    else:
        display.show(Image("00900:""09990:""90909:""00900:""00900"))

```

Fare clic su “Check” per esaminare gli errori nel codice. Il programma è errato se vengono mostrati sottolineature e cursori. 

![](./media/Python_42389bcf.png)

Se il codice è corretto, collegare il micro:bit al computer e fare clic su “Flash” per scaricare il codice sulla scheda micro:bit.

![](./media/Python_bedc607a.png)

6\.  **Risultato del test**

Dopo aver scaricato correttamente il codice sulla scheda, **alimentare tramite cavo micro USB o alimentazione esterna (portare l’interruttore DIP su ON)** e premere il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

Dopo la calibrazione, ruotare la scheda micro:bit, quindi la matrice di LED visualizza i simboli di direzione. 

7\.  **Spiegazione del codice**

![Img](./media/Python_76f66bb0.png)

---