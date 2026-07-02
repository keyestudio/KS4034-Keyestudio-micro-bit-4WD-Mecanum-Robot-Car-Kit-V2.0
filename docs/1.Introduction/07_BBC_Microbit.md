## BBC Micro:bit

### **(1) Wat is Micro:bit?**

Micro:bit is een open‑source hardwareplatform gebaseerd op de ARM‑architectuur, gelanceerd door de British Broadcasting Corporation (BBC) samen met ARM, Barclays, element14, Microsoft en andere instanties. Het kernapparaat is een 32‑bit Arm Cortex‑M4 met FPU.

Het heeft ongeveer het formaat van een creditcard maar is erg krachtig. De Micro:bit hoofdprint is voorzien van vele componenten zoals een 5×5 LED‑dotmatrix, 2 programmeerbare knoppen, een versnellingsmeter, een kompas, een thermometer, een touch‑gevoelig logo, een MEMS‑microfoon, een low‑energy Bluetooth‑module en een zoemer, waardoor het in staat is diverse geluiden af te spelen zonder externe apparatuur.

Bovendien ondersteunt deze plaat een slaapstand om het batterijverbruik te verlagen; deze kan worden ingeschakeld door de Reset & Power‑knop aan de achterkant lang ingedrukt te houden.

Het Micro:bit‑ontwikkelbord is eenvoudig in gebruik en uitbreidbaar: het ontwerp van de gouden contacten (gold fingers) aan de onderzijde (edge connector) kan worden gebruikt om via krokodillenklemmen met diverse elektronische componenten te communiceren. Het kan sensorgegevens uitlezen, servo's en RGB‑lichten aansturen en een uitbreidingsbord opnemen om verschillende sensoren aan te sluiten.

Verder ondersteunt het verschillende codeertalen en grafische programmeerplatforms, is compatibel met bijna alle pc's en mobiele apparaten en vereist geen ingewikkelde driverinstallatie. Het bevat sterk geïntegreerde elektronische modules en een seriële poortmonitor voor eenvoudig debuggen.

Het bord wordt veelvuldig gebruikt voor het programmeren van videogames, licht‑ en geluidsinteracties, robotbesturing, wetenschappelijke experimenten, draagbare apparaten en andere creatieve uitvindingen zoals robots en muziekinstrumenten.

### **(2) Indeling**

![Img](./media/Introduction_5746e59b.png)

Voor meer informatie, raadpleeg de volgende links:

[https://tech.microbit.org/hardware/](https://tech.microbit.org/hardware/)

[https://microbit.org/new-microbit/](https://microbit.org/new-microbit/)

[https://www.microbit.org/get-started/user-guide/overview/](https://www.microbit.org/get-started/user-guide/overview/)

[https://microbit.org/get-started/user-guide/features-in-depth/](https://microbit.org/get-started/user-guide/features-in-depth/)

### **(3) Pinout**

![](./media/Introduction_ce0de295.png)

**Functies:**

|                            |                                                                                                    |
|----------------------------|----------------------------------------------------------------------------------------------------|
| GPIO                       | P0, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, P15, P16, P19, P20                |
| ADC/DAC                    | P0, P1, P2, P3, P4, P10                                                                            |
| IIC                        | P19 (SCL), P20 (SDA)                                                                               |
| SPI                        | P13 (SCK), P14 (MISO), P15 (MOSI)                                                                 |
| PWM (veel gebruikt)        | P0, P1, P2, P3, P4, P10                                                                            |
| PWM (weinig gebruikt)      | P5, P6, P7, P8, P9, P11, P12, P13, P14, P15, P16, P19, P20                                         |
| Bezet                      | P3 (LED Col3), P4 (LED Col1), P5 (Button A), P6 (LED Col4), P7 (LED Col2), P10 (LED Col5), P11 (Button B) |

Bekijk de officiële website voor meer details: [https://tech.microbit.org/hardware/edgeconnector/](https://tech.microbit.org/hardware/edgeconnector/)

[https://microbit.org/guide/hardware/pins/](https://microbit.org/guide/hardware/pins/)

### **(4) Voorzorgsmaatregelen bij gebruik van het Micro:bit‑mainboard:**

a\. Het wordt aanbevolen het bord te bedekken met een siliconen protector om kortsluiting van de gevoelige elektronische componenten te voorkomen.

b\. De IO‑poort is zwak in aansturing en kan slechts stromen onder de 300 mA verwerken. Sluit daarom geen apparaten met hoge stroomvereisten aan, zoals een MG995‑servo of DC‑motor, anders kan het verbranden. Bepaal bovendien de stroomvereisten van apparaten voordat u ze gebruikt; over het algemeen wordt aanbevolen het bord samen met een Micro:bit‑uitbreidingsbord te gebruiken.

c\. Het wordt aanbevolen het mainboard te voeden via de USB‑interface of met een 3V‑batterij. De IO‑poort van dit bord is 3V, dus het ondersteunt geen 5V‑sensoren. Als u 5V‑sensoren moet aansluiten, is een Micro:bit‑uitbreidingsbord vereist.

d\. Wanneer u gebruikmaakt van pinnen die gedeeld worden met de LED‑dotmatrix (P3, P4, P6, P7 en P10), kan het blokkeren van deze pinnen ten opzichte van de matrix of LED's ertoe leiden dat de LEDs willekeurig oplichten en dat de gegevens van aangesloten sensoren onjuist zijn.

e\. Pin 19 en 20 kunnen niet worden gebruikt als IO‑poorten, ook al geeft MakeCode mogelijk aan dat ze dat kunnen. Ze zijn alleen te gebruiken voor I2C‑communicatie.

f\. De 3V‑batterijpoort mag niet worden aangesloten op een batterij van meer dan 3,3V, anders raakt het mainboard beschadigd.

g\. Gebruik het niet op metalen oppervlakken om kortsluiting te vermijden.

Kortom: het Micro:bit V2‑mainboard is als een microcomputer die programmeren binnen handbereik brengt en digitale innovatie bevordert. Voor de programmeeromgeving biedt de BBC de website: [https://microbit.org/code/](https://microbit.org/code/), met een gebruiksvriendelijke grafische MakeCode‑omgeving.

---