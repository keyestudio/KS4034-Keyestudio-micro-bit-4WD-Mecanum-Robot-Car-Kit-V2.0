## Project 7: Accelerometer

![](./media/Makecode_66670811.jpg)

[Klicken Sie hier, um den Code 1 für diese Lektion herunterzuladen](./Code/Accelerometer.hex)

[Klicken Sie hier, um den Code 2 für diese Lektion herunterzuladen](./Code/Accelerometer2.hex)

### (1)Projektbeschreibung:

Das Micro: Bit main board V2 verfügt über einen integrierten LSM303AGR-Schwerkraft-Beschleunigungssensor, auch Beschleunigungssensor (Accelerometer) genannt, mit einer Auflösung von 8/10/12 Bit. Im Codeabschnitt kann der Messbereich auf 1g, 2g, 4g und 8g eingestellt werden.

Beschleunigungssensoren werden häufig zur Erfassung des Zustands von Maschinen eingesetzt. In diesem Projekt zeigen wir, wie die Lage der Platine mit dem Beschleunigungssensor gemessen werden kann. Anschließend betrachten wir die von dem Beschleunigungssensor ausgegebenen rohen Dreiachsendaten.

### (2)Benötigte Komponenten:

Micro:bit main board V2

Micro-USB-Kabel

### (3)Testcode 1:

Verbinden Sie den Computer über ein Micro-USB-Kabel mit dem micro:bit-Board und programmieren Sie im MakeCode-Editor,

![](./media/Makecode_2cd48603.gif)

Vollständiges Programm:

![](./media/Makecode_ba28162b.png)

### (4)Testergebnisse 1:

Nachdem Testcode 1 auf das micro:bit V2 hochgeladen wurde, führt eine Änderung der Orientierung der Platine dazu, dass die 5x5-Punktmatrix unterschiedliche Zahlen anzeigt.

![](./media/Makecode_2e6708e6.gif)

Wenn wir das Micro: Bit main board V2 schütteln – unabhängig von der Richtung – zeigt die LED-Punktmatrix die Ziffer "1" an.

Wenn es aufrecht gehalten wird (das Logo über der LED-Punktmatrix), wird die Zahl 2 angezeigt.

![](./media/Makecode_67247ae1.jpg)

Wenn es umgedreht gehalten wird (das Logo unter der LED-Punktmatrix), erscheint wie unten gezeigt.

![](./media/Makecode_1668a9d0.jpg)

Wenn es ruhig auf dem Schreibtisch liegt und die Vorderseite zeigt, erscheint die Zahl 4.

![](./media/Makecode_0dd33fa1.jpg)

Wenn es ruhig auf dem Schreibtisch liegt und die Rückseite zeigt, erscheint die Zahl 5.

Wenn die Platine nach links geneigt wird, zeigt die LED-Punktmatrix die Zahl 6, wie unten gezeigt.

![](./media/Makecode_ce2b3501.jpg)

Wenn die Platine nach rechts geneigt wird, zeigt die LED-Punktmatrix die Zahl 7, wie unten gezeigt.

![](./media/Makecode_d098ff98.jpg)

Wenn die Platine auf den Boden geschlagen wird, kann dieser Vorgang als freier Fall betrachtet werden und die LED-Punktmatrix zeigt die Zahl 8. (Bitte beachten Sie, dass dieser Test nicht empfohlen wird, da er die Hauptplatine beschädigen kann.)

Achtung: Wenn Sie diese Funktion ausprobieren möchten, können Sie die Beschleunigung auch auf 3g, 6g oder 8g einstellen. Dennoch empfehlen wir dies nicht.

### (5)Testcode 2:

![](./media/Makecode_99083bf6.gif)

Vollständiges Programm:

![](./media/Makecode_42654b0e.png)

### (6) Testergebnisse 2

Laden Sie den Testcode auf das micro:bit main board V2 hoch, versorgen Sie die Hauptplatine über das USB-Kabel mit Strom und klicken Sie auf "Show console Device".

Die folgende Oberfläche zeigt die Zerlegungswerte der Beschleunigung in X-, Y- und Z-Achse sowie die Beschleunigungssynthese (Zusammensetzung aus Schwerkraft und anderen externen Kräften).

![](./media/Makecode_c17f5477.gif)

Nach Rückgriff auf das Datenblatt des MMA8653FC und das Hardware-Schema des Micro: Bit main board V2 sind die Beschleunigungskoordinaten der Micro: Bit V2 Hauptplatine in der folgenden Abbildung dargestellt:

![](./media/Makecode_79d90885.jpg)

Wenn Sie Windows 7 oder 8 anstelle von Windows 10 verwenden, kann Google Chrome die Geräte nicht erkennen. Sie müssen die CoolTerm-Seriellenmonitor-Software verwenden, um die Daten auszulesen. Öffnen Sie die CoolTerm-Software, klicken Sie auf Options, wählen Sie SerialPort, stellen Sie den COM-Port ein und setzen Sie die Baudrate auf 115200 (nach Tests beträgt die Baudrate der USB-SerialPort-Kommunikation auf dem Micro: Bit main board V2 115200), klicken Sie auf OK und Connect. Der CoolTerm-Serielle Monitor zeigt die Daten der X-, Y- und Z-Achse an, wie in den folgenden Abbildungen dargestellt:

![](./media/Makecode_2a63fc72.gif)