# Concatenate

_標註高階函數_

<br>

## 說明

1. 在 Python 中，`typing.Concatenate` 是 `typing` 模組的一個特殊形式，專門用於 `標註高階函數`，即那些接受一個或多個函數作為參數或傳回一個函數的函數。

2. 使用 `Concatenate` 使得在複雜的高階函數中能夠精確控制類型安全，確保在函數呼叫鏈中傳遞正確的參數類型。此外，它增強了程式碼的可讀性和維護性，使得開發者能夠透過類型註解更清楚地理解函數的行為和預期的呼叫方式。

3. `Concatenate` 通常與 `Callable` 和 `ParamSpec` 結合使用，以描述一個 `高階可呼叫物件`，該物件可以新增、移除或轉換另一個可呼叫物件的參數，這在創建如 `函數裝飾器` 等複雜功能時尤其有用。

4. `Concatenate` 被用來在 `Callable` 類型註解中精確地表達參數列表的變化，它必須作為 `Callable` 的第一個參數使用，並且 `Concatenate` 的最後一個參數必須是一個 `ParamSpec` 或省略號 `...`。

5. `Concatenate` 從 3.10 版本開始加入 Python 類型系統，提供了更強大的 `靜態類型檢查能力`。

<br>

## 範例解釋

1. 以下範例展示如何使用 `Concatenate` 來標註一個裝飾器 `with_lock`，該裝飾器向被裝飾的函數提供了一個 `threading.Lock` 物件，並保證了函數在多執行緒環境下的執行緒安全性。

    ```python
    from collections.abc import Callable
    from threading import Lock
    from typing import Concatenate, ParamSpec, TypeVar

    # 定義 ParamSpec 和 TypeVar
    P = ParamSpec('P')
    R = TypeVar('R')

    # 使用 Lock 確保任一時間只有一個執行緒執行函數
    my_lock = Lock()

    def with_lock(f: Callable[Concatenate[Lock, P], R]) -> Callable[P, R]:
        '''一個類型安全的裝飾器，提供一個鎖。 '''
        def inner(*args: P.args, **kwargs: P.kwargs) -> R:
            # 為被呼叫函數的第一個參數提供鎖
            return f(my_lock, *args, **kwargs)
        return inner

    @with_lock
    def sum_threadsafe(lock: Lock, numbers: list[float]) -> float:
        '''以執行緒安全的方式將一組數字相加。 '''
        with lock:
            return sum(numbers)

    # 呼叫裝飾後的函數時，無需手動傳遞鎖
    result = sum_threadsafe([1.1, 2.2, 3.3])
    ```

<br>

2. **裝飾器 `with_lock`** 接受一個函數 `f` 作為參數，該函數預期將 `Lock` 作為第一個參數，後面跟著由 `ParamSpec P` 捕獲的其他任意參數，裝飾器內部的 `inner` 函數負責在呼叫 `f` 時自動插入鎖定物件 `my_lock`。

<br>

3. `sum_threadsafe` 函數透過裝飾器 `with_lock` 被自動注入一個 `Lock` 實例，因此它的定義中包含一個 `lock` 參數，該參數在函數呼叫時由裝飾器自動提供。

<br>

___

_END_