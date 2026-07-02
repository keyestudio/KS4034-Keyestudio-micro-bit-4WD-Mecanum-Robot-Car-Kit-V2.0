### Progetto 8：Rilevamento della luce

![](./media/Python_b855274f.png)

1\.  **Descrizione**

In questo progetto ci concentreremo sulla funzione di rilevamento della luce della scheda principale Micro: Bit. È ottenuta dalla LED dot matrix poiché la scheda principale non è dotata di una fotoresistenza.

2\.  **Preparazione**

A. Collegate il micro:bit main board al computer tramite il cavo USB

B. Aprite la versione offline di Mu.

3\.  **Codice di prova**

Avviate il software Mu e aprite il file “Detect Light Intensity by Microbit\.py” per importare il codice. È anche possibile inserire il codice direttamente nella finestra di modifica.

(**Nota: Tutte le parole e i simboli in inglese devono essere scritti in inglese.**)

![](./media/Python_b4f06503.png)

```python
from microbit import *

while True:

    Lightintensity = display.read_light_level()

    print("Light intensity:", Lightintensity)

    sleep(100)
```
Cliccate su “Check” per controllare la presenza di errori nel codice. Il programma risulta errato se vengono mostrati sottolineature e cursori.

![](./media/Python_b41eeb0f.png)

Se il codice è corretto, collegate il micro:bit al computer e cliccate su “Flash” per scaricare il codice sulla scheda micro:bit.

![](./media/Python_7baa2190.png)

4\.  **Risultato del test**

Dopo aver scaricato correttamente il codice sulla scheda, **alimentate tramite il cavo micro USB o un'alimentazione esterna (turn the DIP switch to ON)**. Cliccate su “REPL” e premete il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

La finestra REPL mostrerà quindi il valore dell'intensità luminosa, come mostrato di seguito.

Quando la LED dot matrix è coperta dalla mano, l'intensità luminosa mostrata è approssimativamente 0; quando la LED dot matrix è esposta alla luce, l'intensità luminosa visualizzata aumenta con l'intensità della luce.

![](./media/Python_778d89d6.png)

5\.  **Spiegazione del codice**

![Img](./media/Python_dcdc4536.png)

---