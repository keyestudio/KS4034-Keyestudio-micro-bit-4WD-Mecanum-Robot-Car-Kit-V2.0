## Progetto 8: Rilevamento della luce

![](./media/Makecode_14063ef9.jpg)

[Fai clic per scaricare il codice per questa lezione](./Code/Light-Detection.hex)

### (1) Descrizione del progetto:

In questo progetto ci concentriamo sulla funzione di rilevamento della luce del Micro: Bit main board V2. Questo è ottenuto tramite la matrice di LED poiché la scheda principale non è dotata di un fotoresistore.

### (2) Componenti necessari:

Micro:bit main board V2

Cavo Micro USB

### (3) Codice di test:

Collegare il computer alla scheda micro:bit tramite cavo Micro USB e programmare nell'editor MakeCode,

![](./media/Makecode_38ffa3b8.gif)

Programma completo :

![](./media/Makecode_5b9a2acf.png)

### (4) Risultati del test:

Caricare il codice di test sul micro:bit main board V2, alimentare la scheda tramite il cavo USB e fare clic su "Show console Device".

Quando la matrice di punti LED è coperta con la mano, l'intensità luminosa visualizzata è circa 0; quando la matrice di punti LED è esposta alla luce, l'intensità luminosa mostrata aumenta con la luce come mostrato sotto.

![](./media/Makecode_11dd3c0b.gif)

Se si utilizza Windows 7 o 8 anziché Windows 10, Google Chrome non riuscirà ad associare i dispositivi. È necessario utilizzare il software di monitor seriale CoolTerm per leggere i dati.

È possibile aprire il software CoolTerm, fare clic su Options, selezionare SerialPort, impostare il COM port e impostare la baud rate su 115200 (dopo i test, la baud rate della comunicazione USB SerialPort sul Micro: Bit main board V2 è 115200), fare clic su OK e Connect. Il monitor seriale CoolTerm mostra il valore dell'intensità luminosa, come mostrato nelle figure seguenti :

![](./media/Makecode_3c6eae52.gif)

---