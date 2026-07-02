### プロジェクト 7：Accelerometer

![](./media/Python_26d107ae.png)

1\.  **説明**

micro: bit main board V2 には、LSM303AGR 重力加速度センサー（加速度計とも呼ばれる）が内蔵されており、分解能は 8/10/12 ビットです。コード内ではレンジを 1g、2g、4g、8g に設定できます。

加速度センサーは機械の状態を検出するためによく使用します。

このプロジェクトでは、加速度センサーを使ってボードの向きを測定する方法を紹介します。その後、加速度センサーが出力する生の三軸データを確認します。

2\.  **準備**

A. USB ケーブルで micro:bit main board をコンピュータに接続します。

B. Mu のオフライン版を開きます。

3\.  **テストコード1**

Mu ソフトを起動し、ファイル “Three-axis acceleration sensor -1\.py“ を開いてコードを読み込みます。編集ウィンドウにコードを自分で入力することもできます。

(**注意: すべての単語および記号は英語で記述してください。**)

![](./media/Python_f20f5b58.png)

```python
from microbit import *

while True:
    gesture = accelerometer.current_gesture()

    if gesture == "shake":
        display.show("1")
    if gesture == "up":
        display.show("2")
    if gesture == "down":
        display.show("3")
    if gesture == "face up":
        display.show("4")
    if gesture == "face down":
        display.show("5")
    if gesture == "left":
        display.show("6")
    if gesture == "right":
        display.show("7")
    if gesture == "freefall":
        display.show("8")
```

「Check」をクリックしてコードのエラーを確認します。下線やカーソルが表示される場合、プログラムは正しくありません。 

![](./media/Python_07e4b578.png)

コードが正しければ、micro:bit をコンピュータに接続して「Flash」をクリックし、コードを micro:bit ボードに書き込みます。

![](./media/Python_eb56750b.png)

4\.  **テスト結果1**

コードをボードに正常にダウンロードしたら、**micro USB ケーブルまたは外部電源で給電する（DIP スイッチを ON にする）**、その後 micro:bit のリセットボタンを押します。

![Img](./media/Python_bb3e1312.png)

micro: bit main board を振ると、方向に関係なく LED ドットマトリクスに数字「1」が表示されます。

ボードを立てた状態（ロゴが LED マトリクスの上に来る）では、数字 2 が表示されます。

![](./media/Python_b91421df.jpg)

上下逆さま（ロゴが LED マトリクスの下に来る）に保持すると、下図のように表示されます。

![](./media/Python_69e81587.jpg)

机の上に静かに置き、表側が上を向いているときは数字 4 が表示されます。

![](./media/Python_9e08cb69.jpg)

机の上に静かに置き、裏側が上を向いているときは数字 5 が表示されます。

ボードを左に傾けると、LED ドットマトリクスに数字 6 が表示されます（下図参照）。

![](./media/Python_81fa2ce1.jpg)

ボードを右に傾けると、LED ドットマトリクスに数字 7 が表示されます（下図参照）：

![](./media/Python_fc13912b.jpg)

ボードを床に叩きつけると、この動作は自由落下とみなすことができ、LED マトリクスに数字 8 が表示されます。（このテストはメインボードを損傷する可能性があるため推奨しません。）

**注意：この機能を試したい場合、加速度を 3g、6g、または 8g に設定することもできます。**

5\.  **テストコード2**

Mu ソフトを起動し、ファイル “Three-axis acceleration sensor -2\.py“ を開いてコードを読み込みます。編集ウィンドウにコードを自分で入力することもできます。

(**注意: すべての単語および記号は英語で記述してください。**)

![](./media/Python_0f7ccf57.png)

```python
from microbit import *

while True:

    x = accelerometer.get_x()

    y = accelerometer.get_y()

    z = accelerometer.get_z()

    print("x, y, z:", x, y, z)

    sleep(100)
```
「Check」をクリックしてコードのエラーを確認します。下線やカーソルが表示される場合、プログラムは正しくありません。 

![](./media/Python_0ed2221e.png)

コードが正しければ、micro:bit をコンピュータに接続して「Flash」をクリックし、コードを micro:bit ボードに書き込みます。

![](./media/Python_35c4c76b.png)

6\.  **テスト結果2**

コードをボードに正常にダウンロードしたら、**micro USB ケーブルまたは外部電源で給電する（DIP スイッチを ON にする）**。 「REPL」をクリックし、micro:bit のリセットボタンを押します。

![Img](./media/Python_bb3e1312.png)

すると REPL ウィンドウに X 軸、Y 軸、Z 軸の加速度の値が以下のように表示されます：

![](./media/Python_940cfcf7.png)

MMA8653FC のデータマニュアルおよび micro: bit main board のハードウェア回路図を参照すると、micro: bit の加速度計座標は下図のようになります：

![](./media/Python_ebd0d44d.png)

7\.  **コードの説明**

![Img](./media/Python_d533d72c.png)

![Img](./media/Python_89d95342.png)

---