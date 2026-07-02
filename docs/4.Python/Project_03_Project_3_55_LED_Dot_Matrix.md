### Project 3：5×5 LED Puntmatrix

![](./media/Python_b855274f.png)

1\.  **Beschrijving**

Puntmatrices komen veel voor in het dagelijks leven en worden veel toegepast in LED-reclameschermen, liftvloerweergaven, bushalte-aankondigingen enzovoort.
De LED-puntmatrix van de Micro: Bit-hoofdplaat bevat 25 diodes. Eerder zijn we erin geslaagd om een bepaalde LED te bedienen via zijn positiepunt. Ondersteund door dezelfde theorie kunnen we meerdere LED's tegelijkertijd inschakelen om patronen, cijfers en tekens weer te geven.

Bovendien kunnen we op “show icon” klikken om het patroon te kiezen dat we willen weergeven. Tot slot kunnen we ook zelf patronen ontwerpen.

2\.  **Voorbereiding**

A. Bevestig het micro:bit-hoofdboard aan uw computer via de USB-kabel

B. Open de offline versie van Mu.

3\.  **Testcode1**

U kunt het bestand “5×5 LED Dot Matrix-1\.py” openen om de code te importeren. U kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: Alle woorden en symbolen moeten in het Engels worden geschreven.**)

![](./media/Python_00f15f0a.png)

```python
from microbit import *

val = Image("00900:""00900:""90909:""09990:""00900")

display.show(val)
```

Klik op “Check” om fouten in de code te controleren. Het programma is fout als er onderstrepingen en cursors worden weergegeven. 

![](./media/Python_a1197f5e.png)

Als de code correct is, sluit u de micro:bit aan op de computer en klikt u op “Flash” om de code naar het micro:bit-board te downloaden.

![](./media/Python_1fd78e31.png)

4\.  **Testresultaat1**

Nadat de code met succes naar het bord is gedownload, **zet u de voeding aan via de micro USB-kabel of een externe voeding (zet de DIP-schakelaar op ON)** en druk op de resetknop op de plaat.

![Img](./media/Python_bb3e1312.png)

U zult zien dat de 5×5 puntmatrix een pijl naar beneden begint weer te geven ![](./media/Python_26c7d8c0.png).

5\.  **Testcode2**

U kunt het bestand “5×5 LED Dot Matrix-2\.py” openen om de code te importeren. U kunt de code ook zelf in het bewerkingsvenster invoeren.

(**Opmerking: Alle woorden en symbolen moeten in het Engels worden geschreven.**)

![](./media/Python_dc6eea45.png)

```python
from microbit import *
val = Image("00900:""00900:""90909:""09990:""00900")
display.show('1')
sleep(500)
display.show('2')
sleep(500)
display.show('3')
sleep(500)
display.show('4')
sleep(500)
display.show('5')
sleep(500)
display.show(val)
sleep(500)
display.scroll("hello!")
sleep(200)
display.show(Image.HEART)
sleep(500)
display.show(Image.ARROW_NE)
sleep(500)
display.show(Image.ARROW_SE)
sleep(500)
display.show(Image.ARROW_SW)
sleep(500)
display.show(Image.ARROW_NW)
sleep(500)
display.clear()
```

Klik op “Check” om fouten in de code te onderzoeken. Het programma is fout als er onderstrepingen en cursors worden weergegeven. 

![](./media/Python_14bb490a.png)

Als de code correct is, sluit u de micro:bit aan op de computer en klikt u op “Flash” om de code naar het micro:bit-board te downloaden.

![](./media/Python_a05c33d2.png)

6\.  **Testresultaat2**

Nadat de code met succes naar het bord is gedownload, **zet u de voeding aan via de micro USB-kabel of een externe voeding (zet de DIP-schakelaar op ON)** en druk op de resetknop op de plaat.

![Img](./media/Python_bb3e1312.png)

U zult zien dat de 5×5 puntmatrix de nummers 1, 2, 3, 4 en 5 begint weer te geven en vervolgens afwisselend een pijl naar beneden ![](./media/Python_26c7d8c0.png), “Hello”, een hartpatroon ![](./media/Python_9b18b2b8.png), een pijl die naar het noordoosten wijst ![](./media/Python_364f2e35.png), daarna naar het zuidoosten
![](./media/Python_fb3ba009.png), daarna naar het zuidwesten ![](./media/Python_7ec21961.png) en tenslotte naar het noordwesten ![](./media/Python_ced0bb41.png) weergeeft.

7\.  **Code-uitleg**

![Img](./media/Python_ef42956d.png)


6.  **Referentie**

display.scroll() ：

Het display scrolt om de waarden weer te geven; als het een integer of float is, gebruiken we str() om het om te zetten naar tekenreeksen.

Meer details vindt u via de link: [https://microbit-micropython.readthedocs.io/en/latest/utime.html](https://microbit-micropython.readthedocs.io/en/latest/utime.html)