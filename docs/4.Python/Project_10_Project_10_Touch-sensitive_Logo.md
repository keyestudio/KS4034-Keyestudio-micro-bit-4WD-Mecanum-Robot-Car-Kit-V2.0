### Project 10: Aanraakgevoelig logo

![](./media/Python_64469585.png)

1\.  **Beschrijving**

De micro:bit hoofdplaat V2 is uitgerust met een gouden aanraakgevoelig logo, dat kan fungeren als een invoercomponent zoals een knop.

Het bevat een capacitieve aanraking-sensor die kleine veranderingen in het elektrische veld waarneemt wanneer het wordt ingedrukt (of aangeraakt), net als het scherm van uw telefoon of tablet. Wanneer u erop drukt, kan het programma worden geactiveerd.

2\.  **Voorbereiding**

A. Sluit de micro:bit hoofdplaat aan op uw computer via de USB-kabel.

B. Open de offline versie van Mu.

3\.  **Testcode**

Start de Mu-software en open het bestand “Touch-sensitive Logo\.py” om de code te importeren. U kunt de code ook zelf in het bewerkvenster invoeren.

(**Opmerking: Alle Engelse woorden en symbolen moeten in het Engels worden geschreven**.)

![](./media/Python_0c54cbe5.png)

```python
from microbit import *
time = 0
start = 0
running = False

while True:

    if button_a.was_pressed():
        running = True
        start = running_time()
    if button_b.was_pressed():
        if running:
            time += running_time() - start
        running = False
    if pin_logo.is_touched():
        if not running:
            display.scroll(int(time/1000))

    if running:
        display.show(Image.HEART)
        sleep(300)
        display.show(Image.HEART_SMALL)
        sleep(300)
    else:
        display.show(Image.ASLEEP)
```

**Hoe werkt de Micro:bit?**

A\. De looptijd wordt geregistreerd in milliseconden (ms).

B\. Wanneer u knop A indrukt, wordt een variabele met de naam start ingesteld op de huidige looptijd.

C\. Wanneer u knop B indrukt, wordt de starttijd afgetrokken van de nieuwe looptijd om de verstreken tijd te berekenen sinds u de stopwatch bent gestart. Dit verschil wordt opgeteld bij de totale tijd, die wordt opgeslagen in een variabele met de naam time.

D\. Als u op het gouden logo drukt, zal het programma de in totaal verstreken tijd op het LED-display weergeven. Het zet tijd om van milliseconden (duizendsten van een seconde) naar seconden door te delen door 1000. Het gebruikt de gehele deling-operator om een geheel getal te geven.

E\. Het programma wordt ook geregeld door een Booleaanse variabele met de naam running. Een Booleaanse variabele heeft slechts twee waarden: true of false. Als "running" "true" is, betekent dit dat de stopwatch is gestart. Als "running" false is, betekent dit dat de stopwatch niet is gestart of is gestopt.

F\. Als "running" true is, wordt het kloppende hartpatroon weergegeven op het LED-dotmatrixscherm.

G\. (7) Als de stopwatch is gestopt en "running" false is, zal het drukken op het gouden logo alleen de tijd weergeven.

H\. Als de stopwatch is gestart en "running" true is, hoeft alleen te worden gegarandeerd dat de variabele time zal veranderen wanneer knop B wordt ingedrukt, en de code kan ook valse metingen voorkomen.

Klik op “Check” om fouten in de code te controleren. Het programma is foutief als er onderstrepingen en cursors worden weergegeven.

![](./media/Python_1766a28c.png)

Als de code correct is, sluit de micro:bit aan op uw computer en klik op “Flash” om de code naar het micro:bit-board te downloaden.

![](./media/Python_a3d6e994.png)

4\.  **Testresultaat**

Nadat de code succesvol naar het board is gedownload, **zet de stroom aan via de micro USB-kabel of een externe voeding (zet de DIP-schakelaar op ON)** en druk op de resetknop van de micro:bit.

![Img](./media/Python_bb3e1312.png)

Druk op knop A om de stopwatch te starten. Tijdens het timen wordt het kloppende hartpatroon weergegeven op de LED-dotmatrix. Druk op knop B om te stoppen; u kunt het op elk moment starten en stoppen.

Het blijft tijd registreren, net als een echte stopwatch. Druk op het gouden logo aan de voorkant van de micro:bit om de gemeten tijd in seconden weer te geven. En de tijd kan worden teruggezet naar nul door op de resetknop aan de achterkant te drukken.