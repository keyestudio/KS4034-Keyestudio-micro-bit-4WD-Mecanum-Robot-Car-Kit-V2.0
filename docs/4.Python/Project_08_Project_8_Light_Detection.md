### プロジェクト 8：光検出

![](./media/Python_b855274f.png)

1\.  **説明**

このプロジェクトでは、micro:bit メインボードの光検出機能に焦点を当てます。メインボードにはフォトレジスタが装備されていないため、LED dot matrix によって実現されます。

2\.  **準備**

A. USB ケーブルで micro:bit main board をコンピュータに接続します

B. Mu のオフライン版を開きます。

3\.  **テストコード**

Mu ソフトを起動し、ファイル “Detect Light Intensity by Microbit\.py” を開いてコードを読み込みます。編集ウィンドウに自分でコードを入力することもできます。

(**注: すべての英単語と記号は英語で記述する必要があります。**)

![](./media/Python_b4f06503.png)

```python
from microbit import *

while True:

    Lightintensity = display.read_light_level()

    print("Light intensity:", Lightintensity)

    sleep(100)
```
“Check” をクリックしてコードのエラーを確認します。下線やカーソルが表示される場合、プログラムは間違っています。

![](./media/Python_b41eeb0f.png)

コードが正しければ、micro:bit をコンピュータに接続し、“Flash” をクリックしてコードを micro:bit ボードにダウンロードします。

![](./media/Python_7baa2190.png)

4\.  **テスト結果**

コードがボードに正常にダウンロードされたら、**micro USB ケーブルまたは外部電源で電源を入れてください (turn the DIP switch to ON)**。“REPL” をクリックし、micro:bit のリセットボタンを押します。

![Img](./media/Python_bb3e1312.png)

すると REPL ウィンドウに光の強度の値が表示されます。下図のとおりです。

LED dot matrix を手で覆うと、表示される光の強度はほぼ 0 になります。LED dot matrix を光にさらすと、表示される光の強度は光の強さに応じて大きくなります。

![](./media/Python_778d89d6.png)

5\.  **コードの説明**

![Img](./media/Python_dcdc4536.png)

---