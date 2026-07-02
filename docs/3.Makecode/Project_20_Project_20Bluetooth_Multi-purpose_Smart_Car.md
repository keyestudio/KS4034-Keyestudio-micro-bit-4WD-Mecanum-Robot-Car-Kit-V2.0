## プロジェクト 20：Bluetooth Multi-purpose Smart Car

### プロジェクト 20.1：Read Bluetooth Data

![](./media/Makecode_55b2424d.png)

1\. **説明**

micro:bit メインボードには組み込みの Bluetooth が搭載されており、これを使って通信できます。micro:bit は Bluetooth によって制御したり、スマートフォンやコンピュータへ信号を送信したりすることもできます。この Bluetooth は他のデバイスに搭載された Bluetooth や Bluetooth アプリと通信して、他の機器を制御できます。

Android と iOS の両方に対応しています。両システム向けにそれぞれ Bluetooth アプリを用意しています。

基板上の Bluetooth とこれら 2 つのアプリの接続は似ています。本レッスンではアプリ上のすべてのキーとパターンの機能を紹介し、Bluetooth アプリでスマートカーを制御します。

2\. **準備**

- micro:bit ボードを keyestudio 4WD Mecanum Robot Car V2.0 のスロットに差し込む

- 電池を電池ホルダーに入れる

- 電源スイッチを ON に切り替える

- USB ケーブルで micro:bit をコンピュータに接続する

- Makecode の Web 版を開く

**コードを手作業でドラッグする場合は、まず Bluetooth 拡張ライブラリを追加する必要があります。右上の歯車アイコン (Settings) をクリックし、Extensions をクリックしてライブラリ選択画面に入り、「Bluetooth」拡張ライブラリをクリックしてください（存在しない場合は Bluetooth で検索してください）。下図のようになります：** 

![](./media/Makecode_4e308360.png)

Bluetooth と radio 拡張は同時に動作できないため、拡張ライブラリは互換性がありません。

そのため、次のようなプロンプトが表示されたら拡張を削除して Bluetooth を追加してください。

![](./media/Makecode_aee56e76.png)

3\. **テストコード**

![](./media/Makecode_ac5ffe1a.png)

“JavaScript” をクリックして対応する JavaScript コードを表示します：

![](./media/Makecode_24191138.png)

4\. **テスト結果**

ブロックをステップごとにドラッグする場合は、テストコード完了後に次のように設定する必要があります。

![](./media/Makecode_01b256e5.png)

![](./media/Makecode_982334c8.png)

![](./media/Makecode_09767d5e.png)

ただし、テストコードを直接インポートした場合はこの手順を省略できます。

設定後、コードを micro:bit ボードにダウンロードし、USB ケーブルを外さないでください。次にアプリをダウンロードします。

**iOS の場合：**

a\. App Store を開く；

![](./media/Makecode_27924fdb.png)

b\. **mecanum_robot** を検索し、![](./media/Makecode_962a57f9.png) をクリックして mecanum_robot の Bluetooth アプリをダウンロードする；

c\. APP をダウンロードしたら「OPEN」をクリックするか、携帯/iPad のデスクトップにある mecanum_robot アプリをクリックして APP を開きます。APP の画面にダイアログが表示されるので、ダイアログで「OK」をクリックします。

d\. まず携帯/iPad の Bluetooth をオンにし、APP 画面左上の接続ボタン（control）をクリックして Bluetooth を検索します。検索結果で "BCC micro:bit" をクリックします。数秒後に Bluetooth が接続されます。

**Android の場合：**

a\. ブラウザのスキャン機能で QR コードをスキャンして識別します

![](./media/Makecode_d9acbfab.png)

またはリンクにアクセス：[http://8.210.52.206/mecanum_robot.apk](http://8.210.52.206/mecanum_robot.apk) からダウンロードします。識別が成功したら「go to website」をクリックして mecanum_robot.apk のダウンロードページに入り、「Download」をクリックして mecanum_robot アプリをダウンロードします。

b\. 「Allow allow」をクリックしてインストール画面に進み、「install」をクリックしてアプリをインストールします。

![](./media/Makecode_638d0a4a.png)

c\. 「Open」をクリックするか、携帯のデスクトップにある mecanum_robot アプリをクリックして APP を開きます。ダイアログが表示されるので、ダイアログ内で「Allow」をクリックして携帯の Bluetooth をオンにします。APP を開く前に携帯の Bluetooth をオンにすることもできます。

![](./media/Makecode_c818fd71.png)

![](./media/Makecode_0c35f0dc.png)

d\. 右上の ![](./media/Makecode_d3f566b9.png) をクリックして Bluetooth を検索し、「connect」をクリックします。数秒後に Bluetooth がペアリングされます。

![](./media/Makecode_3d21cf87.png)

![](./media/Makecode_4a23b197.png)

CoolTerm を開き、Options をクリックして SerialPort を選択します。COM ポートとボーレート 115200 を設定します。「OK」と「Connect」をクリックします。

micro:bit ボードを向け、APP のアイコンを押すと、対応する文字が CoolTerm モニタに表示されます。

![](./media/Makecode_0ed4a53e.png)

テストにより、各アイコンの機能が以下のように得られます：

![](./media/Makecode_05c3d32b.jpg)

### プロジェクト 20.2：Multi-purpose Smart Car

![Img](./media/Makecode_ce6ec959.png)

1\. **説明**

このレッスンでは、スマートカーに多用途の機能を実行させる制御を行います。

2\. **準備**

- micro:bit ボードを keyestudio 4WD Mecanum Robot Car V2.0 のスロットに差し込む

- 電池を電池ホルダーに入れる

- 電源スイッチを ON に切り替える

- USB ケーブルで micro:bit をコンピュータに接続する

- Makecode の Web 版を開く

**手順：** 右上の歯車アイコン (Settings) をクリックし、Extensions をクリックしてライブラリ選択画面に入り、「Bluetooth」拡張ライブラリをクリックしてください（存在しない場合は Bluetooth で検索してください）、下図のようになります： 

![](./media/Makecode_4e308360.png)

Bluetooth と radio 拡張は同時に動作できないため、拡張ライブラリは互換性がありません。

そのため、次のようなプロンプトが表示されたら拡張を削除して Bluetooth を追加してください。

![](./media/Makecode_aee56e76.png)

3\. **テストコード**

コードがかなり長いため、ここには表示しません。対応するコードは以下のパスから直接参照できます。

![Img](./media/Makecode_836c42ce.png)

“JavaScript” をクリックして対応する JavaScript コードを表示します：

![](./media/Makecode_a73529d6.png)

4\. **テスト結果**

この実験は前のプロジェクトを組み合わせ、Bluetooth 経由で車を動作させます。

Makecode オンラインエディタに入り → プロジェクトing Settings → ![](./media/Makecode_bef5b734.png)、“No Pairing....” を有効にします（テストコードを直接インポートする場合はこの手順を省略できます）

コードを micro:bit ボードにダウンロードし、POWER を ON にして Bluetooth を接続すると、mecanum_robot の Bluetooth アプリで車を制御できます。

**注意：** ![](./media/Makecode_81da4f47.jpg) は速度を調整するために使用し、![](./media/Makecode_adc3be60.jpg) はドラッグのみ可能です。