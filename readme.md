
## 安裝與環境設置

1. 確保已安裝 [Python 3.10](https://www.python.org/downloads/release/python-3100/) 或更高版本。
2. 安裝 [Pipenv](https://pipenv.pypa.io/en/latest/):

    ```sh
    pip install pipenv
    ```

3. 使用 Pipenv 安裝依賴：

    ```sh
    pipenv install
    ```

## 執行程式

1. 啟動虛擬環境：

    ```sh
    pipenv shell
    ```

2. 執行程式：

    ```sh
    python BezierCurve.py
    ```

## 主要功能

- 繪製貝茲曲線
- 拖動錨點以控制曲線形狀

## 參考

- [Pygame](https://www.pygame.org/docs/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)

## 代碼結構

- `BezierCurve.py`: 主程式文件，包含 `BezierCurve` 類別及其方法。

## 方法與屬性

### BezierCurve 類別

`BezierCurve` 類別用於表示和操作貝茲曲線。貝茲曲線是一種參數曲線，廣泛應用於計算機圖形學和動畫中。這些曲線由一組控制點定義，曲線的形狀由這些控制點決定。

#### 主要功能

- **初始化**: 可以使用一組控制點來初始化貝茲曲線。
- **計算點**: 可以計算曲線上任意參數位置的點。
- **繪製曲線**: 可以將曲線繪製出來，通常用於可視化。

#### 主要方法

- `__init__(self, control_points)`: 初始化方法，接受一組控制點作為參數。
- `calculate_bezier_curve(self)`: 計算曲線上參數 `t` 對應的點，`t` 的範圍通常是 [0, 1]。
- `draw_curve(self)`: 繪製貝茲曲線的方法，可能會使用一些圖形庫來實現。



## 貢獻

歡迎提交問題和請求，或進行代碼貢獻。
