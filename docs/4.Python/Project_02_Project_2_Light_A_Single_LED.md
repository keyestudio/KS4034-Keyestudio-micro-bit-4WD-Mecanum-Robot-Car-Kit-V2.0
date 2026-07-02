### プロジェクト 2：単一のLEDを点灯する

![](./media/Python_b855274f.png)

1\.  **説明**

LEDドットマトリクスは、5×5の正方形に配置された25個のダイオードで構成され、行線（X）と列線（Y）の交点に配置されています。座標を設定することで25個のLEDのうち1つを制御できます。たとえば、最初の行の最初のLEDは (0,0) に位置し、最初の行の3番目のLEDは (2,0) に位置します。他も同様です。

![](./media/Python_094d5908.png)

2\.  **準備**

A. USBケーブルで micro:bit メインボードをコンピュータに接続します

B. Mu のオフライン版を起動します。

3\.  **テストコード**

Mu ソフトウェアを開き、ファイル “Single LED display\.py.” を開いてコードを読み込みます。編集ウィンドウに直接コードを入力することもできます。

(**注意: すべての英単語と記号は英語で記述してください**)

![](./media/Python_9545233e.png)

```python
from microbit import *

val1 = Image("09000:""00000:""00000:""00000:""00000:")
val2 = Image("00000:""00000:""00000:""00000:""00090:")
val3 = Image("00000:""00000:""00000:""00000:""00000:")

while True:
    display.show(val1)
    sleep(500)
    display.show(val3)
    sleep(500)
    display.show(val2)
    sleep(500)
    display.show(val3)
    sleep(500)

```

コードのエラーを確認するには “Check” をクリックしてください。下線やカーソルが表示されている場合、プログラムに誤りがあります。

![](./media/Python_d205be08.png)

コードが正しい場合は、micro:bit をコンピュータに接続して “Flash” をクリックし、コードを micro:bit ボードに書き込みます。

![](./media/Python_86dd6eea.png)

4\.  **テスト結果**

コードをボードに正常にダウンロードしたら、**micro USB ケーブルまたは外部電源で電源を入れて（DIPスイッチを ON にする）**、ボードのリセットボタンを押してください。

![Img](./media/Python_bb3e1312.png)

(1,0) のLEDが0.5秒間点灯・消灯し、(3,4) のLEDが0.5秒間点灯・消灯する動作を繰り返します。

5\.  **コードの説明**

![Img](./media/Python_c79b7922.png)

6\.  **参照**

sleep(ms) : 遅延時間

遅延の詳細については、次のリンクを参照してください: [https://microbit-micropython.readthedocs.io/en/latest/utime.html](https://microbit-micropython.readthedocs.io/en/latest/utime.html)