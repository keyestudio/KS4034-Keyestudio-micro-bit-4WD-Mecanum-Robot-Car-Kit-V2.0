## Progetto 17：Line Tracking Sensor

### Progetto 17.1：Detect Line Tracking Sensor

![](./media/Makecode_ea7f6c8c.png)

1\. **Descrizione**

La scheda driver del motore del Keyestudio 4WD Mecanum Robot Car è fornita con un sensore di tracciamento linea a 3 canali, che utilizza moduli IR TCRT5000 e 3 potenziometri.

Il modulo IR TCRT5000 contiene un emettitore IR e un ricevitore IR. Quando i segnali infrarossi dell’emettitore vengono ricevuti dal ricevitore tramite riflessione, la resistenza del ricevitore cambia, il che si riflette generalmente in una variazione di tensione nel circuito.  

La resistenza varia in funzione dell’intensità dei segnali infrarossi ricevuti dal ricevitore, che dipende spesso dal colore della superficie riflettente e dalla distanza tra la superficie riflettente e il ricevitore. Durante la rilevazione, il nero è attivo ad alto livello e il bianco è attivo a basso livello. 

2\.  **Principio di funzionamento**

Quando l’auto percorre una strada bianca, il tubo emettitore IR installato sotto l’auto emette segnali infrarossi per rilevare la strada e il tubo ricevitore riceve i segnali e li rimanda. Quindi l’uscita fornisce un livello basso (0); quando rileva linee nere, fornisce un livello alto (1).

Dopo aver posizionato un foglio bianco sotto il 4WD Mecanum Robot Car, ruoteremo i potenziometri sul sensore di tracciamento a 3 vie. Quando il LED di indicazione sul modulo sensore è acceso, sollevare l’auto in modo che le due ruote del 4WD Mecanum Robot Car siano libere di girare. L’altezza del foglio bianco è di circa 1,5 cm; quando il LED del modulo sensore si spegne, la sensibilità è correttamente regolata.

3\.  **Preparazione**

- Inserire la scheda micro:bit nello slot del keyestudio 4WD Mecanum Robot Car V2.0

- Inserire le batterie nel portabatterie

- Impostare l’interruttore di alimentazione su ON

- Collegare il micro:bit al computer tramite un cavo USB

- Aprire la versione Web di Makecode

4\.  **Codice di test**

![](./media/Makecode_3683d83f.png)

Fare clic su “JavaScript” per visualizzare il corrispondente codice JavaScript: 

![](./media/Makecode_4b440616.png)

5\.  **Risultato del test**

Caricare il codice sulla scheda micro:bit e impostare l’interruttore POWER su ON. 

Aprire CoolTerm, fare clic su Options per selezionare SerialPort. Impostare la porta COM e il baud rate a 115200. Fare clic su “OK” e “Connect”.

![](./media/Makecode_ea164439.png)

![](./media/Makecode_b3a18bca.png)

![](./media/Makecode_f78128c1.png)

![](./media/Makecode_13238e98.png)

Il monitor seriale di CoolTerm mostra i segnali digitali letti dai sensori di tracciamento linea.

![](./media/Makecode_0141051a.png)

### Progetto 17.2：Tracking Smart Car

![Img](./media/Makecode_547634e4.png)

1\. **Descrizione**

In questa lezione combineremo un sensore di tracciamento linea con un motore per realizzare un'auto intelligente per il tracciamento della linea.

La scheda micro:bit analizzerà i segnali e controllerà l’auto intelligente per mostrare la funzione di tracciamento della linea.

2\. **Principio di funzionamento**

L’auto intelligente eseguirà movimenti differenti a seconda dei valori ricevuti dal sensore di tracciamento linea a 3 canali.

![Img](./media/Makecode_bbccdb34.png)

3\. **Preparazione**

- Inserire la scheda micro:bit nello slot del keyestudio 4WD Mecanum Robot Car V2.0

- Inserire le batterie nel portabatterie

- Impostare l’interruttore di alimentazione su ON

- Collegare il micro:bit al computer tramite un cavo USB

- Aprire la versione Web di Makecode

**Attenzione:** Il sensore di tracciamento a 3 vie deve essere utilizzato in ambienti senza interferenze infrarosse come la luce solare diretta. La luce solare contiene molta luce invisibile, come infrarossi e ultravioletti. In un ambiente con forte luce solare, il sensore a 3 vie potrebbe non funzionare correttamente.

4\.**Diagramma di flusso**

![Img](./media/Makecode_70f1fd80.png)


5\.  **Codice di test**

![](./media/Makecode_4b104155.png)

![Img](./media/Makecode_d36220cf.png)

![Img](./media/Makecode_4fff0a27.png)

![Img](./media/Makecode_ca91a31f.png)


Fare clic su “JavaScript” per visualizzare il corrispondente codice JavaScript:

![](./media/Makecode_f5caa06a.png)

![](./media/Makecode_8f5f07ec.png)

5\. **Risultato del test**

Caricare il codice sul micro:bit e impostare il POWER su ON; l’auto di tracciamento seguirà la linea nera andando avanti.

**Nota:** accendere l’interruttore sul retro dell’auto micro:bit; la larghezza della linea nera dovrebbe essere maggiore della larghezza del sensore di tracciamento linea.

Evitare di testare l’auto intelligente sotto luce intensa.