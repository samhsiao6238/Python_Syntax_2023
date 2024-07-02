# TypeVar 和 Generics

_TypeVar 與 Generics 泛型_

<br>

## 說明

1. 在 Python 中，TypeVar 和 Generics 是密切相關的概念，它們共同工作以提供強大的類型檢查和靈活的編碼模式，特別是在處理多種數據類型的情況下。

2. `TypeVar` 是 Python 內建模組 `typing` 提供的一種工具，用於定義 `泛型類型` 變數，這允許開發者建立靈活、可重用的函數或類，這些函數或類在類型安全的前提下可以處理多種類型的數據。

3. 使用 `TypeVar` 建立的 `泛型類型` 可以在類、函數或方法的定義中用作 `占位符`，表明該函數或類在保持類型一致性的同時，可以接受不同的數據類型。

4. `Generic` 是用 `TypeVar` 定義來建立可適用於多種數據類型的類或函數的方式，允許在類或函數中預先不指定具體的類型，而是在實例化或調用時指定具體的類型，這增加了程式碼的靈活性和重用性，同時保持了類型安全。

5. `TypeVar` 和 `Generics` 在 Python 中提供了類型抽象能力，這對於建立可重用的資料結構和函數庫特別有用，同時也便於進行靜態類型檢查。 

<br>

# 範例程式碼

1. 程式碼。

    ```python
    from typing import TypeVar, Generic, List
    
    # 定義一個 TypeVar，T 可以是任何類型
    T = TypeVar('T')

    # 定義一個泛型類 Stack，它可以接受任何類型 T 的元素
    class Stack(Generic[T]):
        def __init__(self) -> None:
            # items 是一個列表，列表中的元素類型為 T
            self.items: List[T] = []
        
        def push(self, item: T) -> None:
            # push 方法接受一個類型為 T 的元素
            self.items.append(item)
        
        def pop(self) -> T:
            return self.items.pop()

    '''現在 Stack 可以用於任何特定類型'''

    # 建立一個 int 類型的 Stack
    stack_of_int = Stack[int]()
    stack_of_int.push(1)
    stack_of_int.pop()

    # 建立一個 str 類型的 Stack
    stack_of_str = Stack[str]()
    stack_of_str.push("hello")
    stack_of_str.pop()
    ```

<br>

2. 在程式碼中，`TypeVar('T')` 建立了一個名為 `T` 的 `泛型類型`；`Stack 類` 使用 `Generic[T]` 表示它是一個泛型類，其中 T 是一個 `占位符`，代表將來某個具體的類型。

<br>

3. 當建立 `stack_of_int` 和 `stack_of_str` 的實例時，`int` 和 `str` 分別被傳遞給 `Stack`，這裡的 `T` 被具體化為 `int` 和 `str`，這允許 `Stack 類` 以類型安全的方式處理不同的數據類型，同時保證 `push` 和 `pop` 方法的參數和返回值的類型一致性。

<br>

___

_END
