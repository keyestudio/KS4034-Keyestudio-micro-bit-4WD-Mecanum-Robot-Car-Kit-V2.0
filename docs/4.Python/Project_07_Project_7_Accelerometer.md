### Progetto 7：Accelerometer

![](./media/Python_26d107ae.png)

1\.  **Descrizione**

La scheda principale micro: bit main board V2 è dotata di un sensore di accelerazione gravitazionale LSM303AGR integrato, noto anche come accelerometro, con risoluzione di 8/10/12 bit. Nella sezione del codice è possibile impostare la portata a 1g, 2g, 4g e 8g.

Utilizziamo spesso un accelerometro per rilevare lo stato delle macchine.

In questo progetto mostreremo come misurare la posizione della scheda con l'accelerometro. Successivamente esamineremo i dati grezzi triassiali forniti dall'accelerometro.

2\.  **Preparazione**

A. Collegate la scheda micro:bit main board al computer tramite il cavo USB.

B. Aprite la versione offline di Mu.

3\.  **Codice di test1**

Avviate il software Mu e aprite il file “Three-axis acceleration sensor -1\.py“ per importare il codice. Potete anche inserire il codice manualmente nella finestra di editing.

(**Nota: Tutte le parole e i simboli devono essere scritti in inglese.**)

![](./media/Python_f20f5b58.png)

```python
from microbit import *

while True:
    gesture = accelerometer.current_gesture()

    if gesture == "shake":
        display.show("1")
    if gesture == "up":
        display.show("2")
    if gesture == "down":
        display.show("3")
    if gesture == "face up":
        display.show("4")
    if gesture == "face down":
        display.show("5")
    if gesture == "left":
        display.show("6")
    if gesture == "right":
        display.show("7")
    if gesture == "freefall":
        display.show("8")
```

Cliccate su “Check” per verificare la presenza di errori nel codice. Il programma è errato se vengono mostrati sottolineature e cursori. 

![](./media/Python_07e4b578.png)

Se il codice è corretto, collegate il micro:bit al computer e cliccate su “Flash” per scaricare il codice sulla scheda micro:bit.

![](./media/Python_eb56750b.png)

4\.  **Risultato del test1**

Dopo aver scaricato correttamente il codice sulla scheda, **alimentate tramite il cavo micro USB o una fonte di alimentazione esterna (impostare l'interruttore DIP su ON)** e premete il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

Quando scuotiamo il micro: bit main board, in qualsiasi direzione, la matrice LED visualizza la cifra “1”.

Quando è mantenuto in verticale (con il logo sopra la matrice LED), appare il numero 2.

![](./media/Python_b91421df.jpg)

Quando viene tenuto a testa in giù (con il logo sotto la matrice LED), viene visualizzato come di seguito.

![](./media/Python_69e81587.jpg)

Quando è posizionato fermo sulla scrivania, con il lato anteriore rivolto verso l'alto, compare il numero 4.

![](./media/Python_9e08cb69.jpg)

Quando è posizionato fermo sulla scrivania, con il lato posteriore rivolto verso l'alto, compare il numero 5.

Quando la scheda è inclinata verso sinistra, la matrice LED mostra il numero 6, come mostrato di seguito:

![](./media/Python_81fa2ce1.jpg)

Quando la scheda è inclinata verso destra, la matrice LED visualizza il numero 7, come mostrato di seguito：

![](./media/Python_fc13912b.jpg)

Quando la scheda viene colpita a terra, questo processo può essere considerato come una caduta libera e la matrice LED mostra il numero 8. (Si noti che questo test non è raccomandato perché potrebbe danneggiare la scheda principale.)

**Attenzione: Se desiderate provare questa funzione, potete anche impostare l'accelerazione a 3g, 6g o 8g.**

5\.  **Codice di test2**

Avviate il software Mu e aprite il file “Three-axis acceleration sensor -2\.py“ per importare il codice. Potete anche inserire il codice manualmente nella finestra di editing.

(**Nota: Tutte le parole e i simboli devono essere scritti in inglese.**)

![](./media/Python_0f7ccf57.png)

```python
from microbit import *

while True:

    x = accelerometer.get_x()

    y = accelerometer.get_y()

    z = accelerometer.get_z()

    print("x, y, z:", x, y, z)

    sleep(100)
```
Cliccate su “Check” per verificare la presenza di errori nel codice. Il programma è errato se vengono mostrati sottolineature e cursori. 

![](./media/Python_0ed2221e.png)

Se il codice è corretto, collegate il micro:bit al computer e cliccate su “Flash” per scaricare il codice sulla scheda micro:bit.

![](./media/Python_35c4c76b.png)

6\.  **Risultato del test2**

Dopo aver scaricato correttamente il codice sulla scheda, **alimentate tramite il cavo micro USB o una fonte di alimentazione esterna (impostare l'interruttore DIP su ON)**. Cliccate su “REPL” e premete il pulsante di reset sul micro:bit.

![Img](./media/Python_bb3e1312.png)

Quindi la finestra REPL mostrerà i valori dell'accelerazione sugli assi X, Y e Z come mostrato di seguito:

![](./media/Python_940cfcf7.png)

Facendo riferimento al manuale dati MMA8653FC e allo schema hardware del micro: bit main board, le coordinate dell'accelerometro del micro: bit sono riportate nella figura seguente:

![](./media/Python_ebd0d44d.png)

7\.  **Spiegazione del codice**

![Img](./media/Python_d533d72c.png)

![Img](./media/Python_89d95342.png)

---