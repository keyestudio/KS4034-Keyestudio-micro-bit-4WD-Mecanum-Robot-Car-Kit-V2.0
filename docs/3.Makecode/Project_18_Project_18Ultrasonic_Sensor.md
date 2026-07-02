## Proyecto 18：Sensor ultrasónico

### Proyecto 18.1：Medición de distancia por ultrasonidos

1\.  **Descripción**

El sensor ultrasónico utiliza sonar para determinar la distancia a un objeto, como lo hacen los murciélagos. Ofrece una excelente detección de rango sin contacto, con alta precisión y lecturas estables en un paquete fácil de usar. Incluye módulos transmisor y receptor ultrasonicos.

El sensor ultrasónico se usa en una amplia gama de proyectos electrónicos para crear aplicaciones de detección de obstáculos y medición de distancia, además de otras aplicaciones.

![](./media/Makecode_0180b169.png)

El módulo ultrasónico emitirá las ondas ultrasónicas después de las señales de disparo (trigger). Cuando las ondas se encuentran con un objeto y se reflejan, el módulo emite una señal de eco, por lo que puede determinar la distancia al objeto a partir de la diferencia de tiempo entre la señal de disparo (TRIG) y la señal de eco (ECHO).

Como muestra la imagen, es como dos ojos. Uno es el extremo transmisor y el otro el extremo receptor.

Según el diagrama de cableado anterior, el puerto integrado del módulo del sensor ultrasónico está conectado al puerto 5V G P15 P16 en la placa base del controlador de motor micro:bit. El pin Trig (T) lo controla P15 del micro:bit y el pin Echo (E) está en P16.

![](./media/Makecode_1174e0ec.png)

2\. **Principio de funcionamiento**

![](./media/Makecode_8ff02741.png)

(1) Llevar TRIG a bajo y luego generar una señal alta de al menos 10 µs;

(2) Tras el disparo, el módulo enviará automáticamente ocho pulsos ultrasónicos de 40 kHz y detectará si hay retorno de señal;

(3) Si hay retorno de señal, cuando ECHO (E) emite nivel alto, la duración del nivel alto es el tiempo desde la transmisión hasta la recepción de las ondas ultrasónicas. Entonces distancia de prueba = duración de nivel alto \*340m/s\*0.5. 

3\. **Parámetros**

- Tensión de trabajo: 3-5.5V (DC)

- Corriente de trabajo: 15mA

- Frecuencia de trabajo: 40 kHz

- Distancia máxima de detección: alrededor de 3 m

- Distancia mínima de detección: 2-3 cm

- Precisión: hasta 0,2 cm

- Ángulo de detección: menos de 15 grados

- Pulso de disparo de entrada: 10 µs nivel TTL

- Señal de eco de salida: salida de señal a nivel TTL (alto), proporcional al rango

4\. **Preparación**

- Inserte la placa micro:bit en la ranura del keyestudio 4WD Mecanum Robot Car V2.0

- Coloque las baterías en el portapilas

- Ponga el interruptor de alimentación en ON

- Conecte el micro:bit a su ordenador mediante un cable USB

- Abra la versión web de Makecode


5\. **Código de prueba**

![](./media/Makecode_497760b1.png)

Haga clic en “JavaScript” para ver el código JavaScript correspondiente:

![](./media/Makecode_387f3243.png)

6\.  **Resultado de la prueba**

Descargue el código al micro:bit, mantenga el cable USB conectado y ponga el interruptor POWER en ON. El valor de la distancia se mostrará en el monitor.

![](./media/Makecode_2cd74c16.png)

El monitor muestra la distancia entre el obstáculo y el sensor ultrasónico (como se muestra a continuación).

![](./media/Makecode_422adea3.png)

Abra CoolTerm, haga clic en Options para seleccionar SerialPort. Configure el puerto COM y la tasa en 115200 baudios (la tasa de comunicación serial USB del Micro:bit es 115200 según la prueba). Haga clic en “OK” y “Connect”.

El monitor serie de CoolTerm muestra el valor de la distancia como sigue:

![](./media/Makecode_69b06998.png)

### Proyecto 18.2：Evitación por ultrasonidos

![Img](./media/Makecode_13139b46.png)

1\. **Descripción**

En este proyecto integraremos un sensor ultrasónico y un coche para crear un coche de evitación por ultrasonidos.

Su principio es detectar la distancia entre el coche y el obstáculo mediante el sensor ultrasónico para controlar el movimiento del coche inteligente.

2\.  **Preparación**

- Inserte la placa micro:bit en la ranura del keyestudio 4WD Mecanum Robot Car V2.0

- Coloque las baterías en el portapilas

- Ponga el interruptor de alimentación en ON

- Conecte el micro:bit a su ordenador mediante un cable USB

- Abra la versión web de Makecode

3\.  **Diagrama de flujo**

![Img](./media/Makecode_e2adae4b.png)

4\.  **Código de prueba**

![](./media/Makecode_05a4740b.png)

![Img](./media/Makecode_d7879887.png)

Haga clic en “JavaScript” para ver el código JavaScript correspondiente:

![](./media/Makecode_c8f86a24.png)

![](./media/Makecode_13baf1d6.png)

5\.  **Resultado de la prueba**

Descargue el código al micro:bit, enciéndalo y ponga el interruptor POWER en ON. Cuando la distancia al obstáculo sea mayor de 20 cm, el coche avanza; en caso contrario, el coche inteligente gira a la izquierda.

### Proyecto 18.3：Seguimiento por ultrasonidos

![Img](./media/Makecode_d17a7889.png)

1\. **Descripción**

En la lección anterior aprendimos el principio básico del sensor de seguimiento de línea. A continuación combinaremos el sensor ultrasónico con el coche para crear un coche seguidor ultrasónico.

El sensor ultrasónico detecta la distancia del obstáculo y controla el estado de movimiento del coche.

2\. **Preparación**

- Inserte la placa micro:bit en la ranura del keyestudio 4WD Mecanum Robot Car V2.0

- Coloque las baterías en el portapilas

- Ponga el interruptor de alimentación en ON

- Conecte el micro:bit a su ordenador mediante un cable USB

- Abra la versión web de Makecode

3\. **Diagrama de flujo**

![Img](./media/Makecode_f5026aed.png)

4\. **Código de prueba**

![](./media/Makecode_03b95531.png)

Haga clic en “JavaScript” para ver el código JavaScript correspondiente:

![](./media/Makecode_a93c8245.png)

5\. **Resultado de la prueba**

Descargue el código al micro:bit, ponga el interruptor POWER en ON en el shield; el coche inteligente podrá seguir el obstáculo y moverse.