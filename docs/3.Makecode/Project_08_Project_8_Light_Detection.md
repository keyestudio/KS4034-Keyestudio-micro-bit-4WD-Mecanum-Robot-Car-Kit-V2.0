## Project 8: Lichtdetectie

![](./media/Makecode_14063ef9.jpg)

[Klik hier om code voor deze les te downloaden](./Code/Light-Detection.hex)

### (1) Projectbeschrijving:

In dit project richten we ons op de lichtdetectiefunctie van de Micro: Bit main board V2. Dit wordt gerealiseerd door de LED-dotmatrix, aangezien de hoofdprint niet is uitgerust met een lichtafhankelijke weerstand.

### (2) Benodigde componenten:

Micro:bit main board V2

Micro USB-kabel

### (3) Testcode:

Verbind de computer met de micro:bit board via de Micro USB-kabel en programmeer in de MakeCode-editor,

![](./media/Makecode_38ffa3b8.gif)

Volledig programma :

![](./media/Makecode_5b9a2acf.png)

### (4) Testresultaten:

Upload de testcode naar het micro:bit main board V2, voed de board via de USB-kabel en klik op "Show console Device".

Wanneer de LED-dotmatrix met de hand wordt afgedekt, is de weergegeven lichtintensiteit ongeveer 0; wanneer de LED-dotmatrix aan licht wordt blootgesteld, wordt de weergegeven lichtintensiteit sterker naarmate het licht toeneemt, zoals hieronder weergegeven.

![](./media/Makecode_11dd3c0b.gif)

Als je Windows 7 of 8 gebruikt in plaats van Windows 10, kan Google Chrome de apparaten niet koppelen. Je moet de CoolTerm seriële monitor-software gebruiken om gegevens te lezen.

Je kunt de CoolTerm-software openen, op Options klikken, SerialPort selecteren, de COM port instellen en de baud rate op 115200 zetten (na testen is de baud rate van USB SerialPort-communicatie op het Micro: Bit main board V2 115200), klik op OK en Connect. De CoolTerm seriële monitor toont de waarde van de lichtintensiteit, zoals in de onderstaande afbeeldingen:

![](./media/Makecode_3c6eae52.gif)