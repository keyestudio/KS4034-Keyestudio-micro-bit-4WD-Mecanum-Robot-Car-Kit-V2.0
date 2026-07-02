### プロジェクト 17：ライン追跡センサー

#### プロジェクト 17.1：ライン追跡センサーの検出

![](./media/Python_ea7f6c8c.png)

1\. **説明**

Keyestudio 4WD Mecanum ロボットカーのモータードライバーボードには、TCRT5000 赤外線素子と3つのポテンショメータを採用した3チャネルのライン追跡センサーが搭載されています。

TCRT5000 は赤外線発光素子と受光素子を内蔵しています。発光素子から放射された赤外線が反射を介して受光素子に届くと、受光素子の抵抗が変化し、それが回路上の電圧変化として一般に表れます。　

受光素子が受ける赤外線の強度によって抵抗は変化し、反射面の色や受光素子との距離に依存します。検出時には、黒がハイレベル（アクティブ）、白がローレベル（非アクティブ）となります。　

2\.  **動作原理**

車が白い路面の上を走行すると、車体底部に設置された赤外線発光素子が路面に向けて赤外線を照射し、受光素子が反射光を受信して信号を返します。そのとき出力端はローレベル(0)を出力します。黒い線を検出すると、ハイレベル(1)を出力します。

4WD Mecanum ロボットカーに統合された3チャネル追跡センサーのコネクタは、micro:bit 拡張ボードの G、5V、P10、P4、P3 の収集ポートに接続されており、micro:bit の P10、P4、P3 によって制御されます。センサーの左側の TCRT5000 赤外線ペアは P3 で制御され、中央は P4、右側は P10 で制御されます。

4WD Mecanum ロボットカーの底部に白い紙を置き、3路の追跡センサー上のポテンショメータを回します。センサーモジュールのインジケータが点灯したら、車を持ち上げて 4WD Mecanum ロボットカーの両輪を分離させます。白い紙の高さは約1.5cm にし、センサーモジュールのインジケータが消灯したら感度を調整します。

**注意：5×5 ドットマトリクスは P3、P4、P6、P7、P10 を使用するため、ライン追跡センサーを使うときはドットマトリクス機能をオフにする必要があります。**

3\.  **準備**

- micro:bit ボードを keyestudio 4WD Mecanum Robot Car V2.0 のスロットに挿入する

- 電池をバッテリーホルダに入れる

- 電源スイッチを ON にする

- USB ケーブルで micro:bit をコンピュータに接続する

- Mu のオフライン版を開く

4\.  **テストコード**

Mu を起動し、ファイル “Line tracking detection\.py” を開いてコードを読み込みます。編集ウィンドウに自分でコードを入力することもできます。

（注：英文や記号はすべて英語で記述してください。）

「Check」をクリックしてコードのエラーを確認します。下線やエラー表示がある場合はプログラムに誤りがあります。

コードが正しければ、micro:bit をコンピュータに接続し「Flash」をクリックしてコードを micro:bit ボードに書き込みます。

![](./media/Python_2c7b1c21.png)

```python
from microbit import *
display.off()

val_L = 0
val_C = 0
val_R = 0
while True:
    val_L = pin3.read_digital()
    val_C = pin4.read_digital()
    val_R = pin10.read_digital()
    print("digital signal:", end = ' ')
    print(val_L, end = ' ')
    print(val_C, end = ' ')
    print(val_R)
    sleep(200)
```

5\.  **テスト結果**

コードをボードに正常に書き込んだ後、USB ケーブルは抜かないでください。「REPL」をクリックしてからリセットボタンを押します。

![Img](./media/Python_bb3e1312.png)

左側の TCRT5000 赤外線素子が検出した値がモニタに表示されます。

左側の TCRT5000 が白い物体を検出すると 0 が表示され、左のインジケータが点灯します。黒い物体のみを検出すると 1 が表示され、インジケータは消灯します。以下のように表示されます：

![](./media/Python_6a25b450.png)

6\.  **コードの説明**

![Img](./media/Python_5dad345e.png)


#### プロジェクト 17.2：ライン追跡スマートカー

![](./media/Python_f0b62e0f.jpg)

1\. 説明

このレッスンでは、ライン追跡センサーとモーターを組み合わせてライン追跡スマートカーを作ります。

micro:bit ボードがセンサーの信号を解析し、スマートカーを制御してライン追跡の動作を行います。

2\.  **動作原理**

3チャネルライン追跡センサーが受け取る値に応じて、スマートカーは異なる動作を行います。

![Img](./media/Python_e672c637.png)

3\.  **準備**

- micro:bit ボードを keyestudio 4WD Mecanum Robot Car V2.0 のスロットに挿入する

- 電池をバッテリーホルダに入れる

- 電源スイッチを ON にする

- USB ケーブルで micro:bit をコンピュータに接続する

- Mu のオフライン版を開く

**警告：** 3路追跡センサーは直射日光のような赤外線の干渉がない環境で使用してください。太陽光には赤外線や紫外線など多数の不可視光が含まれており、強い日光下では 3路追跡センサーは正しく動作しないことがあります。

4\.  **フローチャート**

![Img](./media/Python_47856ed2.png)

5\.  **テストコード**

Mu を起動し、ファイル “Line tracking car\.py” を開いてコードを読み込みます。編集ウィンドウに自分でコードを入力することもできます。

（注：英文や記号はすべて英語で記述してください。）

「Files」をクリックして “keyes_mecanum_Car.py” ライブラリファイルを micro:bit に取り込みます。

「Check」をクリックしてコードのエラーを確認します。下線やエラー表示がある場合はプログラムに誤りがあります。

コードが正しければ、micro:bit をコンピュータに接続し「Flash」をクリックしてコードを micro:bit ボードに書き込みます。

![](./media/Python_bd395cbe.png)

```python
from microbit import *
from keyes_mecanum_Car_V2 import *
mecanumCar = Mecanum_Car_Driver_V2()
display.off()

val_L = 0
val_C = 0
val_R = 0
while True:
    val_L = pin3.read_digital()
    val_C = pin4.read_digital()
    val_R = pin10.read_digital()
    if val_C == 0:
        if val_L == 0 and val_R == 1:
            mecanumCar.Motor_Upper_L(1, 80)
            mecanumCar.Motor_Lower_L(1, 80)
            mecanumCar.Motor_Upper_R(0, 80)
            mecanumCar.Motor_Lower_R(0, 80)
        elif val_L == 1 and val_R == 0:
            mecanumCar.Motor_Upper_L(0, 80)
            mecanumCar.Motor_Lower_L(0, 80)
            mecanumCar.Motor_Upper_R(1, 80)
            mecanumCar.Motor_Lower_R(1, 80)
        else:
            mecanumCar.Motor_Upper_L(0, 0)
            mecanumCar.Motor_Lower_L(0, 0)
            mecanumCar.Motor_Upper_R(0, 0)
            mecanumCar.Motor_Lower_R(0, 0)
    else :
        if val_L == 0 and val_R == 1:
            mecanumCar.Motor_Upper_L(1, 80)
            mecanumCar.Motor_Lower_L(1, 80)
            mecanumCar.Motor_Upper_R(0, 80)
            mecanumCar.Motor_Lower_R(0, 80)
        elif val_L == 1 and val_R == 0:
            mecanumCar.Motor_Upper_L(0, 80)
            mecanumCar.Motor_Lower_L(0, 80)
            mecanumCar.Motor_Upper_R(1, 80)
            mecanumCar.Motor_Lower_R(1, 80)
        else:
            mecanumCar.Motor_Upper_L(1, 80)
            mecanumCar.Motor_Lower_L(1, 80)
            mecanumCar.Motor_Upper_R(1, 80)
            mecanumCar.Motor_Lower_R(1, 80)
```
6\.  **テスト結果**

コードをボードに正常に書き込んだ後、**外部電源（DIPスイッチを ON に切り替える）** を用意し、micro:bit のリセットボタンを押します。

![Img](./media/Python_bb3e1312.png)

ライン追跡カーは黒い線に沿って前進します。

**注意：** （1）追跡時の黒線の幅は、ライン追跡センサーの幅と同じかそれ以上である必要があります。

（2）強い光の下でのテストは避けてください。


7\.  **コードの説明**

![Img](./media/Python_b16f9d7b.png)

![Img](./media/Python_35f35a4c.png)

---