## Projekt 12: Bluetooth-Drahtloskommunikation

![](./media/Makecode_041ff91a.jpg)

### (1)Projektbeschreibung:

Hinweis: Diese Lektion erklärt, wie Code über Bluetooth mithilfe einer App hochgeladen wird. Daher wird kein Code bereitgestellt. Bitte folgen Sie den Schritten in der animierten GIF-Datei.

Das Micro: Bit main board V2 verfügt über einen nRF52833-Prozessor (mit einem integrierten BLE (Bluetooth Low Energy)-Modul, Bluetooth 5.1) und eine 2,4‑GHz-Antenne für Bluetooth- und 2,4‑GHz-Drahtloskommunikation. Dadurch kann die Platine mit einer Vielzahl von Bluetooth-Geräten kommunizieren, einschließlich Smartphones und Tablets.

In diesem Projekt konzentrieren wir uns hauptsächlich auf die Bluetooth-Drahtloskommunikationsfunktion dieses Mainboards. Über Bluetooth kann es Code oder Signale übertragen. Dazu sollten wir ein Apple-Gerät (ein iPhone oder ein iPad) mit der Platine verbinden.

Da die Einrichtung von Android-Telefonen zur drahtlosen Übertragung der von Apple-Geräten ähnelt, ist keine zusätzliche Darstellung erforderlich.

### (2) Vorbereitung

Verbinden Sie das Micro:bit main board V2 über das Micro-USB-Kabel mit Ihrem Computer.

Ein Apple-Gerät (ein Telefon oder ein iPad) oder ein Android-Gerät;

### (3) Installieren von Micro:bit:

Für Android

![](./media/Makecode_0cf9abf0.gif)

Für ios

![](./media/Makecode_5937459b.gif)

(4)Testcode:

Als Nächstes verwenden wir unsere Telefone, um Code zu schreiben und eine Verbindung über Bluetooth herzustellen (Hinweis: Der Vorgang ist für Android- und iOS-Geräte identisch; in dieser Demonstration wird ein Android-Telefon verwendet).

1、Öffnen Sie die Software und verbinden Sie sich mit Bluetooth.

![](./media/Makecode_dcb2416a.gif)

2、Drücken Sie nacheinander die Taste A, die Taste B und die Reset-Taste auf der Rückseite des Microbit. Die Hauptplatine zeigt dann ein Symbol an.

![](./media/Makecode_6985c2b1.gif)

3、Geben Sie das in Schritt zwei angezeigte Muster in die Telefonoberfläche ein.

![](./media/Makecode_9095fb35.gif)

Code schreiben und hochladen

1、Öffnen Sie die Programmieroberfläche und schreiben Sie einen Code.

![](./media/Makecode_b7c8c1ca.gif)

2、Drücken Sie nacheinander die Taste A, die Taste B und die Reset-Taste. (Hinweis: Dieser Vorgang muss jedes Mal wiederholt werden, wenn Code über die App hochgeladen wird.)

 ![](./media/Makecode_86ab2b39.gif)

3、Nachdem Sie bestätigt haben, dass das Microbit-Symbol mit dem auf Ihrem Telefon dargestellten übereinstimmt, klicken Sie einfach auf „Next“.

![](./media/Makecode_f3c17f45.gif)

Schließlich können Sie sehen, dass die Microbit-Platine das im Code definierte Muster anzeigt.

Hiermit haben wir den Vorgang zum Hochladen von Code auf das Telefon abgeschlossen. Wichtige Hinweise:

1. Um das Telefon mit der Microbit-Platine zu verbinden, drücken Sie nacheinander die Tasten A, B und Reset. Die Punktmatrixanzeige zeigt dann ein Muster an, das in das Telefon eingegeben werden muss.
2. Die Microbit-Platine kann über ein USB-Kabel mit Strom versorgt werden oder indem 3V über ein Batteriepack an den Stromanschluss der Platine gelegt werden. Hinweis: Die Spannung darf 3V nicht überschreiten, da eine Überschreitung die Platine beschädigen kann.