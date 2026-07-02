## BBC Micro:bit

### **(1) Qu'est-ce que le Micro:bit ?**

Micro:bit est une plateforme matérielle open source basée sur l'architecture ARM, lancée par la British Broadcasting Corporation (BBC) en collaboration avec ARM, Barclays, element14, Microsoft et d'autres institutions. Le cœur est un microprocesseur 32 bits Arm Cortex‑M4 avec FPU.

Il a la taille d'une carte de crédit mais il est très puissant. La carte principale Micro:bit est équipée de nombreux composants tels qu'une matrice de LED 5×5, 2 boutons programmables, un accéléromètre, une boussole, un thermomètre, un logo tactile, un microphone MEMS, un module Bluetooth basse consommation ainsi qu'un buzzer, ce qui lui permet de produire une variété de sons sans périphériques externes.

De plus, cette carte prend en charge un mode veille pour réduire la consommation de la batterie ; ce mode peut être activé en maintenant enfoncé le bouton Reset & Power à l'arrière.

La carte de développement Micro:bit est facile à utiliser et à étendre : les contacts dorés (gold fingers) situés sur le bord inférieur (edge connector) peuvent interagir avec divers composants électroniques via des pinces crocodiles. Elle peut lire les données des capteurs, contrôler des servomoteurs et des LED RGB, et accueillir une carte d'extension pour connecter différents capteurs.

En outre, elle prend en charge divers langages et environnements de programmation graphiques, est compatible avec quasiment tous les PC et appareils mobiles et ne nécessite pas de pilote complexe. Elle intègre des modules électroniques et une fonction de surveillance du port série pour faciliter le débogage.

La carte est largement utilisée pour la programmation de jeux vidéo, les interactions lumière‑son, le contrôle de robots, les expériences scientifiques, les dispositifs portables ainsi que pour des créations originales comme des robots et des instruments de musique.

### **(2) Disposition**

![Img](./media/Introduction_5746e59b.png)

Pour plus d'informations, veuillez consulter les liens suivants :

[https://tech.microbit.org/hardware/](https://tech.microbit.org/hardware/)

[https://microbit.org/new-microbit/](https://microbit.org/new-microbit/)

[https://www.microbit.org/get-started/user-guide/overview/](https://www.microbit.org/get-started/user-guide/overview/)

[https://microbit.org/get-started/user-guide/features-in-depth/](https://microbit.org/get-started/user-guide/features-in-depth/)

### **(3) Brochage (Pin out)**

![](./media/Introduction_ce0de295.png)

**Fonctions :**

|                            |                                                                                                    |
|----------------------------|----------------------------------------------------------------------------------------------------|
| GPIO                       | P0, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, P15, P16, P19, P20                |
| ADC/DAC                    | P0, P1, P2, P3, P4, P10                                                                            |
| IIC                        | P19 (SCL), P20 (SDA)                                                                              |
| SPI                        | P13 (SCK), P14 (MISO), P15 (MOSI)                                                                 |
| PWM (fréquemment utilisé)  | P0, P1, P2, P3, P4, P10                                                                            |
| PWM (peu utilisé)          | P5, P6, P7, P8, P9, P11, P12, P13, P14, P15, P16, P19, P20                                         |
| Occupé                     | P3 (LED Col3), P4 (LED Col1), P5 (Button A), P6 (LED Col4), P7 (LED Col2), P10 (LED Col5), P11 (Button B) |

Veuillez consulter le site officiel pour plus de détails : [https://tech.microbit.org/hardware/edgeconnector/](https://tech.microbit.org/hardware/edgeconnector/)

[https://microbit.org/guide/hardware/pins/](https://microbit.org/guide/hardware/pins/)

### **(4) Précautions d'utilisation de la carte mère Micro:bit :**

a\. Il est recommandé de recouvrir la carte d'une protection en silicone pour éviter les courts‑circuits sur ses composants électroniques sensibles.

b\. Les ports IO ont une capacité de pilotage faible et ne peuvent supporter que des courants inférieurs à 300 mA. Par conséquent, ne les connectez pas à des dispositifs consommant un courant important, tels que des servomoteurs MG995 ou des moteurs DC, sous peine de les endommager. Assurez‑vous de connaître les besoins en courant des dispositifs avant de les utiliser ; il est généralement recommandé d'utiliser la carte avec une carte d'extension Micro:bit.

c\. Il est conseillé d'alimenter la carte principale via l'interface USB ou une batterie 3V. Les ports IO sont en 3V et ne prennent pas en charge les capteurs 5V. Si vous devez connecter des capteurs 5V, une carte d'extension Micro:bit est nécessaire.

d\. Lors de l'utilisation des broches partagées avec la matrice LED (P3, P4, P6, P7 et P10), si ces broches sont occultées par la matrice ou les LED, celles‑ci peuvent s'afficher de façon aléatoire et les données des capteurs connectés peuvent être erronées.

e\. Les broches 19 et 20 ne peuvent pas être utilisées comme ports IO bien que MakeCode puisse l'indiquer. Elles ne servent qu'à la communication I2C.

f\. Le port batterie 3V ne doit pas être connecté à une batterie de plus de 3,3V, au risque d'endommager la carte principale.

g\. Il est interdit de faire fonctionner la carte sur des surfaces métalliques afin d'éviter les courts‑circuits.

En résumé, la carte principale Micro:bit V2 est comme un micro‑ordinateur : elle rend la programmation accessible et favorise l'innovation numérique. Pour l'environnement de programmation, la BBC propose le site : [https://microbit.org/code/](https://microbit.org/code/), qui propose un environnement graphique MakeCode facile à utiliser.

---