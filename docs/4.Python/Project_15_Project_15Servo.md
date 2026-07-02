### プロジェクト 15：Servo

![](./media/Python_c4b5e57b.png)

1\.  **説明**

DIYスマートカーには通常、自動障害物回避機能が含まれています。作成プロセスでは、超音波モジュールを左右に回転させるためのサーボが必要で、その後、車と障害物との距離を検出して車を障害物から回避させます。

他のマイコンでサーボの回転を制御する場合は、サーボ角を制御するために一定の周波数とパルス幅を設定する必要があります。しかし micro:bit メインボードを使用してサーボ角を制御する場合、開発環境で制御角を設定するだけで、対応するパルスが自動的に設定されてサーボの回転が制御されます。本プロジェクトでは、サーボを 0° から 90° の間で往復させる方法を学びます。

サーボモーターは位置制御の回転アクチュエータで、主にハウジング、回路基板、コアレスモーター、ギア、位置センサーで構成されます。動作原理は、サーボが MCU または受信機から送られる信号を受け取り、周期 20ms 幅 1.5ms の基準信号を生成し、取得した直流バイアス電圧をポテンショメータの電圧と比較して差分電圧を出力することです。

本プロジェクトで使用するサーボでは、茶色がGND、赤がVCC、オレンジが信号線です。

![](./media/Python_69be9581.png)

2\.  **サーボの情報**

サーボモーターの回転角は、PWM（パルス幅変調）信号のデューティ比を調整することで制御されます。PWM信号の標準周期は 20ms（50Hz）です。理論的には幅は 1ms〜2ms の範囲ですが、実際には 0.5ms〜2.5ms の範囲です。幅は 0° から 180° までの回転角に対応します。ただし、ブランドにより同じ信号でも回転角が異なる場合がある点に注意してください。

![](./media/Python_0982cb7b.png)

測定の結果、本サーボのパルス範囲は 0.65ms〜2.5ms でした。180度サーボに対する対応関係は以下の通りです。


|Time on High Level|Angle of the Servo|Reference Signal Cycle Time（20ms）|
|-|-|-|
|0.65ms|0 degree|0.65ms high level+19.35ms low level|
|1.5ms|90 degrees|1.5ms high level+18.5ms low level|
|2.5ms|180degrees|2.5ms high level+17.5ms low level|


3\.  **仕様**

- 動作電圧: DC 4.8V ~ 6V

- 動作角度範囲: 約 180 ° (500 → 2500 μsec 時)

- 寸法: 22.9\*12.2\*30mm

- パルス幅範囲: 500 → 2500 μsec

- 無負荷速度: 0.12 ± 0.01 秒 / 60 (DC 4.8V), 0.1 ± 0.01 秒 / 60 (DC 6V)

- 無負荷電流: 200 ± 20mA (DC 4.8V), 220 ± 20mA (DC 6V)

- 停止トルク: 1.3 ± 0.01kg · cm (DC 4.8V), 1.5 ± 0.1kg · cm (DC 6V)

- ストール電流: ≦ 850mA (DC 4.8V) ≦ 1000mA (DC 6V)

- 待機電流: 3 ± 1mA (DC 4.8V), 4 ± 1mA (DC 6V)

- 重量: 9±1g (サーボホーン除く)

- 動作温度: -30℃~60℃

**注意: コンピュータの電源を使用しないでください。電流要求が 500mA を超えるとサーボが焼損する恐れがあります。外部バッテリーでの給電を推奨します。**

4\.  **準備**

- micro:bit ボードを keyestudio 4WD Mecanum Robot Car V2.0 のスロットに差し込む

- 電池を電池ホルダーに入れる

- 電源スイッチを ON にする

- USB ケーブルで micro:bit をコンピュータに接続する

- オフライン版 Mu を起動する。

5\.  **テストコード**

Mu ソフトウェアを開き、ファイル “Servo\.py” を開いてコードを読み込みます。エディタウィンドウに自分でコードを入力することもできます。

(**注意: すべての英単語および記号は英語で記述してください**.)

“Check” をクリックしてコードのエラーを確認します。下線やカーソルが表示される場合はプログラムに誤りがあります。

コードが正しければ、micro:bit をコンピュータに接続し “Flash” をクリックしてコードを micro:bit ボードに書き込みます。

![](./media/Python_eecf365e.png)

```python
from microbit import *

class Servo:
    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.analog_period = 0
        self.pin = pin
        analog_period = round((1/self.freq) * 1000)  # hertz to miliseconds
        self.pin.set_analog_period(analog_period)

    def write_us(self, us):
        us = min(self.max_us, max(self.min_us, us))
        duty = round(us * 1024 * self.freq // 1000000)
        self.pin.write_analog(duty)
        sleep(100)
        self.pin.write_analog(0)

    def write_angle(self, degrees=None):
        if degrees is None:
            degrees = math.degrees(radians)
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.write_us(us)

Servo(pin14).write_angle(0)
display.show(Image.HAPPY)

while True:
        Servo(pin14).write_angle(0)
        sleep(1000)
        Servo(pin14).write_angle(45)
        sleep(1000)
        Servo(pin14).write_angle(90)
        sleep(1000)
        Servo(pin14).write_angle(135)
        sleep(1000)
        Servo(pin14).write_angle(180)
        sleep(1000)

```

4\.  **テスト結果**

コードをボードに正常に書き込んだ後、**外部電源を投入（DIPスイッチを ON に）**し、micro:bit のリセットボタンを押します。

![Img](./media/Python_bb3e1312.png)

LEDドットマトリクスはスマイリーモチーフを表示し、サーボは 0°~45°~90°~135°~180°~0° のパターンで回転します。

---