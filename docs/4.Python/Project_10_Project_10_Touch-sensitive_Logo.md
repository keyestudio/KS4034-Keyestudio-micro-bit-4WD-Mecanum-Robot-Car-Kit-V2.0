### プロジェクト10：タッチ感知ロゴ

![](./media/Python_64469585.png)

1\.  **説明**

micro:bit メインボード V2 には金色のタッチ感知ロゴが搭載されており、ボタンのような入力コンポーネントとして動作します。

これは静電容量方式のタッチセンサを内蔵しており、押された（または触れられた）ときに電界の微小な変化を検出します。スマートフォンやタブレットの画面と同様です。押すとプログラムを起動できます。

2\.  **準備**

A. USB ケーブルで micro:bit メインボードをコンピュータに接続します。

B. Mu のオフライン版を開きます。

3\.  **テストコード**

Mu ソフトウェアを起動し、ファイル “Touch-sensitive Logo\.py” を開いてコードをインポートします。編集ウィンドウに手動でコードを入力することもできます。

(**注意：すべての英語の単語と記号は英語で記述してください**。)

![](./media/Python_0c54cbe5.png)

```python
from microbit import *
time = 0
start = 0
running = False

while True:

    if button_a.was_pressed():
        running = True
        start = running_time()
    if button_b.was_pressed():
        if running:
            time += running_time() - start
        running = False
    if pin_logo.is_touched():
        if not running:
            display.scroll(int(time/1000))

    if running:
        display.show(Image.HEART)
        sleep(300)
        display.show(Image.HEART_SMALL)
        sleep(300)
    else:
        display.show(Image.ASLEEP)
```

**Micro:bit はどのように動作するのか？**

A\. 実行時間はミリ秒（ms）で記録されます。

B\. ボタン A を押すと、start という名前の変数に現在の実行時間が設定されます。

C\. ボタン B を押すと、開始時刻が新しい実行時間から差し引かれ、ストップウォッチを開始してから経過した時間が計算されます。この差分が合計時間に加算され、time という変数に保存されます。

D\. 金色のロゴを押すと、プログラムは合計経過時間を LED 表示に表示します。ミリ秒（千分の一秒）を 1000 で割ることで秒に変換します。整数の結果を得るために整数除算を使用します。

E\. プログラムは running という名前のブール変数でも制御されます。ブール変数は true または false の 2 値のみを取ります。もし "running" が "true" なら、ストップウォッチが動作中であることを意味します。もし "running" が false なら、ストップウォッチは開始されていないか停止していることを意味します。

F\. "running" が true の場合、LED ドットマトリクスに鼓動するハートのパターンが表示されます。

G\. (7) ストップウォッチが停止しており "running" が false の場合、金色のロゴを押すと時間のみが表示されます。

H\. ストップウォッチが開始され "running" が true の場合、ボタン B が押されたときに time 変数が変化することを確実にすればよく、コードは誤検出を防ぐこともできます。

コードのエラーを確認するには “Check” をクリックしてください。下線やカーソルが表示される場合、プログラムは誤りがあります。

![](./media/Python_1766a28c.png)

コードが正しければ、micro:bit をコンピュータに接続して “Flash” をクリックし、コードを micro:bit ボードに書き込みます。

![](./media/Python_a3d6e994.png)

4\.  **テスト結果**

コードをボードに正常にダウンロードしたら、**micro USB ケーブルまたは外部電源で電源を入れる（DIP スイッチを ON にする）** か、micro:bit のリセットボタンを押します。

![Img](./media/Python_bb3e1312.png)

ボタン A を押してストップウォッチを開始します。計測中は LED マトリクスに鼓動するハートのパターンが表示されます。ボタン B を押すと停止し、いつでも開始・停止が可能です。

それは実際のストップウォッチのように時間を記録し続けます。micro:bit 前面の金色ロゴを押すと、測定された時間が秒で表示されます。後部のリセットボタンを押すと時間をゼロにリセットできます。

---