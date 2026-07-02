## Keyestudio 4WD Mecanum Robot Car V2.0 の組み立て

### ステップ 1

**必要な部品:**

![](./media/Assemble_Mecanum_Robot_f3d856b4.png)

**取り付け図:**

![](./media/Assemble_Mecanum_Robot_3d1dbf07.png)

**プロトタイプ:**

![](./media/Assemble_Mecanum_Robot_f5d38786.png)

### ステップ 2

**必要な部品:**

![](./media/Assemble_Mecanum_Robot_a2ee8074.png)

**取り付け図:**

![](./media/Assemble_Mecanum_Robot_6fdf9d4d.png)

**プロトタイプ:**

![](./media/Assemble_Mecanum_Robot_3fec7c19.png)

### ステップ 3

**必要な部品:**

![](./media/Assemble_Mecanum_Robot_d4f24cc5.png)

**取り付け図:**

![](./media/Assemble_Mecanum_Robot_e1d7b425.png)

**プロトタイプ:**

![](./media/Assemble_Mecanum_Robot_cc96b9d6.png)

### ステップ 4

（まずサーボの角度を調整してください）

**サーボの角度を90度に設定します。**

**方法1: MakeCode コード**

⚠️**特記事項：** コードを書いてアップロードする前に、MakeCode IDE を理解し、ライブラリファイルを追加する必要があります。次のリンクにアクセスしてください: [Get Started with makecode](./Code1.7z)

![](./media/Assemble_Mecanum_Robot_a9ff633c.png)

上記の MakeCode コードは資料に含まれています。サーボの調整用コードを開き、それを 4WD Mecanum Robot Car V2.0 の microbit 本体に書き込み、**micro USB ケーブルまたは外部電源で電源を入れてください（DIP switch を ON にしてください）**。これで完了です。コードは図に示した位置にあります：

![Img](./media/Assemble_Mecanum_Robot_21db9fa2.png)

**方法2：Python コード**

⚠️**特記事項：** コードを書いてアップロードする前に、Mu IDE をインストールし、ライブラリファイルを追加する必要があります。次のリンクにアクセスしてください: [Get Started with Python](./Code2.7z)

```Python
# import microbit related libraries
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


Servo(pin14).write_angle(90)
sleep(1000)
```

**必要な部品:**

![](./media/Assemble_Mecanum_Robot_1e3fd9e2.png)

取り付け図:（取り付け方向に注意）

![](./media/Assemble_Mecanum_Robot_9ca5d2c8.png)

**プロトタイプ:**

![](./media/Assemble_Mecanum_Robot_9b8bccaa.png)

### ステップ 5

**必要な部品:**

![](./media/Assemble_Mecanum_Robot_8d138501.png)

**取り付け図:**

![](./media/Assemble_Mecanum_Robot_bda8fbc4.png)

**プロトタイプ:**

![](./media/Assemble_Mecanum_Robot_9f244272.png)

### ステップ 6

**必要な部品:**

![](./media/Assemble_Mecanum_Robot_36259594.png)

**取り付け図:**

![](./media/Assemble_Mecanum_Robot_6d3e3ad9.png)

**プロトタイプ:**

![](./media/Assemble_Mecanum_Robot_3c33f63b.png)

### ステップ 7

**必要な部品:**

![](./media/Assemble_Mecanum_Robot_817e834e.png)

**取り付け図：**（モーターの向きに注意）

![](./media/Assemble_Mecanum_Robot_09a61aa6.png)

**プロトタイプ:**

![](./media/Assemble_Mecanum_Robot_8c97de28.png)

### ステップ 8

**必要な部品:**

![](./media/Assemble_Mecanum_Robot_43bac346.png)

**取り付け図：**（メカナムホイールの取り付け方向に注意）

![](./media/Assemble_Mecanum_Robot_d92dee68.png)

**プロトタイプ:**

![](./media/Assemble_Mecanum_Robot_64467ed0.png)

### ステップ 9

**必要な部品:**

![](./media/Assemble_Mecanum_Robot_5c38573f.png)

**取り付け図:**

![](./media/Assemble_Mecanum_Robot_a72469e3.png)

**プロトタイプ:**

![](./media/Assemble_Mecanum_Robot_243aa35b.png)

### ステップ 10

**必要な部品:**

![](./media/Assemble_Mecanum_Robot_b60b9f16.png)

**取り付け図:**

![](./media/Assemble_Mecanum_Robot_55f2db60.png)

**プロトタイプ:**

![](./media/Assemble_Mecanum_Robot_456df8a0.png)

### 配線図

**サーボの配線:**

![Img](./media/Assemble_Mecanum_Robot_c82a9395.png)

![](./media/Assemble_Mecanum_Robot_859cd41e.jpg)

![](./media/Assemble_Mecanum_Robot_b3bcce9d.png)

**超音波センサーの配線:**

![Img](./media/Assemble_Mecanum_Robot_c9f3da75.png)

![](./media/Assemble_Mecanum_Robot_5747ad7c.jpg)

![](./media/Assemble_Mecanum_Robot_a8f0e176.png)

**IR受信モジュールの配線:**

![Img](./media/Assemble_Mecanum_Robot_61d53b21.png)

![](./media/Assemble_Mecanum_Robot_1e081a3a.png)

**RGB の配線:**

![Img](./media/Assemble_Mecanum_Robot_c5b8a804.png)

![](./media/Assemble_Mecanum_Robot_01848b2e.jpg)

**モーターと7色ライトを制御する配線:**

![Img](./media/Assemble_Mecanum_Robot_0c4635c5.png)

![](./media/Assemble_Mecanum_Robot_1689f2c9.jpg)

**3チャンネルライントレースセンサーを制御する配線:**

![Img](./media/Assemble_Mecanum_Robot_542d1798.png)

![](./media/Assemble_Mecanum_Robot_08eb8d7e.jpg)

**電源の配線:**

![](./media/Assemble_Mecanum_Robot_cdcec4ba.jpg)

**モーターの対応インターフェース:**

![](./media/Assemble_Mecanum_Robot_ffcceef1.jpg)

**バッテリーの取り付け:**

![](./media/Assemble_Mecanum_Robot_fe8ce786.png)