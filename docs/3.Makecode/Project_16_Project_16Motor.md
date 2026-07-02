## Project 16：Motor

![](./media/Makecode_77f3b857.png)

1\.  **Descripción**

El Keyestudio 4WD Mecanum Robot Car está equipado con 4 motores DC de reducción, también llamados motores con caja reductora, desarrollados a partir del motor DC ordinario. Cuenta con una caja reductora a juego que proporciona una velocidad menor pero un mayor par. Además, diferentes relaciones de reducción de la caja pueden proporcionar distintas velocidades y pares.

El motor con engranajes es la integración del motor reductor y el motor, que se aplica ampliamente en la industria del acero y la ingeniería mecánica.

El shield controlador de motor para micro:bit viene con un chip DRV8833. Para ahorrar recursos de puertos IO, controlamos la dirección de rotación y la velocidad de los 4 motores DC con reductor mediante el chip DRV8833.

![Img](./media/Makecode_4c9781dc.png)

Front

![](./media/Makecode_4919ce3b.png)

Back

![](./media/Makecode_59c34b6e.png)

STC8G1K08 Chip circuit

![](./media/Makecode_8874ded0.png)

HR8833 Motor driver circuit

2\.  **Preparación**

- Inserte la placa micro:bit en la ranura del keyestudio 4WD Mecanum Robot Car V2.0

- Coloque las pilas en el portapilas

- Gire el interruptor de encendido a la posición ON

- Conecte el micro:bit a su ordenador mediante un cable USB

- Abra la versión web de Makecode

3\.  **Test Code1**

![](./media/Makecode_3a759dd8.png)

Haga clic en“JavaScript" para ver el código JavaScript correspondiente: 

![](./media/Makecode_242ba6ca.png)

4\.  **Resultado de la prueba1**

Descargue el código 1 en la placa micro:bit, gire el interruptor POWER a ON. El coche inteligente avanza durante 2s y se detiene durante 2s.

5\.  **Test Code2**

![](./media/Makecode_a3a9d39a.png)

![Img](./media/Makecode_4eb6b574.png)

Haga clic en“JavaScript" para ver el código JavaScript correspondiente: 

![](./media/Makecode_ee70b846.png)

6\.  **Resultado de la prueba2**

Descargue el código 2 en la placa micro:bit, el coche avanza durante 2s, retrocede durante 2s, gira a la izquierda durante 2s, gira a la derecha durante 2s, se detiene durante 2s y repite este patrón.