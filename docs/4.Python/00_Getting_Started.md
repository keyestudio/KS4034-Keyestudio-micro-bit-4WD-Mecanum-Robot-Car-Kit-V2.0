## Resource Download

この製品に関連するコード、ライブラリ、その他サポートファイルを迅速に入手できるよう、以下のリンクをクリックしてダウンロードしてください:

- [Python Code and library downloads](./PythonCode.7z)

## Pythonのはじめ方

このチュートリアルはPython言語向けに記載されています。グラフィカルなコードプログラミングを使用したい場合は、マニュアル「Makecode Tutorial」を参照してください。ダウンロードしたリソースのルートディレクトリには「Python tutorial」というフォルダがあり、Micro:bit 4WD Mecanum Robot Car V2.0のすべてのPythonコードが格納されています。Pythonコードファイルは拡張子が ".py" のファイルです。

### MicroPythonとは？

Pythonはテキストベースの言語で、教育分野で広く使用されており、データサイエンスや機械学習などの分野でもプロのプログラマーに使用されています。

Micro: bitはPythonでプログラム可能なマイコンですが、ハードウェアの違いによりmicro: bitがPythonを完全にはサポートできません。MicroPythonはmicro：bit専用で、Python3の効率的な実装です。Python標準ライブラリの一部を含み、micro:bitマイクロコントローラ上で動作するよう最適化されています。

BBC micro: bitで使用されているPythonのバージョンはMicroPythonと呼ばれます。MicroPythonはプログラミングをもっと学びたい人に最適で、一連のコードスニペットや各種のプリセットグラフィックス、音楽でプログラミングを助けます。

BBC microbit MicroPyth のリンク：[BBC micro:bit MicroPython ](https://microbit-micropython.readthedocs.io/en/latest/tutorials/introduction.html) 

**Pythonには2種類のエディタがあります：ウェブ版とオフライン版**

1\.  ウェブ版： [https://python.microbit.org/v/1.1](https://python.microbit.org/v/1.1)

![](./media/Python_693f76f5.png)

2\.  もう一つはオフラインコンパイラの Mu です ![](./media/Python_153c77ed.png)

Mu公式サイト：[https://codewith.mu/](https://codewith.mu/)

### Mu

Mu は初心者に適したPythonコードエディタです。32ビット版のWindowsはサポートしていません。

1\.  **Muをダウンロードする**

「This PC」をクリックし、右クリックして「プロパティ」を選択し、コンピュータのバージョンを確認します。

![](./media/Python_3a58be54.png)

コンピュータのシステムの種類を確認します。

![](./media/Python_e774ae15.png)

MUのリンクにアクセスしてください: [https://codewith.mu/en/download](https://codewith.mu/en/download) そして対応するバージョンのMuをダウンロードします。

![](./media/Python_ceb4cfa6.png)

2\.  **セットアップを実行**

以下のファイルを開きます

![](./media/Python_8bcfe24c.png)

Mac OSX: [https://codewith.mu/en/howto/1.1/install_macos](https://codewith.mu/en/howto/1.1/install_macos).

Linux: [https://codewith.mu/en/howto/1.2/install_linux](https://codewith.mu/en/howto/1.2/install_linux).

**Windows 10**

ポップアップが表示されたら「More info」をクリックします。

![](./media/Python_877beb7b.png)

次に「Run anyway」をクリックします。

![](./media/Python_c87475e5.png)

3\. ライセンス契約

「Install」をクリックします。

![](./media/Python_33f42b66.png)

![](./media/Python_f5c6698f.png)

インストール後、「finish」をクリックします。

![](./media/Python_c6ec7436.png)

4\. Muを起動する

次に、以下の画像のように探します

![](./media/Python_c4adbdd1.png)

メインインターフェースは次のように表示されます：

![](./media/Python_3697c0c7.png)

### モードとメニューバーの使い方

“<span style="color: rgb(255, 76, 65);">**Mode**</span>” を BBC micro:bit に設定します。

メニューで「**Mode**」をクリックして「**BBC micro：bit**」に設定します。micro:bitモードはmicro:bitとのやり取りや接続方法を理解します。

![](./media/Python_18512c7e.png)

[Start with Mu](https://codewith.mu/en/tutorials/1.1/start) をクリックしてください。

### MuがライブラリをMicro:bitにインポートする方法

<span style="color: rgb(255, 76, 65);">**ライブラリをインポートする前に、.pyコード（空のコードでも可）をmicro:bitボードにアップロードする必要があります。ここでは空のコードを例にします。**</span>

USBケーブルでボードをコンピュータに接続します。Muを開き、「Flash」をクリックして .py コード（空でも可）をボードにアップロードします。

![Img](./media/Python_611b2c4e.png)

このチュートリアルでは "keyes_mecanum_Car_V2.py" ライブラリファイルを使用します。したがって、"keyes_mecanum_Car_V2.py" ライブラリファイルをmicro:bitにインポートしてください。このファイルには Micro:bit 4WD Mecanum Robot Car V2.0 の制御方法が含まれています。

Muがファイルを保存するデフォルトのディレクトリは、ユーザーのディレクトリのルートにある “mu_code” です。

参照リンク: [https://codewith.mu/en/tutorials/1.0/files](https://codewith.mu/en/tutorials/1.0/files)

**"mu_code" フォルダを見つける方法：**

**方法1：**

例えば、WindowsシステムでシステムがコンピュータのCドライブにインストールされており、ユーザー名が "**Administrator**" の場合、"**mu_code**" ディレクトリのパスは "**C:\Users\Administrator\mu_ code**" です。Linuxシステムでは "mu_code" ディレクトリのパスは "**~/home/mu_code**" です。

「**mu_code**」フォルダを開きます。

![](./media/Python_d271a924.png)

**方法2：**

ディスク (C:) で「mu_code」フォルダを検索します。

![Img](./media/Python_03ff037e.png)

![Img](./media/Python_54199d45.png)

「mu_code」を開きます。

![Img](./media/Python_4841ca3f.png)

当社が提供するライブラリファイル “keyes_mecanum_Car.py” が保存されているデータフォルダのパスは次のとおりです：

![Img](./media/Python_7adb2b68.png)

“keyes_mecanum_Car.py” ライブラリファイルを “mu_code” フォルダにコピーします。コピーが完了すると、下図のようになります：

![](./media/Python_d753d652.png)

まずMuソフトウェアを開き、micro:bitをコンピュータに接続します。次に「Files」ボタンをクリックし、ライブラリファイル "keyes_mecanum_Car.py" をmicro:bitにドラッグします。

![](./media/Python_aeaae2b7.png)

数秒後、インポートが完了し、左のボックスに表示されます。

![](./media/Python_2be967ca.png)