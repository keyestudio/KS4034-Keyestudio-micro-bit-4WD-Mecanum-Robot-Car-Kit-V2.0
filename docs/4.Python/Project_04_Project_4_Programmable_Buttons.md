### Progetto 4：Pulsanti programmabili

![](./media/Python_06be84fb.png)

1\.  **Descrizione**

![](./media/Python_b6d60ae2.png)

I pulsanti possono essere usati per controllare i circuiti. In un circuito integrato con un pulsante, il circuito viene chiuso quando si preme il pulsante e si riapre dopo il rilascio.

Entrambe le estremità del pulsante sembrano due montagne. C'è un fiume in mezzo. 
Il pezzo metallico interno collega i due lati per lasciare passare la corrente, proprio come costruire un ponte per collegare due montagne.

La struttura interna del pulsante è mostrata come segue: prima di premere il pulsante, 1, 2, 3 e 4 sono attivi. Tuttavia, 1 e 3 o 1 e 4 o 2 e 3 o 2 e 4 sono disconnessi; queste connessioni vengono abilitate solo quando il pulsante viene premuto. ![](./media/Python_d2a204e6.png)

La scheda principale micro:bit dispone di tre pulsanti: due sono pulsanti programmabili (contrassegnati con A e B) e quello sull'altro lato è un pulsante di reset. Premendo i due pulsanti programmabili si possono inviare tre segnali diversi. Possiamo premere il pulsante A o B da soli oppure premerli insieme e la matrice di LED mostrerà rispettivamente A, B e AB. Iniziamo.

2\.  **Preparazione**

A. Collegare la scheda principale micro:bit al computer tramite il cavo USB

B. Aprire la versione offline di Mu.

3\.  **Test Code1**

Aprire il software Mu e aprire il file “Programmable Buttons-1\.py” per importare il codice. È anche possibile inserire il codice direttamente nella finestra di modifica.

(**Nota: Tutte le parole e i simboli devono essere scritti in inglese.**)

![](./media/Python_2637f524.png)

```python
from microbit import *

while True:
    if button_a.is_pressed():
        display.show("A")
    elif button_a.is_pressed() and button_b.is_pressed():
        display.scroll("AB")
    elif button_b.is_pressed():
        display.show("B")
```
Fare clic su “Check” per esaminare gli errori nel codice. Il programma risulta errato se vengono visualizzate sottolineature e cursori.

![](./media/Python_a0f284f3.png)

Se il codice è corretto, collegare il micro:bit al computer e fare clic su “Flash” per scaricare il codice sulla scheda micro:bit.

![](./media/Python_5694d3ce.png)

4\.  **Risultato del test 1**

Dopo aver scaricato correttamente il codice sulla scheda, **alimentare tramite cavo micro USB o alimentazione esterna (portare l'interruttore DIP su ON)** e premere il pulsante di reset sulla scheda.

![Img](./media/Python_bb3e1312.png)

La matrice di LED 5*5 visualizza “A” se viene premuto il pulsante A, poi “B” se viene premuto il pulsante B, e “AB” se vengono premuti contemporaneamente A e B.

5\.  **Test Code2**

Aprire il software Mu e aprire il file “Programmable Buttons-2\.py” per importare il codice. È anche possibile inserire il codice direttamente nella finestra di modifica.

(**Nota: Tutte le parole e i simboli devono essere scritti in inglese.**)

![](./media/Python_1a1126f6.png)

![](./media/Python_94849305.png)

```python
from microbit import *
a = 0
b = 0
val1 = Image("00000:""00000:""00000:""00000:""00900")
val2 = Image("00000:""00000:""00000:""00900:""99999")
val3 = Image("00000:""00000:""00900:""99999:""99999")
val4 = Image("00000:""00900:""99999:""99999:""99999")
val5 = Image("00900:""99999:""99999:""99999:""99999")
val6 = Image("99999:""99999:""99999:""99999:""99999")
display.show(val1)

while True:
    while button_a.is_pressed() == True:
        sleep(10)
        if button_a.is_pressed() == False:
            a = a + 1
            if(a >= 5):
                a = 5
            break
    while button_b.is_pressed() == True:
        sleep(10)
        if button_b.is_pressed() == False:
            a = a - 1
            if(a <= 0):
                a = 0
            break
    if a == 0:
        display.show(val1)
    if a == 1:
        display.show(val2)
    if a == 2:
        display.show(val3)
    if a == 3:
        display.show(val4)
    if a == 4:
        display.show(val5)
    if a == 5:
        display.show(val6)
```
Fare clic su “Check” per esaminare gli errori nel codice. Il programma risulta errato se vengono visualizzate sottolineature e cursori.

![](./media/Python_21771d90.png)

![Img](./media/Python_8d257384.png)

Se il codice è corretto, collegare il micro:bit al computer e fare clic su “Flash” per scaricare il codice sulla scheda micro:bit.

![](./media/Python_84ba8cde.png)

![Img](./media/Python_8d257384.png)

6\.  **Risultato del test 2**

Dopo aver scaricato correttamente il codice sulla scheda, **alimentare tramite cavo micro USB o alimentazione esterna (portare l'interruttore DIP su ON)** e premere il pulsante di reset sulla scheda.

![Img](./media/Python_bb3e1312.png)

Se viene premuto il pulsante A, il numero di LED che diventano rossi aumenta; se viene premuto il pulsante B, il numero di LED rossi diminuisce.

7\.  **Spiegazione del codice**

![Img](./media/Python_b33858dc.png)

![Img](./media/Python_32bd1cca.png)

---