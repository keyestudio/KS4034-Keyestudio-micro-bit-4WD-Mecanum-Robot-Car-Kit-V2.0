### Progetto 3：Matrice LED 5×5

![](./media/Python_b855274f.png)

1\.  **Descrizione**

La matrice a punti è molto comune nella vita quotidiana e trova ampia applicazione in schermi pubblicitari LED, display dei piani degli ascensori, annunci alle fermate degli autobus e così via.
La matrice LED della scheda principale Micro: Bit contiene 25 diodi. In precedenza siamo riusciti a controllare un determinato LED tramite la sua posizione. Basandoci sulla stessa teoria, possiamo accendere più LED contemporaneamente per mostrare motivi, cifre e caratteri.

Inoltre, possiamo cliccare su “show icon” per scegliere il motivo che vogliamo visualizzare. Infine, possiamo anche progettare i nostri pattern.

2\.  **Preparazione**

A. Collegare la scheda principale micro:bit al computer tramite il cavo USB

B. Aprire la versione offline di Mu.

3\.  **Codice di test1**

È possibile aprire il file “5×5 LED Dot Matrix-1\.py” per importare il codice. È inoltre possibile inserire il codice direttamente nella finestra di modifica.

(**Nota: Tutte le parole e i simboli devono essere scritti in inglese.**)

![](./media/Python_00f15f0a.png)

```python
from microbit import *

val = Image("00900:""00900:""90909:""09990:""00900")

display.show(val)
```

Fare clic su “Check” per controllare gli errori nel codice. Il programma risulta errato se vengono mostrati sottolineature e cursori. 

![](./media/Python_a1197f5e.png)

Se il codice è corretto, collegare il micro:bit al computer e fare clic su “Flash” per scaricare il codice sulla scheda micro:bit.

![](./media/Python_1fd78e31.png)

4\.  **Risultato del test1**

Dopo aver scaricato con successo il codice sulla scheda, **alimentare tramite il cavo micro USB o un'alimentazione esterna (portare l'interruttore DIP su ON)** e premere il pulsante di reset sulla scheda.

![Img](./media/Python_bb3e1312.png)

Vedremo che la matrice 5×5 inizia a mostrare una freccia verso il basso ![](./media/Python_26c7d8c0.png).

5\.  **Codice di test2**

È possibile aprire il file “5×5 LED Dot Matrix-2\.py” per importare il codice. È inoltre possibile inserire il codice direttamente nella finestra di modifica.

(**Nota: Tutte le parole e i simboli devono essere scritti in inglese.**)

![](./media/Python_dc6eea45.png)

```python
from microbit import *
val = Image("00900:""00900:""90909:""09990:""00900")
display.show('1')
sleep(500)
display.show('2')
sleep(500)
display.show('3')
sleep(500)
display.show('4')
sleep(500)
display.show('5')
sleep(500)
display.show(val)
sleep(500)
display.scroll("hello!")
sleep(200)
display.show(Image.HEART)
sleep(500)
display.show(Image.ARROW_NE)
sleep(500)
display.show(Image.ARROW_SE)
sleep(500)
display.show(Image.ARROW_SW)
sleep(500)
display.show(Image.ARROW_NW)
sleep(500)
display.clear()
```

Fare clic su “Check” per controllare eventuali errori nel codice. Il programma risulta errato se vengono mostrati sottolineature e cursori. 

![](./media/Python_14bb490a.png)

Se il codice è corretto, collegare il micro:bit al computer e fare clic su “Flash” per scaricare il codice sulla scheda micro:bit.

![](./media/Python_a05c33d2.png)

6\.  **Risultato del test2**

Dopo aver scaricato con successo il codice sulla scheda, **alimentare tramite il cavo micro USB o un'alimentazione esterna (portare l'interruttore DIP su ON)** e premere il pulsante di reset sulla scheda.

![Img](./media/Python_bb3e1312.png)

Vedremo che la matrice 5×5 inizia a mostrare i numeri 1, 2, 3, 4 e 5 e quindi mostra alternativamente una freccia verso il basso ![](./media/Python_26c7d8c0.png), “Hello”, un motivo a forma di cuore ![](./media/Python_9b18b2b8.png), una freccia verso nord-est ![](./media/Python_364f2e35.png), poi verso sud-est
![](./media/Python_fb3ba009.png), poi verso sud-ovest ![](./media/Python_7ec21961.png) e infine verso nord-ovest ![](./media/Python_ced0bb41.png).

7\.  **Spiegazione del codice**

![Img](./media/Python_ef42956d.png)


6.  **Riferimento**

display.scroll() ：

Il display scorre per mostrare i valori; se si tratta di un intero o di un float, useremo str() per convertirlo in stringhe di caratteri.

Per maggiori dettagli, fare riferimento al link: [https://microbit-micropython.readthedocs.io/en/latest/utime.html](https://microbit-micropython.readthedocs.io/en/latest/utime.html)