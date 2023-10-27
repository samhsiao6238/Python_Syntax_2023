# assert 斷言

_斷言語句可以透過 `-O` 選項關閉全局的斷言檢查。_



<br>

## 說明

1. assert 關鍵字語句被用作一個調試輔助工具，後面跟著一個條件，可用以檢查程序中的條件，如果條件為 False，則引發一個 AssertionError 異常。

2. 特別注意，斷言 `不該` 用於應用程式正式階段的錯誤處理，所以 Python 有一個 `-O` 優化選項可以用於關閉全局的斷言檢查。
   
   ```python
    python -O example.py    # 大寫的英文字母 `O`，不是數字 `0`
    ```

3. 斷言應該用於開發和測試階段，用以檢查代碼的內部邏輯錯誤檢測。


<br>

## 範例

<br>

1. 簡單範例

    ```python
    x = 8
    try:
        assert x == 10, "The value of x is not 10"
    except AssertionError as e:
        print(e)    # The value of x is not 10
    ```


    ```python
    x = 10
    # 斷言，如果 x 等於 10，則不會顯示任合訊息
    assert x == 10, "The value of x is not 10"
    ```

<br>

2. 檢查函數的輸入：驗證函數參數是否符合預期。


    ```python
    def calculate_square_root(x):
        assert x >= 0, "Input must be non-negative"
        return x ** 0.5

    # 使用正確的輸入，不會引發 AssertionError
    print(calculate_square_root(4))  # 輸出: 2.0

    # 使用錯誤的輸入，將引發 AssertionError
    try:
        calculate_square_root(-4)
    except AssertionError as e:
        print(e)  # AssertionError: Input must be non-negative
    ```
    _OUTPUT_
    ```bash
    2.0
    Input must be non-negative
    ```

<br>

3. 檢查函數的輸出：驗證函數的返回值是否符合預期。


    ```python
    def add(x, y):
        result = x + y
        assert result >= x and result >= y, "Result is less than inputs"
        return result

    # 使用正確的輸入
    print(add(5, 7))  # 輸出: 12

    # AssertionError
    try:
        add(7, -6)
    except AssertionError as e:
        print(e)


    # TypeError
    try: 
        add("5", 7)
    except TypeError as e:
        print(e)
    ```
    _OUTPUT_
    ```bash
    12
    Result is less than inputs
    can only concatenate str (not "int") to str
    ```

<br>

4. 在代碼中的特定點檢查變數的狀態。


    ```python
    def process_data(data):
        assert isinstance(data, list), "Input data must be a list"
        # 更多處理過程...

    data = "Hello"
    # 此處將引發 AssertionError，因為輸入的數據不是列表
    try:
        process_data(data)  # AssertionError: Input data must be a list
    except AssertionError as e:
        print(e)
    ```
    _OUTPUT_
    ```bash
    Input data must be a list
    ```

<br>

---

_END_
