# Lambda 匿名函數

<br>

## 簡介

1. 在 Python 中，`lambda` 是一種 `匿名函數` 的技術，它既是一種表達式，也是 `函數` 的一種形式。

2. `lambda` 函數是一種快速定義的小型匿名函數的方法，通常以單行表達，此外，因沒有函數名稱而稱為匿名函數，可用於需要一個簡單函數的地方，並且不會在其他地方重複使用。

3. `lambda` 函數與普通函數定義不同，它是以表達式形式定義的，所以可嵌入到其他表達式中使用，例如作為函數的參數或返回值。

4. `lambda` 函數使用關鍵字 `lambda` 作為表達式的關鍵字，與一般函數使用 `def` 不同。

<br>

## 範例

1. 匿名表達。

    ```python
    # 使用關鍵字 `lambda` 定義一個匿名的函數，傳出值賦予變數 `add`
    add = lambda x, y: x + y
    print(add(2, 3))  # 輸出 5
    ```

<br>

2. 以表達式呈現。

    ```python
    # 在排序中使用 lambda 作為鍵函數，傳出值提供給參數 `key` 作為鍵列表
    sorted_pairs = sorted([(1, 2), (3, 1), (5, 0)], key=lambda x: x[1])
    print(sorted_pairs)  # 輸出 [(5, 0), (3, 1), (1, 2)]
    ```

<br>

3. 過濾列表：使用 `filter` 函數和 `lambda` 來過濾列表中的偶數。

    ```python
    # 一個整數列表
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)  # 輸出 [2, 4, 6, 8, 10]
    ```

<br>

4. 映射列表：使用 `map` 函數和 `lambda` 來將列表中的每個數字平方。

    ```python
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    print(squared_numbers)  # 輸出 [1, 4, 9, 16, 25]
    ```

<br>

5. 嵌套在其他函數中：在函數內部使用 `lambda` 作為返回值。

    ```python
    def make_incrementor(n):
        return lambda x: x + n

    increment_by_2 = make_incrementor(2)
    print(increment_by_2(5))  # 輸出 7
    ```

<br>

6. 使用 `lambda` 作為參數：在高階函數中使用 `lambda`。

    ```python
    def apply_function(func, value):
        return func(value)

    result = apply_function(lambda x: x * 2, 5)
    print(result)  # 輸出 10
    ```

<br>

7. 列表推導式中的 `lambda`：在列表推導式中使用 `lambda`。

    ```python
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    # 按照數字排序（實際已經排序），使用 lambda 作為鍵函數
    sorted_pairs = sorted(pairs, key=lambda pair: pair[0])
    print(sorted_pairs)  # 輸出 [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    ```

<br>

___

_END_