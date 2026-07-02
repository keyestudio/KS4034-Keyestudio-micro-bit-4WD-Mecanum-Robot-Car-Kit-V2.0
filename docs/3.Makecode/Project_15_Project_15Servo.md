## Project 15：Servo

![](./media/Makecode_215da878.png)

1\.  **Beschrijving**

Bij doe-het-zelf slimme auto's is vaak een automatische obstakelvermijding functie aanwezig. Tijdens het bouwproces moeten we een servo gebruiken om de ultrasone module naar links en rechts te laten draaien en vervolgens de afstand tussen de auto en het obstakel te detecteren, zodat de auto het obstakel kan ontwijken. Als andere microcontrollers worden gebruikt om de servo-rotatie te regelen, moeten bepaalde frequenties en pulsbreedtes worden ingesteld om de servohoek te besturen.

Als echter het micro:bit-hoofdboard wordt gebruikt om de servohoek te regelen, hoeft u in de ontwikkelomgeving alleen de stuurhoek in te stellen; de overeenkomstige puls wordt dan automatisch ingesteld om de servodraaing te regelen. In dit project leert u hoe u de servo heen en weer tussen 0° en 90° laat draaien.

2\.  **Informatie over de servo**

Een servomotor is een roterende actuator voor positiebesturing. Het bestaat voornamelijk uit behuizing, printplaat, kernloze motor, tandwiel en positieresensor. Het werkingsprincipe is dat de servo het signaal dat door de MCU of ontvanger wordt verzonden ontvangt, een referentiesignaal met een periode van 20 ms en een breedte van 1,5 ms genereert, en vervolgens de verkregen DC-voorspanning vergelijkt met de spanning van de potentiometer en het spanningsverschil als uitgang verkrijgt.

![](./media/Makecode_87b41036.png)

Bij de in dit project gebruikte servo is de bruine draad massa (GND), de rode draad de plus (V+) en de oranje draad de signaaldraad.

De rotatiehoek van de servomotor wordt geregeld door het regelen van de dutycycle van het PWM- (Pulse-Width Modulation) signaal. De standaardcyclus van het PWM-signaal is 20 ms (50 Hz). Theoretisch ligt de pulsbreedte tussen 1 ms en 2 ms, maar in de praktijk tussen 0,5 ms en 2,5 ms. De breedte komt overeen met de rotatiehoek van 0° tot 180°. Houd er rekening mee dat bij verschillende merken motoren hetzelfde signaal tot verschillende rotatiehoeken kan leiden.

![](./media/Makecode_49467dfa.png)

Meer details:

![](./media/Makecode_b167d550.png)

3\.  **Parameters**

- Werkspanning: DC 4.8V ~ 6V

- Werkhoek bereik: ongeveer 180 ° (bij 500 → 2500 μsec)

- Pulsbreedtebereik: 500 → 2500 μsec

- Onbelast snelheid: 0.12 ± 0.01 s / 60 (DC 4.8V) 0.1 ± 0.01 s / 60 (DC 6V)

- Onbelast stroom: 200 ± 20mA (DC 4.8V) 220 ± 20mA (DC 6V)

- Houdkoppel (stoptorque): 1.3 ± 0.01kg·cm (DC 4.8V) 1.5 ± 0.1kg·cm (DC 6V)

- Stopstroom: ≦ 850mA (DC 4.8V) ≦ 1000mA (DC 6V)

- Standby-stroom: 3 ± 1mA (DC 4.8V) 4 ± 1mA (DC 6V)

4\.  **Voorbereiding**

- Steek de micro:bit kaart in de sleuf van de keyestudio   4WD Mecanum Robot Car V2.0

- Plaats batterijen in de batterijhouder

- Zet de stroomschakelaar op ON

- Verbind de micro:bit met uw computer via een USB-kabel

- Open de webversie van Makecode


5\.  **Testcode**

![](./media/Makecode_087e1822.png)

Klik op "JavaScript" om de bijbehorende JavaScript-code te bekijken:

![](./media/Makecode_2354311f.png)

6.  **Testresultaat**

Na het uploaden van de testcode en het zetten van de POWER-schakelaar op ON, draait de servo van 0 graden naar 180 graden.