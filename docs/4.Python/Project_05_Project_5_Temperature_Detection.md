### プロジェクト 5：温度検出

1\.  **説明**

Micro:bit メインボードには温度センサーが搭載されていませんが、温度検出のために NFR52833 チップに内蔵された温度センサーを使用します。したがって、検出される温度はチップの温度に近く、周囲温度とずれが生じる可能性があります。

このプロジェクトでは、センサーを使用して現在の環境の温度を測定し、測定結果を表示装置に表示します。その後、センサーで検出した温度範囲を設定して LED ドットマトリクスに異なるパターンを表示させます。

**注: Micro:bit メインボードの温度センサーは以下の通りです:**

![](./media/Python_206c8ec1.png)

2\.  **準備**

A. USB ケーブルで micro:bit メインボードをコンピュータに接続します

B. Mu のオフラインバージョンを開きます。

3\.  **テストコード1**

Mu を起動し、ファイル “Temperature Measurement -1\.py “ を開いてコードを読み込みます。編集ウィンドウに直接コードを入力することもできます。

(**注: すべての単語と記号は英語で記述する必要があります。**)

![](./media/Python_03cbb6e9.png)

```python
from microbit import *

while True:

    Temperature = temperature()

    print("Temperature:", Temperature, "C")

    sleep(500)
```

“Check” をクリックしてコードのエラーを確認します。下線やカーソルが表示される場合、プログラムに誤りがあります。 

![](./media/Python_7b437c2d.png)

コードが正しければ、micro:bit をコンピュータに接続し “Flash” をクリックしてコードを micro:bit ボードに書き込みます。

![](./media/Python_193065ab.png)

4\.  **テスト結果1**

コードが正常にボードに書き込まれたら、**micro USB ケーブルまたは外部電源で電源を入れてください（DIP スイッチを ON にしてください）**。“REPL” をクリックし、micro:bit のリセットボタンを押します。

![Img](./media/Python_bb3e1312.png)

すると REPL ウィンドウに周囲温度の値が表示されます。以下の例を参照してください:（C は温度の単位を表します）

![](./media/Python_d08386d8.png)

5\.  **テストコード2**

Mu を起動し、ファイル “Temperature Measurement -2\.py “ を開いてコードを読み込みます。編集ウィンドウに直接コードを入力することもできます。

(**注: すべての単語と記号は英語で記述する必要があります。**)

温度値は実際の温度に合わせて設定できます。

![](./media/Python_c6456d78.png)

```python
from microbit import *

while True:

    if temperature() >= 35:
        display.show(Image.HEART)

    else:
        display.show(Image.HEART_SMALL)
```

“Check” をクリックしてコードのエラーを確認します。下線やカーソルが表示される場合、プログラムに誤りがあります。 

![](./media/Python_709d3031.png)

コードが正しければ、micro:bit をコンピュータに接続し “Flash” をクリックしてコードを micro:bit ボードに書き込みます。

![](./media/Python_06f7542e.png)

6\.  **テスト結果2**

コードが正常にボードに書き込まれたら、**micro USB ケーブルまたは外部電源で電源を入れてください（DIP スイッチを ON にしてください）**。その後、micro:bit のリセットボタンを押します。

![Img](./media/Python_bb3e1312.png)

 周囲温度が 35℃ 未満のとき、5×5 LED ドットマトリクスは ![](./media/Python_034dc0d5.png) を表示します。温度が 35℃ 以上の場合は、パターン ![](./media/Python_ebfaeac9.png) が表示されます。

7\.  **コードの説明**

![Img](./media/Python_d7cdc397.png)

---