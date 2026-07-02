## Proyecto 15：Servo

![](./media/Makecode_215da878.png)

1\.  **Descripción**

En los coches inteligentes DIY, a menudo se incluye la función de evitación automática de obstáculos. En el proceso de construcción necesitamos usar un servo para controlar que el módulo ultrasónico gire hacia la izquierda y la derecha, y así detectar la distancia entre el coche y el obstáculo, de modo que se pueda controlar el coche para evitarlo. Si se utilizan otros microcontroladores para controlar la rotación del servo, es necesario establecer una cierta frecuencia y una determinada anchura de pulso para controlar el ángulo del servo.

Sin embargo, si se utiliza la placa principal micro:bit para controlar el ángulo del servo, solo es necesario establecer el ángulo de control en el entorno de desarrollo; el pulso correspondiente se generará automáticamente para controlar la rotación del servo. En este proyecto aprenderás a controlar el servo para que gire hacia adelante y hacia atrás entre 0° y 90°.

2\.  **Información del Servo**

El servomotor es un actuador rotativo de control de posición. Se compone principalmente de carcasa, placa de circuito, motor sin núcleo, engranajes y sensor de posición. Su principio de funcionamiento es que el servo recibe la señal enviada por el MCU o el receptor, genera una señal de referencia con un periodo de 20 ms y una anchura de 1.5 ms, luego compara la tensión de polarización continua obtenida con la tensión del potenciómetro y obtiene la diferencia de tensión como salida.

![](./media/Makecode_87b41036.png)

Para el servo usado en este proyecto, el cable marrón es la masa, el rojo es el positivo y el naranja es el cable de señal.

El ángulo de rotación del servomotor se controla regulando el ciclo de trabajo de la señal PWM (Pulse-Width Modulation). El ciclo estándar de la señal PWM es de 20 ms (50 Hz). Teóricamente la anchura se distribuye entre 1 ms y 2 ms, pero en la práctica está entre 0.5 ms y 2.5 ms. La anchura corresponde al ángulo de rotación de 0° a 180°. Tenga en cuenta que para motores de marcas diferentes, la misma señal puede producir ángulos de rotación distintos.

![](./media/Makecode_49467dfa.png)

Más detalles:

![](./media/Makecode_b167d550.png)

3\.  **Parámetros**

- Tensión de trabajo: DC 4.8V ~ 6V

- Rango de ángulo operativo: alrededor de 180 ° (a 500 → 2500 μsec)

- Rango de anchura de pulso: 500 → 2500 μsec

- Velocidad sin carga: 0.12 ± 0.01 s / 60 (DC 4.8V) 0.1 ± 0.01 s / 60 (DC 6V)

- Corriente sin carga: 200 ± 20mA (DC 4.8V) 220 ± 20mA (DC 6V)

- Par de detención: 1.3 ± 0.01kg·cm (DC 4.8V) 1.5 ± 0.1kg·cm (DC 6V)

- Corriente de parada: ≦ 850mA (DC 4.8V) ≦ 1000mA (DC 6V)

- Corriente en espera: 3 ± 1mA (DC 4.8V) 4 ± 1mA (DC 6V)

4\.  **Preparación**

- Inserte la placa micro:bit en la ranura del keyestudio   4WD Mecanum Robot Car V2.0

- Coloque las pilas en el portapilas

- Ponga el interruptor de alimentación en la posición ON

- Conecte la micro:bit a su ordenador mediante un cable USB

- Abra la versión Web de Makecode


5\.  **Código de prueba**

![](./media/Makecode_087e1822.png)

Haga clic en "JavaScript" para ver el código JavaScript correspondiente:

![](./media/Makecode_2354311f.png)

6.  **Resultado de la prueba**

Tras cargar el código de prueba y colocar el interruptor POWER en ON, el servo gira de 0 grados a 180 grados.