## Project 6: Geomagnetische sensor

[Klik hier om code 1 voor deze les te downloaden](./Code/Geomagnetic-Sensor.hex)

[Klik hier om code 2 voor deze les te downloaden](./Code/Geomagnetic-Sensor2.hex)

### (1)Projectbeschrijving:

(1) Projectbeschrijving: Dit project heeft tot doel het gebruik van de Micro:bit geomagnetische sensor uit te leggen, die niet alleen de sterkte van het geomagnetische veld kan detecteren, maar ook als kompas kan worden gebruikt om richtingen te bepalen. Het is ook een belangrijk onderdeel van het Attitude and Heading Reference System (AHRS). De Micro:bit main board V2 gebruikt de LSM303AGR geomagnetische sensor, en het dynamische bereik van het magnetische veld is ± 50 gauss. Op de plaat wordt de magnetometermodule zowel voor magnetische detectie als als kompas gebruikt. In dit experiment wordt eerst het kompas geïntroduceerd en vervolgens worden de ruwe gegevens van de magnetometer gecontroleerd. Het belangrijkste onderdeel van een gewoon kompas is een magnetische naald, die door het geomagnetische veld kan worden gedraaid en naar de geomagnetische Noordpool wijst (die zich dicht bij de geografische Zuidpool bevindt) om de richting te bepalen.

### (2)Benodigde onderdelen:

Micro:bit main board V2

 Micro-USB-kabel

### (3)Testcode 1 :

Verbind de computer met de micro:bit-ploeg via een Micro-USB-kabel en programmeer in de MakeCode-editor.

![](./media/Makecode_5805c7de.gif)

Volledig programma :

![](./media/Makecode_5a958132.png)

### (4)Testresultaten 1 :

Nadat u de testcode naar het Micro:bit main board V2 hebt geüpload en de board van stroom hebt voorzien via de USB-kabel, en op knop A hebt gedrukt, vraagt de board ons om het kompas te kalibreren en toont de LED-puntmatrix "TILT TO FILL SCREEN". Ga dan naar de kalibratiepagina. Draai de board totdat alle 25 LED's rood oplichten zoals hieronder weergegeven.

![](./media/Makecode_b0a4ebf1.jpg)

kalibreer kompas:

![](./media/Makecode_05a88e21.gif)

Daarna verschijnt een glimlachpatroon ![](./media/Makecode_74a69436.png), wat aangeeft dat de kalibratie is voltooid. Wanneer het kalibratieproces is voltooid, zorgt het indrukken van knop A ervoor dat de magnetometerlezing direct op het scherm wordt weergegeven. En de richtingen noord, oost, zuid en west komen respectievelijk overeen met 0°, 90°, 180° en 270°.

![](./media/Makecode_23b07bfb.gif)

### (5) Testcode 2:

Deze module kan gegevens blijven lezen om de richting te bepalen, en wijst dus met een pijl naar de huidige magnetische noordpool.

Verbind de computer met de micro:bit-ploeg via een Micro-USB-kabel en programmeer in de MakeCode-editor,

![](./media/Makecode_db8b2d7e.gif)

Volledig programma :

![](./media/Makecode_ef823069.png)

### (6) Testresultaten 2

Upload code 2. Na de kalibratie kantelt u de micro:bit-ploeg en toont de LED-puntmatrix de richtingstekens.

![](./media/Makecode_d8944d5f.gif)

---