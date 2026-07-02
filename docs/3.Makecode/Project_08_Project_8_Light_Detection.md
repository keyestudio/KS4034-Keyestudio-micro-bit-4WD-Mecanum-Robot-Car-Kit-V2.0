## プロジェクト8: 光検出

![](./media/Makecode_14063ef9.jpg)

[Click to download the code for this lesson](./Code/Light-Detection.hex)

### (1) プロジェクトの説明:

このプロジェクトでは、Micro: Bit main board V2 の光検出機能に焦点を当てます。メインボードにはフォトレジスタが搭載されていないため、LEDドットマトリクスで実現しています。

### (2) 必要な部品:

Micro:bit main board V2

Micro USB ケーブル

### (3) テストコード:

Micro USB ケーブルでコンピュータを micro:bit board に接続し、MakeCode エディタでプログラムします、

![](./media/Makecode_38ffa3b8.gif)

完全なプログラム :

![](./media/Makecode_5b9a2acf.png)

### (4) テスト結果:

テストコードを micro:bit main board V2 にアップロードし、USB ケーブルでボードに電源を供給して "Show console Device" をクリックします。

LEDドットマトリクスを手で覆うと表示される光強度は概ね 0 になります。LEDドットマトリクスが光にさらされると、下図のように光が強くなるにつれて表示される光強度も強くなります。

![](./media/Makecode_11dd3c0b.gif)

Windows 10 ではなく Windows 7 または 8 を使用している場合、Google Chrome 経由ではデバイスを認識できないことがあります。データを読み取るには CoolTerm シリアルモニタソフトを使用する必要があります。

CoolTerm ソフトを開き、Options をクリックし、SerialPort を選択して COM port を設定し、baud rate を 115200 に設定します（テスト結果により、Micro: Bit main board V2 の USB SerialPort 通信の baud rate は 115200 です）。OK をクリックし、Connect をクリックします。CoolTerm シリアルモニタには光強度の値が表示されます。下図参照：

![](./media/Makecode_3c6eae52.gif)

---