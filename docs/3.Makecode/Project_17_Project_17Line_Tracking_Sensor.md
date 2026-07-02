## Proyecto 17：Line Tracking Sensor

### Proyecto 17.1：Detect Line Tracking Sensor

![](./media/Makecode_ea7f6c8c.png)

1\. **Descripción**

La placa controladora del Keyestudio 4WD Mecanum Robot Car viene con un sensor de seguimiento de línea de 3 canales, que emplea módulos IR TCRT5000 y 3 potenciómetros.

El módulo IR TCRT5000 contiene un emisor IR y un receptor IR. Cuando las señales infrarrojas del emisor son recibidas por el receptor tras la reflexión, la resistencia del receptor cambia, lo que generalmente se refleja en un cambio de tensión en el circuito.  

La resistencia varía según la intensidad de las señales infrarrojas recibidas por el receptor, lo que suele depender del color de la superficie reflectante y de la distancia entre la superficie reflectante y el receptor. En el momento de la detección, el negro es nivel alto activo y el blanco es nivel bajo activo. 

2\.  **Principio de funcionamiento**

Cuando el coche circula sobre una pista blanca, el tubo emisor IR instalado bajo el coche emite señales infrarrojas para detectar la pista y el tubo receptor recibe las señales y las devuelve. Entonces la salida proporciona nivel bajo (0); cuando detecta líneas negras, proporciona nivel alto (1).

Después de colocar un papel blanco en la parte inferior del 4WD Mecanum Robot Car, giraremos los potenciómetros del sensor de seguimiento de 3 vías. Cuando la luz indicadora del módulo del sensor esté encendida, levante el coche para que las dos ruedas del 4WD Mecanum Robot Car queden separadas y puedan girar libremente. La altura del papel blanco es de aproximadamente 1,5 cm; cuando la luz indicadora del módulo del sensor se apaga, la sensibilidad está ajustada.

3\.  **Preparación**

- Inserte la placa micro:bit en la ranura del keyestudio 4WD Mecanum Robot Car V2.0

- Coloque las pilas en el portapilas

- Gire el interruptor de alimentación a ON

- Conecte el micro:bit a su ordenador mediante un cable USB

- Abra la versión Web de Makecode

4\.  **Código de prueba**

![](./media/Makecode_3683d83f.png)

Haga clic en “JavaScript” para ver el código JavaScript correspondiente: 

![](./media/Makecode_4b440616.png)

5\.  **Resultado de la prueba**

Descargue el código en la placa micro:bit y ponga el interruptor POWER en ON. 

Abra CoolTerm, haga clic en Options para seleccionar SerialPort. Establezca el puerto COM y la velocidad en baudios a 115200. Haga clic en “OK” y “Connect”.

![](./media/Makecode_ea164439.png)

![](./media/Makecode_b3a18bca.png)

![](./media/Makecode_f78128c1.png)

![](./media/Makecode_13238e98.png)

El monitor serie de CoolTerm muestra las señales digitales leídas por los sensores de seguimiento de línea.

![](./media/Makecode_0141051a.png)

### Proyecto 17.2：Tracking Smart Car

![Img](./media/Makecode_547634e4.png)

1\. **Descripción**

En esta lección combinaremos un sensor de seguimiento de línea con un motor para construir un coche inteligente de seguimiento de línea.

La placa micro:bit analizará las señales y controlará el coche inteligente para mostrar la función de seguimiento de línea.

2\. **Principio de funcionamiento**

El coche inteligente ejecutará movimientos diferentes según los valores recibidos por el sensor de seguimiento de línea de 3 canales.

![Img](./media/Makecode_bbccdb34.png)

3\. **Preparación**

- Inserte la placa micro:bit en la ranura del keyestudio 4WD Mecanum Robot Car V2.0

- Coloque las pilas en el portapilas

- Gire el interruptor de alimentación a ON

- Conecte el micro:bit a su ordenador mediante un cable USB

- Abra la versión Web de Makecode

**Advertencia:** El sensor de seguimiento de 3 vías debe usarse en entornos sin interferencias infrarrojas, como la luz solar. La luz solar contiene mucha luz invisible, como infrarrojo y ultravioleta. En un entorno con luz solar intensa, el sensor de 3 vías no podrá funcionar correctamente.

4\.**Diagrama de flujo**

![Img](./media/Makecode_70f1fd80.png)


5\.  **Código de prueba**

![](./media/Makecode_4b104155.png)

![Img](./media/Makecode_d36220cf.png)

![Img](./media/Makecode_4fff0a27.png)

![Img](./media/Makecode_ca91a31f.png)


Haga clic en “JavaScript” para ver el código JavaScript correspondiente:

![](./media/Makecode_f5caa06a.png)

![](./media/Makecode_8f5f07ec.png)

5\. **Resultado de la prueba**

Descargue el código en el micro:bit y ponga POWER en ON; el coche seguidor de línea avanza siguiendo la línea negra.

**Nota:** encienda el interruptor en la parte posterior del coche micro:bit; el ancho de la línea negra debe ser mayor que el ancho del sensor de seguimiento de línea.

Evite probar el coche inteligente bajo luz intensa.