### Progetto 5：Rilevamento della temperatura

1\.  **Descrizione**

La scheda principale Micro:bit non è dotata di un sensore di temperatura, ma utilizza il sensore di temperatura integrato nel chip NFR52833 per la rilevazione della temperatura. Pertanto, la temperatura rilevata è più vicina alla temperatura del chip e potrebbe discostarsi dalla temperatura ambiente.

In questo progetto useremo il sensore per misurare la temperatura nell'ambiente corrente e visualizzare i risultati del test sul dispositivo di visualizzazione. Successivamente controlleremo la matrice LED per mostrare diversi schemi impostando l'intervallo di temperatura rilevato dal sensore.

**Nota: il sensore di temperatura della scheda principale Micro:bit è mostrato di seguito:**

![](./media/Python_206c8ec1.png)

2\.  **Preparazione**

A. Collegare la scheda principale micro:bit al computer tramite cavo USB

B. Aprire la versione offline di Mu.

3\.  **Codice di test1**

Aprire il software Mu e importare il file “Temperature Measurement -1\.py “. È inoltre possibile inserire il codice nella finestra di modifica manualmente.

(**Nota: Tutte le parole e i simboli devono essere scritti in inglese.**)

![](./media/Python_03cbb6e9.png)

```python
from microbit import *

while True:

    Temperature = temperature()

    print("Temperature:", Temperature, "C")

    sleep(500)
```

Fare clic su “Check” per verificare la presenza di errori nel codice. Il programma è errato se vengono visualizzate sottolineature e cursori. 

![](./media/Python_7b437c2d.png)

Se il codice è corretto, collegare il micro:bit al computer e fare clic su “Flash” per scaricare il codice sulla scheda micro:bit.

![](./media/Python_193065ab.png)

4\.  **Risultato del test1**

Dopo aver scaricato correttamente il codice sulla scheda, **alimentare tramite cavo micro USB o alimentazione esterna (portare l'interruttore DIP su ON)**. Fare clic su “REPL” e premere il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

La finestra REPL mostrerà quindi il valore della temperatura ambiente, come indicato di seguito: (C indica l'unità di temperatura)

![](./media/Python_d08386d8.png)

5\.  **Codice di test2**

Aprire il software Mu e importare il file “Temperature Measurement -2\.py “. È inoltre possibile inserire il codice nella finestra di modifica manualmente.

(**Nota: Tutte le parole e i simboli devono essere scritti in inglese.**)

Il valore di temperatura può essere impostato in conformità con la temperatura reale.

![](./media/Python_c6456d78.png)

```python
from microbit import *

while True:

    if temperature() >= 35:
        display.show(Image.HEART)

    else:
        display.show(Image.HEART_SMALL)
```

Fare clic su “Check” per verificare la presenza di errori nel codice. Il programma è errato se vengono visualizzate sottolineature e cursori. 

![](./media/Python_709d3031.png)

Se il codice è corretto, collegare il micro:bit al computer e fare clic su “Flash” per scaricare il codice sulla scheda micro:bit.

![](./media/Python_06f7542e.png)

6\.  **Risultato del test2**

Dopo aver scaricato correttamente il codice sulla scheda, **alimentare tramite cavo micro USB o alimentazione esterna (portare l'interruttore DIP su ON)** e premere il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

 Quando la temperatura ambiente è inferiore a 35℃, la matrice di LED 5×5 mostra ![](./media/Python_034dc0d5.png). Quando la temperatura è uguale o superiore a 35℃, appare il motivo ![](./media/Python_ebfaeac9.png).

7\.  **Spiegazione del codice**

![Img](./media/Python_d7cdc397.png)

---