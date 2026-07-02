## BBC Micro:bit

### **(1) ¿Qué es Micro:bit?**

Micro:bit es una plataforma de hardware de código abierto basada en la arquitectura ARM, lanzada por la British Broadcasting Corporation (BBC) junto con ARM, Barclays, element14, Microsoft y otras instituciones. El dispositivo central es un microprocesador Arm Cortex‑M4 de 32 bits con FPU.

Tiene el tamaño de una tarjeta de crédito pero es muy potente. La placa principal Micro:bit está equipada con numerosos componentes como una matriz LED 5×5, 2 botones programables, un acelerómetro, una brújula, un termómetro, un logo táctil, un micrófono MEMS, un módulo Bluetooth de baja energía y un zumbador, lo que le permite reproducir diversos sonidos sin dispositivos externos.

Además, esta placa admite un modo de suspensión para reducir el consumo de la batería; se puede activar manteniendo pulsado el botón Reset & Power en la parte trasera.

La placa de desarrollo Micro:bit es fácil de usar y ampliar: el diseño de los contactos dorados (gold fingers) en la parte inferior permite interactuar con diversos componentes electrónicos mediante pinzas de cocodrilo. Puede leer datos de sensores, controlar servos y luces RGB e incorporar una placa de expansión para conectar varios sensores.

Asimismo, admite diversos códigos y plataformas de programación gráfica, es compatible con casi todos los PC y dispositivos móviles y no requiere instalación complicada de drivers. Dispone de módulos electrónicos altamente integrados y de una función de monitorización del puerto serie para facilitar la depuración.

La placa se utiliza ampliamente en la programación de videojuegos, interacciones de luz y sonido, control de robots, experimentos científicos, dispositivos wearables y en inventos creativos como robots e instrumentos musicales.

### **(2) Disposición**

![Img](./media/Introduction_5746e59b.png)

Para más información, consulte los siguientes enlaces:

[https://tech.microbit.org/hardware/](https://tech.microbit.org/hardware/)

[https://microbit.org/new-microbit/](https://microbit.org/new-microbit/)

[https://www.microbit.org/get-started/user-guide/overview/](https://www.microbit.org/get-started/user-guide/overview/)

[https://microbit.org/get-started/user-guide/features-in-depth/](https://microbit.org/get-started/user-guide/features-in-depth/)

### **(3) Pin out**

![](./media/Introduction_ce0de295.png)

**Funciones:**

|                            |                                                                                                    |
|----------------------------|----------------------------------------------------------------------------------------------------|
| GPIO                       | P0, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, P15, P16, P19, P20                |
| ADC/DAC                    | P0, P1, P2, P3, P4, P10                                                                            |
| IIC                        | P19 (SCL), P20 (SDA)                                                                               |
| SPI                        | P13 (SCK), P14 (MISO), P15 (MOSI)                                                                 |
| PWM (usado con frecuencia) | P0, P1, P2, P3, P4, P10                                                                            |
| PWM (poco usado)           | P5, P6, P7, P8, P9, P11, P12, P13, P14, P15, P16, P19, P20                                         |
| Ocupado                    | P3 (LED Col3), P4 (LED Col1), P5 (Button A), P6 (LED Col4), P7 (LED Col2), P10 (LED Col5), P11 (Button B) |

Consulte el sitio web oficial para más detalles: [https://tech.microbit.org/hardware/edgeconnector/](https://tech.microbit.org/hardware/edgeconnector/)

[https://microbit.org/guide/hardware/pins/](https://microbit.org/guide/hardware/pins/)

### **(4) Precauciones para el uso de la placa Micro:bit:**

a\. Se recomienda cubrirla con un protector de silicona para evitar cortocircuitos en sus delicados componentes electrónicos.

b\. Su puerto IO tiene una capacidad de manejo de corriente limitada y solo puede gestionar corrientes inferiores a 300 mA. Por lo tanto, no conecte dispositivos de alta corriente, como servos MG995 o motores de corriente continua (DC), ya que podrían quemarse. Además, debe comprobar los requisitos de corriente de los dispositivos antes de usarlos; generalmente se recomienda utilizar la placa junto con una placa de expansión Micro:bit.

c\. Se recomienda alimentar la placa principal mediante la interfaz USB o con una batería de 3V. El puerto IO de esta placa es de 3V, por lo que no admite sensores de 5V. Si necesita conectar sensores de 5V, se requiere una placa de expansión Micro:bit.

d\. Al usar pines compartidos con la matriz LED (P3, P4, P6, P7 y P10), si se bloquean respecto a la matriz o a los LED, estos pueden mostrarse de forma aleatoria y los datos de los sensores conectados pueden ser incorrectos.

e\. Los pines 19 y 20 no pueden usarse como puertos IO aunque MakeCode muestre que sí. Solo pueden utilizarse para comunicación I2C.

f\. El puerto de batería de 3V no debe conectarse a una batería de más de 3,3V o la placa principal se dañará.

g\. Prohibido operar sobre superficies metálicas para evitar cortocircuitos.

En resumen, la placa principal Micro:bit V2 es como un microordenador que pone la programación al alcance de la mano y potencia la innovación digital. En cuanto al entorno de programación, la BBC ofrece el sitio: [https://microbit.org/code/](https://microbit.org/code/), que dispone de un entorno gráfico MakeCode fácil de usar.

---