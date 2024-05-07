# Union

_typing.Union_

<br>

## 說明

1. 在 Python 的 `typing` 模組中，`Union` 類型是一種非常有用的工具，它用於指定一個變數可能屬於多種類型中的一種。

<br>

2. 從 Python 3.10 版本開始，引入了更簡潔的語法 `X | Y` 來表示 `Union[X, Y]`，這使得類型聲明更加直觀和易於閱讀；特別注意，雖然可以使用多個 `|` 語法來連接兩個以上的類型，但在複雜的表達式中，使用 `Union` 可能更加清晰。

    ```python
    '''定義一個接受三種類型之一個函數'''
    # 使用 `|`
    def process_data(data: int | str | float) -> float | str:
        return str(data)

    # 使用 `Union`
    def process_data(data: Union[int, str, float]) -> float | str:
        return str(data)
    ```

<br>

3. 舉例說，`Union[X, Y]` 表示一個類型可以是 `X` 或 `Y`，這是一種 `類型註解`，用於 _標註變數或函數參數、傳回值可以接受多種類型之一_。

<br>

4. 在使用限制上，不能對 `Union` 進行子類別化或實例化。 

<br>

## 特性

1. **巢狀結構扁平化**：`Union` 中的巢狀 `Union` 會被扁平化，例如 `Union[Union[int, str], float]` 等效於 `Union[int, str, float]`。

2. **單一參數簡化**：只包含單一類型的 `Union` 會簡化為該類型本身，例如 `Union[int]` 直接簡化為 `int`。

3. **重複參數省略**：在 `Union` 中重複的類型會被省略，例如 `Union[int, str, int]` 會簡化為 `Union[int, str]` 或 `int | str`。

4. **無視參數順序**：比較 `Union` 類型時，參數的順序被忽略，因此 `Union[int, str]` 等同於 `Union[str, int]`。

<br>

## 應用範例

1. 程式碼。

    ```python
    from typing import Union

    # 使用 Union 標註傳入參數與傳出值
    def process_input(value: Union[int, str]) -> Union[float, str]:
        # 檢查 value 是否為 int 類型
        if isinstance(value, int):
            # 如果是 int，則將其轉換為 float 並返回
            return float(value)
        # 如果不是 int，則返回一個字串 "Not a number"
        return "Not a number"

    # 使用 Python 3.10+ 推薦的簡寫方式
    def process_input_shorthand(value: int | str) -> float | str:
        # 檢查 value 是否為 int 類型
        if isinstance(value, int):
            # 如果是 int，則將其轉換為 float 並返回
            return float(value)
            # 如果不是 int，則返回一個字串 "Not a number"
        return "Not a number"

    # 呼叫函數
    print(process_input(10)) # 回傳 10.0
    print(process_input("hello")) # 回傳 "Not a number"
    ```

<br>

___

_END_