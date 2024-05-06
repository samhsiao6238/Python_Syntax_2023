# Callable

<br>

## 說明

1. 在 Python 的 `collections.abc` 和 `typing` 模組中，`Callable` 是用於標註可呼叫物件的類型，如函數或具有 `__call__` 方法的類實例，這個標註可以明確指定函數的參數類型和返回值類型，以增進程式碼的可讀性和確保類型安全。

<br>

2. `Callable` 類型標註是 Python `類型提示系統` 的一部分，用於提高代碼的清晰性和安全性，並從 Python 3.10 版本起，`Callable` 支援使用 `ParamSpec` 和 `Concatenate` 進行更複雜的參數處理，這些新增功能為開發者提供了更多靈活性和精確性。

<br>

3. 在 Python 中，使用 `Callable` 進行類型標註時，必須指定一個參數列表和一個返回類型，例如，`Callable[[int], str]` 表示一個函數，它接受一個整數 `int` 為參數，返回一個字符串 `str`。

<br>

## 範例說明

1. 程式碼。

    ```python
    from collections.abc import Callable, Awaitable

    def feeder(get_next_item: Callable[[], str]) -> None:
        # 此函數接受一個無參數，返回字符串的可呼叫物件
        ...

    def async_query(on_success: Callable[[int], None],
                    on_error: Callable[[int, Exception], None]) -> None:
        # 此函數接受兩個可呼叫物件，分別在操作成功和錯誤時呼叫
        ...

    async def on_update(value: str) -> None:
        # 此為異步函數，用於更新某個值
        ...

    # 標註一個回調函數，它接受一個字符串並返回一個 Awaitable 物件
    callback: Callable[[str], Awaitable[None]] = on_update
    ```

<br>

2. 使用省略號 `...` 作為 `Callable` 的參數列表時，表示可接受任意類型和數量的參數。

    ```python
    def concat(x: str, y: str) -> str:
        return x + y

    x: Callable[..., str]
    x = str     # 正確
    x = concat  # 也正確
    ```

<br>

3. 使用 `Protocol` 定義複雜的簽名：當需要表達接受可變參數、僅限關鍵字參數或重載函數的可呼叫物件時，可以使用帶有 `__call__` 方法的 `Protocol` 類：

    ```python
    from collections.abc import Iterable
    from typing import Protocol

    class Combiner(Protocol):
        def __call__(self, *vals: bytes, maxlen: int | None = None) -> list[bytes]:
            ...

    def batch_proc(data: Iterable[bytes], cb_results: Combiner) -> bytes:
        for item in data:
            ...

    def good_cb(*vals: bytes, maxlen: int | None = None) -> list[bytes]:
        ...

    def bad_cb(*vals: bytes, maxitems: int | None) -> list[bytes]:
        ...

    batch_proc([], good_cb)  # 正確
    batch_proc([], bad_cb)   # 錯誤！第二個參數類型不兼容
    ```

<br>

___

_END_