## Project 5: Temperatuurdetectie

![](./media/Makecode_22c6434f.jpg)

[Klik hier om code 1 voor deze les te downloaden](./Code/Temperature-Detection.hex)

[Klik hier om code 2 voor deze les te downloaden](./Code/Temperature-Detection2.hex)

### (1)Projectbeschrijving:

De Micro:bit main board V2 is niet uitgerust met een aparte temperatuursensor, maar gebruikt de in de NFR52833-chip ingebouwde temperatuursensor voor temperatuurdetectie. Daarom komt de gemeten temperatuur meer overeen met de temperatuur van de chip en kan deze afwijken van de omgevingstemperatuur.

### (2)Benodigde componenten:

Micro:bit main board V2

Micro USB-kabel

### (3)Testcode 1 :

![](./media/Makecode_e6674fe9.gif)

### (4)Testresultaten 1:

Nadat u testcode 1 naar de Micro:bit main board V2 heeft geüpload, het bord via de USB-kabel van stroom heeft voorzien en op "Show console Device" heeft geklikt, verschijnen de temperatuurgegevens op de seriële monitorpagina zoals hieronder weergegeven.

![](./media/Makecode_898eded8.gif)

Als u Windows 7 of 8 gebruikt in plaats van Windows 10, kan Google Chrome de apparaten niet koppelen. U moet de CoolTerm-seriële monitorsoftware gebruiken om de gegevens te lezen. Open CoolTerm, klik op Options, selecteer SerialPort, stel de COM-poort in en zet de baudrate op 115200 (na tests is de baudrate van USB SerialPort-communicatie op de Micro:bit main board V2 115200), klik OK en Connect. De CoolTerm-seriële monitor toont de verandering van de temperatuur in de huidige omgeving, zoals in de onderstaande afbeeldingen:

![](./media/Makecode_268159a1.gif)

### (5)Testcode 2 :

Verbind de computer met het micro:bit-bord via een micro-USB-kabel en programmeer in de MakeCode-editor,

![](./media/Makecode_4057bdd7.gif)

Volledig programma :

![](./media/Makecode_ec457959.png)

### (6)Testresultaten 2:

Na het uploaden van code 2 toont de 5x5 LED-puntsmatrix ![](./media/Makecode_350d26c6.png) wanneer de omgevingstemperatuur minder dan 35℃ is. Wanneer de temperatuur gelijk aan of hoger dan 35℃ is, verschijnt het patroon ![](./media/Makecode_ef8d7c88.png).