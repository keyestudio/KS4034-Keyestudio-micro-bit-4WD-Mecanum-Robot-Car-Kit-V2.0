## プロジェクト11：マイク

![](./media/Makecode_d2f14bdc.jpg)

[Click to download the code 1 for this lesson](./Code/Microphone.hex)

[Click to download the code 2 for this lesson](./Code/Microphone2.hex)

### (1)プロジェクトの説明：

Micro:bit main board V2 にはマイクが搭載されており、周囲の音量を検出できます。手をたたくと、マイクのLEDインジケータが点灯します。音の強さを測定できるため、騒音の尺度を作成したり、音楽に合わせて変化するディスコ風の照明を作ったりできます。マイクはマイクのLEDインジケータの反対側に配置されており、音が通るための穴の近くにあります。基板が音を検出すると、LEDインジケータが点灯します。

### (2)必要な部品：

Micro:bit main board V2

Micro USBケーブル

### (3)テストコード1：

Micro USB ケーブルでコンピュータと micro:bit ボードを接続し、MakeCode エディタでプログラムします。

![](./media/Makecode_7c037c9b.gif)

完成プログラム：

![](./media/Makecode_1ea97896.png)

### (4)テスト結果1：

コードをアップロードすると、周囲の音が検出されたときに大きなハートアイコンが表示され、周囲が静かなときには小さなハートアイコンが表示されます（注意：検出できないほど小さな音は反応を引き起こしません）。

![](./media/Makecode_facbbb50.gif)

### (5)テストコード2：

Micro USB ケーブルでコンピュータと micro:bit ボードを接続し、MakeCode エディタでプログラムします。

![](./media/Makecode_68e37f22.gif)

完成プログラム：

![](./media/Makecode_9851e889.png)

### (6)テスト結果2：

![](./media/Makecode_0b914334.gif)

コードをアップロードすると、ドットマトリクスが音の変化に同期してパルスします。「A」キーを押すと、現在の音の数値が表示されます。