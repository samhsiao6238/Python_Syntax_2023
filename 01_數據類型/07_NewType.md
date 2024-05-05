# 新型別（NewType）

_內建模組 typing 所提供的功能_

<br>

## 說明

1. `NewType` 用於創建現有類型的子類，有助於進行 _強類型檢查_。
2. 它並不創建一個新的類別，而是幫助開發者確保那些需要特別類型安全的場合不會誤用普通的資料類型。

## 範例

1. 程式碼。

    ```python
    from typing import NewType

    # 透過 `NewType` 創建名為 UserId 的新類型
    # 這個類型在運行時表現為整數 `int`，但在類型檢查階段，它被視為一個與 int 不同的獨立類型
    UserId = NewType('UserId', int)

    def get_user_name(user_id: UserId) -> str:
        # 假設這裡有實際的查詢邏輯
        return "username"

    # 正確使用
    user = get_user_name(UserId(12345))

    # 錯誤使用，會被類型檢查器識別出來
    # 因為 `12345` 是 int 而不是 UserId
    user = get_user_name(12345)
    ```

2. `NewType` 用來定義一個新的類型，這個新類型在運行時和原始類型 `int`基本相同，但在類型檢查時被視為一個獨立的類型，這有助於利用類型檢查器如 `MyPy` 來捕捉在運行時可能引起錯誤的不當類型使用。

3. 創建這種新類型可增強代碼的可讀性和安全性，例如系統中有多個使用整數作為識別碼的地方，如用戶 ID、訂單號等，使用 `int` 類型可能會導致混淆，因為這些整數在邏輯上代表不同的實體，通過創建 `UserId` 這樣的新類型，可以明確指出某個變數或函數參數應該專門用於用戶 ID，從而避免類型混淆。

<br>

___

_END_
