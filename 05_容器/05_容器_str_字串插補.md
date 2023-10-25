# 字串差捕

<br>

1. 使用 f-string（在Python 3.6以上的版本可用）


    ```python
    name = "John"
    print(f"Hello, {name}!")
    ```
    ```bash
    Hello, John!
    ```

<br>

1. 使用.format()


    ```python
    name = "John"
    print("Hello, {}!".format(name))
    ```
    ```bash
    Hello, John!
    ```

<br>

3. 使用 `%`


    ```python
    name = "John"
    print("Hello, %s!" % name)
    ```
    _輸出_
    ```bash
    Hello, John!
    ```

<br>

_⚠️ 以下這部分是比較進階的用法，可以跳過_

<br>

4. `!r` 指定符

- 在 Python 的 `f-string` 格式化機制中，`!r` 指定符表示要在字串插補之前，對其調用內建的 `repr()` 函數。

- `repr()` 函數的目的是返回該物件的正式字符串表示形式 `official string representation`。這種表示形式的目標是要足夠明確，足使 Python 能夠透過該表示形式重新構造或再現該物件。

- 若物件所屬的類別中定義了 `__repr__()` 方法，`repr()` 函數便會調用該方法來取得物件的正式字符串表示。

- 這正式的字串表示的一大特質是，當提供給內建的 `eval()` 函數時，它應能在理論上重建該物件。

- 通常，開發者會確保 `__repr__()` 方法返回一個表示，該表示清晰地說明如何構造一個與當前實例相同屬性的新對象。


<br>

---

- 範例 1

    ```python
    class Example:
        def __init__(self, value):
            self.value = value

        def __repr__(self):
            return f"Example({self.value})"
    
    # 建立一個物件
    example = Example(5)

    # 使用 f-string 和 !r 語法
    print(f"The object is: {example!r}") 
    ```
    _結果_
    ```bash
    The object is: Example(5)
    ```

<br>

---

- 範例 2

    ```python
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        # 定義這個類別的 __repr__ 方法，用於提供物件的正式字符串表示形式。
        # 這個表示形式可以被 eval() 函數正確地評估，以再次創建相同的物件。
        # 這就是 __repr__ 的主要目標
        def __repr__(self):
            return f"Vector({self.x}, {self.y})"
    
    # 建立一個 Vector 物件
    v = Vector(1, 2)
    #
    v1 = repr(v)
    print(v1, id(v1))
    #
    v2 = repr(v)
    print(v2, id(v2))
    #
    v3 = eval(repr(v))
    print(v3, id(v3))
    ```
    _結果_
    ```bash
    Vector(1, 2) 140510001281456
    Vector(1, 2) 140510001280240
    Vector(1, 2) 140510000952176
    ```

<br>

---

_END-
