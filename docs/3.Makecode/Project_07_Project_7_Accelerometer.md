## Project 7: Accelerometer

![](./media/Makecode_66670811.jpg)

[Klik hier om code 1 voor deze les te downloaden](./Code/Accelerometer.hex)

[Klik hier om code 2 voor deze les te downloaden](./Code/Accelerometer2.hex)

### (1)Projectbeschrijving:

De Micro: Bit main board V2 heeft een ingebouwde LSM303AGR zwaartekrachtversnellingssensor, ook wel accelerometer genoemd, met een resolutie van 8/10/12 bits. In de code-sectie kan het bereik worden ingesteld op 1g, 2g, 4g en 8g.

We gebruiken vaak versnellingsmeters om de status van machines te detecteren. In dit project leggen we uit hoe je met de accelerometer de positie van de bord kunt meten en bekijken we vervolgens de ruwe driedimensionale gegevens die de accelerometer uitstuurt.

### (2)Benodigde componenten:

Micro:bit main board V2

Micro USB-kabel

### (3)Testcode 1:

Verbind de computer met het micro:bit-bord via een Micro USB-kabel en programmeer in de MakeCode-editor,

![](./media/Makecode_2cd48603.gif)

Volledig programma:

![](./media/Makecode_ba28162b.png)

### (4)Testresultaten 1:

Nadat Test Code 1 naar het micro:bit V2-bord is geüpload, zorgt het veranderen van de oriëntatie van het bord ervoor dat de 5x5 stippenmatrix verschillende cijfers weergeeft.

![](./media/Makecode_2e6708e6.gif)

Als we het Micro: Bit main board V2 schudden, ongeacht de richting, toont de LED-stippenmatrix het cijfer "1".

Als het rechtop wordt gehouden (het logo boven de LED-stippenmatrix), verschijnt het nummer 2.

![](./media/Makecode_67247ae1.jpg)

Als het ondersteboven wordt gehouden (het logo onder de LED-stippenmatrix), wordt het als hieronder weergegeven.

![](./media/Makecode_1668a9d0.jpg)

Als het stil op het bureau ligt met de voorkant omhoog, verschijnt het nummer 4.

![](./media/Makecode_0dd33fa1.jpg)

Als het stil op het bureau ligt met de achterkant omhoog, verschijnt het nummer 5.

Wanneer het bord naar links helt, toont de LED-stippenmatrix het nummer 6 zoals hieronder weergegeven.

![](./media/Makecode_ce2b3501.jpg)

Wanneer het bord naar rechts helt, toont de LED-stippenmatrix het nummer 7 zoals hieronder weergegeven.

![](./media/Makecode_d098ff98.jpg)

Wanneer het bord op de grond wordt geslagen, kan dit proces worden beschouwd als vrije val en toont de LED-stippenmatrix het nummer 8. (let op: deze test wordt niet aanbevolen omdat het de hoofdprintplaat kan beschadigen.)

Let op: als je deze functie wilt proberen, kun je de versnelling ook instellen op 3g, 6g of 8g. Toch raden we dit niet aan.

### (5)Testcode 2:

![](./media/Makecode_99083bf6.gif)

Volledig programma:

![](./media/Makecode_42654b0e.png)

### (6) Testresultaten 2

Upload de testcode naar de Micro: Bit main board V2, voed de hoofdprintplaat via de USB-kabel en klik op "Show console Device".

De volgende interface toont de ontbonden waarden van de versnelling in de X-, Y- en Z-as respectievelijk, evenals de versnelling-synthese (synthese van zwaartekracht en andere externe krachten).

![](./media/Makecode_c17f5477.gif)

Na raadpleging van de MMA8653FC datasheet en het hardware-schemadiagram van de Micro: Bit main board V2, zijn de accelerometercoördinaten van het Micro: Bit V2 moederbord weergegeven in de onderstaande afbeelding:

![](./media/Makecode_79d90885.jpg)

Als je Windows 7 of 8 gebruikt in plaats van Windows 10, kan Google Chrome geen apparaten koppelen. Je moet de CoolTerm seriële monitor-software gebruiken om gegevens te lezen. Je kunt CoolTerm openen, op Options klikken, SerialPort selecteren, de COM-poort instellen en de baudrate op 115200 zetten (na testen is de baudrate van USB SerialPort-communicatie op de Micro: Bit main board V2 115200), klik op OK en Connect. De CoolTerm-seriële monitor toont de gegevens van de X-, Y- en Z-as, zoals in de onderstaande afbeeldingen:

![](./media/Makecode_2a63fc72.gif)