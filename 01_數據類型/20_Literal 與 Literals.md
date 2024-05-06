# Literal

_Literal 是 Python 的 typing 模組中引入的一個類型提示工具_

<br>

## 說明

1. `Literal 類型` 和 `literals 字面量` 兩者具有本質上的不同。

2. `字面量 Literals` 是一種程式設計語言的標記法，用於直接在程式碼中表示固定值的數據，如數值字面量（123、3.14）、字串字面量（'hello'、"world"）、布林值字面量（True、False）、空值字面量（None）等，字面量是靜態的，它們在程式碼中直接被寫出，並在程式運行時被解釋為具體的值。

3. `Literal` 用於指定函數參數、變數或返回值必須是限定的 `實字常量  Literal Constants` 之一，常用於增強靜態類型檢查的精確度，並允許開發者明確指出某些函數的行為依賴於特定的數值或狀態。

4. 雖然 `Literal` 和 `literals 字面量` 都涉及到 `固定的值`，但 `Literal` 在 Python 中是用作 `類型標註` 的一部分，用以確保類型安全和程式碼的正確性，例如使用 Literal 可以確保函數參數只能是幾個預定義的字面量之一。

5. 範例。

    ```python
    from typing import Literal

    # 定義一個函數接受一個 mode 參數，該參數必須是 'debug' 或 'release' 其中之一。
    # 這樣的做法確保了函數行為的預期性和正確性，防止錯誤的值被傳入。
    def configure_system(mode: Literal['debug', 'release']) -> None:
        if mode == 'debug':
            print("System is set to debug mode.")
        else:
            print("System is set to release mode.")

    configure_system('debug')  # 正確
    configure_system('test')  # 錯誤，類型檢查將失敗
    ```

<br>

___

_END_