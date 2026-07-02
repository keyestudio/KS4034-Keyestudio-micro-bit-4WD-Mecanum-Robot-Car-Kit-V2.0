## BBC Micro:bit

### **(1) Che cos'è Micro:bit?**

Micro:bit è una piattaforma hardware open source basata sull'architettura ARM, lanciata dalla British Broadcasting Corporation (BBC) insieme ad ARM, Barclays, element14, Microsoft e altre istituzioni. Il dispositivo centrale è un microprocessore Arm Cortex‑M4 a 32 bit con FPU.

Ha le dimensioni di una carta di credito ma è molto potente. La scheda principale Micro:bit è dotata di numerosi componenti come una matrice LED 5×5, 2 pulsanti programmabili, un accelerometro, una bussola, un termometro, un logo sensibile al tocco, un microfono MEMS, un modulo Bluetooth a bassa energia e un buzzer, permettendo di riprodurre diversi suoni senza dispositivi esterni.

Inoltre, questa scheda supporta una modalità sleep per ridurre il consumo della batteria, attivabile tenendo premuto a lungo il pulsante Reset & Power sul retro.

La scheda di sviluppo Micro:bit è facile da usare ed espandere: il design dei contatti dorati (gold finger) sul lato inferiore consente l'interazione con vari componenti elettronici tramite morsetti a coccodrillo. È in grado di leggere i dati dei sensori, controllare servomotori e luci RGB e ospitare una scheda di espansione per collegare vari sensori.

Inoltre supporta diversi linguaggi e piattaforme di programmazione grafica, è compatibile con quasi tutti i PC e dispositivi mobili e non richiede driver complessi. Dispone di moduli elettronici altamente integrati e di una funzione di monitoraggio della porta seriale per un debug semplice.

La scheda è ampiamente utilizzata nella programmazione di videogiochi, interazioni luce‑suono, controllo di robot, esperimenti scientifici, dispositivi indossabili e in invenzioni creative come robot e strumenti musicali.

### **(2) Layout**

![Img](./media/Introduction_5746e59b.png)

Per maggiori informazioni consultare i seguenti link:

[https://tech.microbit.org/hardware/](https://tech.microbit.org/hardware/)

[https://microbit.org/new-microbit/](https://microbit.org/new-microbit/)

[https://www.microbit.org/get-started/user-guide/overview/](https://www.microbit.org/get-started/user-guide/overview/)

[https://microbit.org/get-started/user-guide/features-in-depth/](https://microbit.org/get-started/user-guide/features-in-depth/)

### **(3) Pin out**

![](./media/Introduction_ce0de295.png)

**Funzioni:**

|                            |                                                                                                    |
|----------------------------|----------------------------------------------------------------------------------------------------|
| GPIO                       | P0, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, P15, P16, P19, P20                |
| ADC/DAC                    | P0, P1, P2, P3, P4, P10                                                                            |
| IIC                        | P19 (SCL), P20 (SDA)                                                                               |
| SPI                        | P13 (SCK), P14 (MISO), P15 (MOSI)                                                                 |
| PWM (usato frequentemente) | P0, P1, P2, P3, P4, P10                                                                            |
| PWM (poco usato)           | P5, P6, P7, P8, P9, P11, P12, P13, P14, P15, P16, P19, P20                                         |
| Occupato                   | P3 (LED Col3), P4 (LED Col1), P5 (Button A), P6 (LED Col4), P7 (LED Col2), P10 (LED Col5), P11 (Button B) |

Consultare il sito ufficiale per maggiori dettagli: [https://tech.microbit.org/hardware/edgeconnector/](https://tech.microbit.org/hardware/edgeconnector/)

[https://microbit.org/guide/hardware/pins/](https://microbit.org/guide/hardware/pins/)

### **(4) Precauzioni per l'uso della scheda madre Micro:bit:**

a\. Si consiglia di coprire la scheda con una protezione in silicone per evitare cortocircuiti sui suoi delicati componenti elettronici.

b\. Le porte IO hanno una capacità di pilotaggio limitata e possono gestire correnti inferiori a 300 mA. Pertanto, non collegare dispositivi ad alto assorbimento, come servomotori MG995 o motori DC, altrimenti possono bruciarsi. Verificare sempre i requisiti di corrente dei dispositivi prima dell'uso; in genere è consigliato utilizzare la scheda insieme a una scheda di espansione Micro:bit.

c\. Si raccomanda di alimentare la scheda principale tramite la porta USB o con una batteria da 3V. Le porte IO sono a 3V, quindi non supportano sensori a 5V. Per collegare sensori a 5V è necessario un modulo di espansione Micro:bit.

d\. Quando si utilizzano i pin condivisi con la matrice LED (P3, P4, P6, P7 e P10), se questi pin sono schermati rispetto alla matrice o ai LED, questi possono visualizzare valori casuali e i dati dei sensori collegati potrebbero essere errati.

e\. I pin 19 e 20 non possono essere usati come porte IO anche se MakeCode può mostrarlo. Possono essere usati solo per comunicazione I2C.

f\. Alla presa batteria da 3V non devono essere collegate batterie superiori a 3,3V, altrimenti la scheda principale potrebbe danneggiarsi.

g\. Vietato utilizzare la scheda su superfici metalliche per evitare cortocircuiti.

In sintesi, la scheda principale Micro:bit V2 è come un microcomputer che mette la programmazione a portata di mano e favorisce l'innovazione digitale. Per l'ambiente di programmazione la BBC fornisce il sito: [https://microbit.org/code/](https://microbit.org/code/), che offre un'interfaccia grafica MakeCode facile da usare.

---