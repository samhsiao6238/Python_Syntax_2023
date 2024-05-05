# Annotating callable objects

_`Callable` 類型標註是 Python 靜態類型檢查系統的一個強大工具，尤其適用於構建複雜的應用程序和庫。_

<br>

## 說明

1. 在 Python 中，`Annotating callable objects` 涉及到使用 `typing.Callable` 或 `collections.abc.Callable` 來標註那些 `可調用對象`，所謂的可調用對象包含了函數、方法、或任何實現了 `__call__` 方法的類實例。

<br>

2. 標註可調用對象使得開發者能夠明確指定函數或其他可調用對象的參數類型和返回類型，從而增強靜態類型檢查的效果和代碼的可讀性，這在設計 API 和高階函數時尤其有用，因為它允許開發者對函數的行為進行更準確的描述和預期。

<br>

## 範例

1. **基本的可調用對象標註**：在這個例子中，`process_data` 接受一個參數 `func`，這是一個從整數到字符串的可調用對象。

    ```python
    from typing import Callable

    def process_data(func: Callable[[int], str]) -> None:
        result = func(10)  # 假設這個函數將整數轉換為字符串
        print(result)

    def number_to_str(n: int) -> str:
        return str(n)

    process_data(number_to_str)
    ```

<br>

2. **使用可變參數和關鍵字參數的 Protocol**：這裡，`Combiner` 定義了一個 Protocol，它期望一個接受多個字符串並返回一個字符串的函數。`concat_elements` 是一個符合這個協定的函數。

    ```python
    from typing import Protocol, runtime_checkable

    @runtime_checkable
    class Combiner(Protocol):
        def __call__(self, *args: str, delimiter: str = ' ') -> str:
            ...

    def concat_elements(*args: str, delimiter: str = ' ') -> str:
        return delimiter.join(args)

    def use_combiner(combiner: Combiner) -> None:
        print(combiner('Hello', 'World', delimiter='-'))

    use_combiner(concat_elements)
    ```

<br>

## ParamSpec 和 Concatenate 的使用

1. 從 Python 3.10 開始，`Callable` 獲得了對 `ParamSpec` 和 `Concatenate` 的支持，這讓 `Callable` 可以精確地表達出參數之間的依賴關係。

<br>

2. 在以下範例中，`wrapper` 函數接受一個可調用對象 `func`，其第一個參數是固定的 `int`，後面跟隨由 `ParamSpec` 定義的任意額外參數，`wrapper` 返回一個新的函數，該函數使用提供的參數調用 `func`。

<br>

3. 程式碼。

    ```python
    from typing import Callable, ParamSpec, Concatenate
    from collections.abc import Awaitable

    P = ParamSpec('P')

    def wrapper(func: Callable[Concatenate[int, P], Awaitable[None]]) -> Callable[P, None]:
        async def inner(*args: P.args, **kwargs: P.kwargs) -> None:
            await func(42, *args, **kwargs)
        return inner

    async def async_func(num: int, msg: str) -> None:
        print(f"Number: {num}, Message: {msg}")

    # Apply wrapper
    sync_func = wrapper(async_func)
    sync_func("Hello")
    ```

<br>

___

_END_