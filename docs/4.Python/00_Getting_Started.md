## Resource Download

Om u snel aan de gerelateerde codes, bibliotheken en andere ondersteunende bestanden voor dit product te helpen, klik op de onderstaande links om te downloaden:

- [Python Code and library downloads](./PythonCode.7z)

## Aan de slag met Python

Deze handleiding is geschreven voor de programmeertaal Python. Als u grafische codeprogrammering wilt gebruiken, raadpleeg dan de handleiding "Makecode Tutorial". In de hoofdmap van de gedownloade bron bevindt zich een map met de naam "Python tutorial", waarin alle Python-code van de Micro:bit 4WD Mecanum Robot Car V2.0 is opgeslagen. Het Python-codebestand is een bestand dat eindigt op ".py".

### Wat is MicroPython?

Python is een tekstgebaseerde taal die veel wordt gebruikt in het onderwijs en ook door professionele programmeurs wordt gebruikt in vakgebieden zoals data science en machine learning.

Micro: bit kan in Python worden geprogrammeerd; omdat het een microcontroller is, verhinderen hardwareverschillen dat de micro: bit Python volledig ondersteunt. MicroPython is speciaal voor micro：bit en is een efficiënte implementatie van de programmeertaal Python3. Het bevat een klein deel van de standaardbibliotheek van Python en is geoptimaliseerd om te draaien op micro:bit-microcontrollers.

De versie van Python die door BBC micro: bit wordt gebruikt heet MicroPython. MicroPython is perfect voor degenen die meer over programmeren willen leren; het helpt je te programmeren met een reeks codefragmenten en verschillende kant-en-klare graphics en muziek.

Link voor BBC microbit MicroPyth: [BBC micro:bit MicroPython ](https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html) 

**Python heeft twee soorten editors: webversie en offline versie**

1\.  Webversie: [https://python.microbit.org/v/1.1](https://python.microbit.org/v/1.1)

![](./media/Python_693f76f5.png)

2\.  De andere is ook de offline compiler — Mu ![](./media/Python_153c77ed.png)

Officiële website van Mu: [https://codewith.mu/](https://codewith.mu/)

### Mu

Mu, een Python-code-editor, is geschikt voor beginners. Het ondersteunt geen 32-bit Windows.

1\.  **Mu downloaden**

Klik op “This PC” en klik met de rechtermuisknop op Eigenschappen om de versie van uw computer te controleren.

![](./media/Python_3a58be54.png)

Controleer het systeemtype van uw computer.

![](./media/Python_e774ae15.png)

Ga naar de MU-link: [https://codewith.mu/en/download](https://codewith.mu/en/download) om de bijbehorende versie van Mu te downloaden.

![](./media/Python_ceb4cfa6.png)

2\.  **Installatie uitvoeren**

Open het onderstaande bestand

![](./media/Python_8bcfe24c.png)

Mac OSX: [https://codewith.mu/en/howto/1.1/install_macos](https://codewith.mu/en/howto/1.1/install_macos).

Linux: [https://codewith.mu/en/howto/1.2/install_linux](https://codewith.mu/en/howto/1.2/install_linux).

**Windows 10**

Er verschijnt een pop-up; klik vervolgens op “More info”.

![](./media/Python_877beb7b.png)

Klik vervolgens op “Run anyway”.

![](./media/Python_c87475e5.png)

3\. Licentieovereenkomst

Klik op “Install”.

![](./media/Python_33f42b66.png)

![](./media/Python_f5c6698f.png)

Na installatie, klik op “finish”.

![](./media/Python_c6ec7436.png)

4\. Mu starten

Zoek het vervolgens zoals op de volgende afbeelding

![](./media/Python_c4adbdd1.png)

De hoofdinterface ziet er als volgt uit:

![](./media/Python_3697c0c7.png)

### Gebruik van Modus & Menubalk

Stel “<span style="color: rgb(255, 76, 65);">**Mode**</span>” in op BBC micro:bit.

Klik in het menu op “**Mode**” om het in te stellen op “**BBC micro：bit**”. De micro:bit-modus weet hoe hij moet communiceren met en verbinden met een micro:bit.

![](./media/Python_18512c7e.png)

Klik om te [Start with Mu](https://codewith.mu/en/tutorials/1.1/start).

### Hoe Mu een bibliotheek naar de Micro:bit importeert

<span style="color: rgb(255, 76, 65);">**Voordat bibliotheken worden geïmporteerd, moeten we een .py-code (een lege code is ook ok) uploaden naar de micro:bit-board. Hier nemen we een lege code als voorbeeld.**</span>

Verbind de board via een USB-kabel met de computer. Open Mu en klik op “Flash” om de .py-code (ook leeg) naar het board te uploaden.

![Img](./media/Python_611b2c4e.png)

In dit tutorial wordt het bibliotheekbestand "keyes_mecanum_Car_V2.py" gebruikt. Importeer daarom het bibliotheekbestand "keyes_mecanum_Car_V2.py" naar de micro:bit. Dit bestand bevat de bedieningsmethode van de Micro:bit 4WD Mecanum Robot Car V2.0.

De standaardmap waar Mu bestanden opslaat is “mu_code” in de hoofdmap van de gebruikersdirectory.

Referentielink: [https://codewith.mu/en/tutorials/1.0/files](https://codewith.mu/en/tutorials/1.0/files)

**de methoden om de "mu_code" map te vinden:**

**Methode Een:**

Bijvoorbeeld, op een Windows-systeem, stel dat uw systeem is geïnstalleerd op de C-schijf van de computer en de gebruikersnaam is "**Administrator**", dan is het pad van de "**mu_code**" map "**C:\Users\Administrator\mu_ code**". Op Linux-systemen is het pad van de "**mu_code**" map "**~/home/mu_code**".

Open de “**mu_code**” map.

![](./media/Python_d271a924.png)

**Methode Twee:**

Zoek de “mu_code” map op Schijf (C:).

![Img](./media/Python_03ff037e.png)

![Img](./media/Python_54199d45.png)

Open “mu_code”.

![Img](./media/Python_4841ca3f.png)

Het pad van de datafolder waar het door ons geleverde bibliotheekbestand “keyes_mecanum_Car.py” zich bevindt, is als volgt:

![Img](./media/Python_7adb2b68.png)

Kopieer het bibliotheekbestand “keyes_mecanum_Car.py” naar de map “mu_code”。Wanneer de kopie is voltooid, ziet het er als volgt uit:

![](./media/Python_d753d652.png)

Open eerst de Mu-software en verbind de micro:bit met uw computer, klik vervolgens op de knop "Files" en sleep het bibliotheekbestand "keyes_mecanum_Car.py" naar de micro:bit.

![](./media/Python_aeaae2b7.png)

Na een paar seconden is de import voltooid en kunt u het zien in het vak aan de linkerkant.

![](./media/Python_2be967ca.png)