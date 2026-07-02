## Proyecto 19：Control remoto IR

### Proyecto 19.1：Decodificar el control remoto IR

![](./media/Makecode_3a3e9860.png)

1\. **Descripción**

No cabe duda de que el control remoto infrarrojo es omnipresente en la vida diaria. Se utiliza para controlar varios electrodomésticos, como televisores, equipos de sonido, videograbadores y receptores de señal por satélite. El control remoto infrarrojo está compuesto por sistemas de transmisión y recepción infrarroja, es decir, un control remoto infrarrojo, un módulo receptor infrarrojo y un microcontrolador capaz de decodificar.

![](./media/Makecode_9980b41f.png)

La señal portadora infrarroja de 38K emitida por el mando se codifica mediante el chip de codificación del mando. Está compuesta por una sección de código de piloto, código de usuario, código inverso de usuario, código de datos y código inverso de datos. El intervalo de tiempo del pulso se utiliza para distinguir si es una señal 0 o 1 y la codificación se compone de estas señales 0 y 1.

El código de usuario del mismo mando permanece sin cambios. El código de datos distingue la tecla.

Cuando se pulsa un botón del mando, éste envía una señal portadora infrarroja. Cuando el receptor IR recibe la señal, el programa decodifica la portadora y determina qué tecla se ha pulsado. El MCU decodifica la señal 01 recibida, determinando así qué tecla del mando fue pulsada.

El receptor infrarrojo que utilizamos es un módulo receptor infrarrojo. Compuesto principalmente por una cabeza receptora infrarroja, es un dispositivo que integra recepción, amplificación y demodulación. Su IC interno ha completado la demodulación y puede llevar a cabo desde la recepción infrarroja hasta la salida, siendo compatible con señales TTL. Además, es adecuado para el control remoto por infrarrojos y la transmisión de datos por infrarrojos. El módulo receptor infrarrojo fabricado por el receptor tiene solo tres pines: línea de señal, VCC y GND.

Según la imagen anterior, el puerto integrado del receptor infrarrojo está conectado al puerto P9 5V G en la placa controladora del motor y es controlado por el P9 del micro:bit.

2\. **Parámetros:**

- Tensión de funcionamiento: 3.3-5V（DC）

- Interfaz: 3PIN

- Señal de salida: señal digital

- Ángulo de recepción: 90 grados

- Frecuencia: 38khz

- Distancia de recepción: aproximadamente 5m

3\. **Preparación**

- Inserte la placa micro:bit en la ranura del keyestudio   4WD Mecanum Robot Car V2.0

- Coloque las baterías en el portabaterías

- Gire el interruptor de alimentación a la posición ON

- Conecte el micro:bit a su ordenador mediante un cable USB

- Abra la versión web de Makecode


4\. **Código de prueba**

![](./media/Makecode_2e20f731.png)

Haga clic en “JavaScript" para cambiar al código JavaScript correspondiente:

![](./media/Makecode_87e18859.png)

**Explicación del código:** Si los botones no están pulsados, el monitor serie muestra constantemente 0; al pulsarlos, se muestran los valores de las teclas correspondientes.

**Notas：**

El mando de este kit no incluye las pilas. Recomendamos adquirirlas en línea. (tipo de pila: CR2025).

Asegúrese de que el mando IR funciona antes de la prueba. Aquí tiene un consejo para comprobarlo:

Abra la cámara del móvil, apunte el mando IR hacia la cámara y pulse un botón. Si ve una luz púrpura intermitente en la cámara, el mando está bien.

5\. **Resultado de la prueba**

Descargue el código en la placa micro:bit y no desconecte el cable USB. Haga clic![](./media/Makecode_e0580d78.png)

![](./media/Makecode_0d3198e0.png)

Apunte el mando IR al receptor IR y pulse el botón; el monitor serie mostrará los valores de las teclas correspondientes, como se muestra a continuación:

![](./media/Makecode_c7a33a4c.png)

Abra CoolTerm, haga clic en Options para seleccionar SerialPort. Configure el puerto COM y la velocidad en baudios a 115200. Haga clic en “OK” y “Connect”.

El monitor serie de CoolTerm muestra el valor de la tecla como sigue:

![Img](./media/Makecode_155c857a.png)

El valor de la tecla se muestra como referencia:

![](./media/Makecode_1fc0d9bb.jpg)

### Proyecto 19.2：Control remoto IR

![Img](./media/Makecode_643cb701.png)

1\. **Descripción**

En este proyecto combinamos el control remoto IR con el car shield para crear un coche inteligente controlado por IR. Su principio es controlar el movimiento del coche enviando señales de tecla desde el mando IR al módulo receptor IR del car shield.

2\. **Preparación**

- Inserte la placa micro:bit en la ranura del keyestudio   4WD Mecanum Robot Car V2.0

- Coloque las baterías en el portabaterías

- Gire el interruptor de alimentación a la posición ON

- Conecte el micro:bit a su ordenador mediante un cable USB

- Abra la versión web de Makecode

**Nota:** El sensor infrarrojo y el mando IR no deben utilizarse en entornos con interferencias infrarrojas como la luz solar, ya que esta contiene muchas luces invisibles, como infrarrojos y ultravioleta. En un entorno con luz solar intensa, no pueden funcionar normalmente.

3\. **Diagrama de flujo**

![Img](./media/Makecode_e5f416e3.png)

4\. **Código de prueba**

![](./media/Makecode_22d06d74.png)

Haga clic en “JavaScript" para cambiar al código JavaScript correspondiente:

![](./media/Makecode_e68b6275.png)

![](./media/Makecode_94de6552.png)

5\. **Resultado de la prueba**

Descargue el código en la placa micro:bit y ponga el interruptor POWER en ON.

Apunte el mando IR al micro:bit y pulse el botón para controlar el movimiento del coche inteligente.

![](./media/Makecode_d55474f3.png) el botón hace que el coche inteligente avance，![](./media/Makecode_5c8a6549.png) representa girar a la izquierda，![](./media/Makecode_41116032.png) implica giro a la derecha，![](./media/Makecode_369433f6.png) indica marcha atrás，![](./media/Makecode_a8ef4b17.png) detiene el coche.

**Nota:** La distancia entre el mando IR y la cabeza receptora IR del coche inteligente debe ser inferior a 5 m durante la prueba.

---