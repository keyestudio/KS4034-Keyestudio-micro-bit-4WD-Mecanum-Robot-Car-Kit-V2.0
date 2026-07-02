## プロジェクト6: 地磁気センサー

[Click to download the code 1 for this lesson](./Code/Geomagnetic-Sensor.hex)

[Click to download the code 2 for this lesson](./Code/Geomagnetic-Sensor2.hex)

### (1)プロジェクトの説明:

(1) プロジェクトの説明: 本プロジェクトは Micro:bit の地磁気センサーの使い方を説明することを目的としています。地磁気の強さを検出できるだけでなく、方位を求めるためのコンパスとしても使用できます。また、姿勢方位基準系（AHRS: Attitude and Heading Reference System）の重要な一部でもあります。Micro:bit main board V2 は LSM303AGR 地磁気センサーを使用しており、磁場のダイナミックレンジは ±50 ガウスです。ボード上では、磁力計モジュールが磁気検出およびコンパスの両方に使用されています。本実験ではまずコンパスを紹介し、その後磁力計の生データを確認します。一般的なコンパスの主な構成要素は磁針であり、地磁気によって回転し、方角を決定するために地磁気北極（地理的な南極の近くにある）を指します。

### (2)必要な部品:

Micro:bit main board V2

 Micro USB ケーブル

### (3)テストコード 1 :

Micro USB ケーブルでコンピュータと micro:bit ボードを接続し、MakeCode エディタでプログラミングします。

![](./media/Makecode_5805c7de.gif)

完成プログラム :

![](./media/Makecode_5a958132.png)

### (4)テスト結果 1 :

テストコードを Micro:bit main board V2 に書き込み、USB ケーブルでボードに電源を供給し、ボタン A を押すと、ボードがコンパスの校正を促し、LED ドットマトリクスに "TILT TO FILL SCREEN" が表示されます。すると校正ページに入ります。下図のように 25 個の LED がすべて赤く点灯するまでボードを回転させます。

![](./media/Makecode_b0a4ebf1.jpg)

コンパスを校正:

![](./media/Makecode_05a88e21.gif)

その後、スマイルのパターン ![](./media/Makecode_74a69436.png)が表示され、校正が完了したことを示します。校正プロセスが完了すると、ボタン A を押すことで磁力計の読み取り値が画面に直接表示されます。北、東、南、西の方向はそれぞれ 0°、90°、180°、270° に対応します。

![](./media/Makecode_23b07bfb.gif)

### (5) テストコード 2:

このモジュールは方向を決定するために継続的にデータを読み取ることができ、矢印で現在の磁気北極を指します。

Micro USB ケーブルでコンピュータと micro:bit ボードを接続し、MakeCode エディタでプログラミングします、

![](./media/Makecode_db8b2d7e.gif)

完成プログラム :

![](./media/Makecode_ef823069.png)

### (6) テスト結果 2

コード2をアップロードします。校正後、micro:bit ボードを傾けると、LED ドットマトリクスに方位表示が表示されます。

![](./media/Makecode_d8944d5f.gif)

---