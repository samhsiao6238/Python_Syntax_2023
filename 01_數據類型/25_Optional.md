# Optional

_型別建構器_

<br>

## 說明

1. 在 Python 的 `typing` 模組中，`Optional[X]` 是常用的 `型別建構器`，用來指示某個變數或函式參數的型別可以是 `X` 或是 `None`。

<br>

2. 從 Python 3.10 開始，`Optional[X]` 可以更簡潔地用 `X | None` 來表示，這種 `類型標註` 表是一個變數不僅可以接受特定類型 `X`，還可以接受 `None` 作為其 `類型`，由於該類型僅有一個 `None` 值，故可視為可接受 `None` 作為其 `值`，這在處理可能沒有值的情況時非常有用。

<br>

3. 特別留意，因為 `Optional[X]` 等同於 `Union[X, None]` 或 `X | None`，所以 `Optional` 可說是 `Union` 的一個特例。

<br>

## 範例

1. **基本使用**：在下方程式碼中，`process_data` 函數接受一個類型為 `Optional[int]` 的參數 `data`，表示這個參數可以是 `int` 類型的數值或 `None`，當沒有傳入 `data` 時會使用預設值 `None`。

    ```python
    from typing import Optional

    def process_data(data: Optional[int] = None) -> None:
        if data is not None:
            print(f"Data processed: {data}")
        else:
            print("No data to process.")

    process_data() # 輸出: No data to process.
    process_data(123) # 輸出: Data processed: 123
    ```

<br>

2. **與預設參數區分**：`Optional` 代表的是 `標註類型的可選`，與 `參數有預設值` 時的 `可選參數`不是同一概念； `Optional` 是指 `Optional Type Hints`，這是 `Type Annotations` 的一個特例；而 `有預設值的參數` 是指 `可選參數 Optional Parameters`，由於參數具有預設值，所以在呼叫函數時可以不提供該參數，而參數會自動使用預設值；可知，如果函數的參數要允許明確地傳入 `None`，那麼 `可` 使用 `Optional` 來標註傳入的類型。

    ```python
    # 參數 `arg` 是可選參數的（預設值）。
    def foo(arg: int = 0) -> None:
        print(f"Arg value: {arg}")

    # `arg` 參數使用了 `Optional[int]`，明確允許傳入 `None`，且預設值為 `None`。
    def bar(arg: Optional[int] = None) -> None:
        if arg is None:
            print("Arg is None")
        else:
            print(f"Arg value: {arg}")
    
    foo() # 輸出: Arg value: 0
    bar() # 輸出: Arg is None
    ```

<br>

___

_END_