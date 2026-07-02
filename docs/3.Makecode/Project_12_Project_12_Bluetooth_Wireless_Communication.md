## Proyecto 12: Comunicación inalámbrica Bluetooth

![](./media/Makecode_041ff91a.jpg)

### (1)Descripción del proyecto:

Nota: Esta lección se centra en explicar cómo subir código vía Bluetooth usando una app, por lo que no se proporciona código. Por favor, siga los pasos en el gif animado.

La placa principal Micro: Bit main board V2 viene con un procesador nRF52833 (con un dispositivo BLE (Bluetooth Low Energy) integrado, Bluetooth 5.1) y una antena de 2,4 GHz para la comunicación inalámbrica Bluetooth y la comunicación inalámbrica de 2,4 GHz. Con su ayuda, la placa puede comunicarse con una variedad de dispositivos Bluetooth, incluidos teléfonos inteligentes y tabletas.

En este proyecto nos centramos principalmente en la función de comunicación inalámbrica Bluetooth de esta placa principal. Conectada por Bluetooth, puede transmitir código o señales. Para ello, debemos conectar un dispositivo Apple (un iPhone o un iPad) a la placa.

Dado que la configuración de los teléfonos Android para lograr la transmisión inalámbrica es similar a la de los dispositivos Apple, no es necesario ilustrarla de nuevo.

### (2) Preparación

Conexión del Micro:bit main board V2 a su ordenador mediante el cable Micro USB.

Un dispositivo Apple (un teléfono o un iPad) o un dispositivo Android;

### (3) Instalar Micro:bit:

Para Android

![](./media/Makecode_0cf9abf0.gif)

Para ios

![](./media/Makecode_5937459b.gif)

(4)Código de prueba:

A continuación, usaremos nuestros teléfonos para escribir código y conectarnos vía Bluetooth (Nota: el proceso es idéntico para dispositivos Android e iOS; esta demostración usa un teléfono Android).

1、Abra el software y conéctese a Bluetooth.

![](./media/Makecode_dcb2416a.gif)

2、Presione en secuencia el botón A del Microbit, el botón B y el botón de reinicio en la parte posterior. La placa principal mostrará entonces un icono.

![](./media/Makecode_6985c2b1.gif)

3、Introduzca el patrón que se muestra en el paso dos en la interfaz del teléfono.

![](./media/Makecode_9095fb35.gif)

Escribir código y subir

1、Acceda a la interfaz de programación de código y escriba un código.

![](./media/Makecode_b7c8c1ca.gif)

2、Presione en secuencia el botón A, el botón B y el botón de reinicio. (Nota: este procedimiento debe repetirse cada vez que se sube código mediante la app.)

 ![](./media/Makecode_86ab2b39.gif)

3、Después de confirmar que el icono Microbit coincide con el que se muestra en su teléfono, simplemente haga clic en “Next”.

![](./media/Makecode_f3c17f45.gif)

Finalmente, podrá ver la placa Microbit mostrando el patrón del código.

Aquí hemos completado el proceso de subir código al teléfono. Es importante tener en cuenta:

1. Para conectar el teléfono a la placa Microbit, presione en secuencia los botones A, B y Reset. La pantalla de matriz de puntos mostrará entonces un patrón, que debe introducirse en el teléfono.
2. La placa Microbit puede alimentarse mediante un cable USB o suministrando 3V a la entrada de alimentación de la placa mediante un paquete de baterías. Nota: el voltaje no debe exceder los 3V, ya que superarlo dañará la placa.