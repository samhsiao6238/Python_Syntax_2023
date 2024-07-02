# 主題 range 

<br>

## 說明

1. range 是一個內建的類別，且有一個同名的內建函數 range()，可用於建立 range 物件。

2. range 的物件是一個 *不可變的* 數字序列，並常常用在迴圈中進行特定次數的迭代。

3. range 物件佔用的記憶體空間與 *range 的成員數量大小* 無關，只與 range 的起始、結束和間隔大小有關。這使得 range 對象在表示大範圍時非常高效。

<br>

## 應用與方法

1. 使用 `range()` 函數建立範圍


    ```python
    # range(stop): 產生從0（含）到stop（不含）的數字序列
    # 建立一個range物件
    r = range(5)
    print(r, type(r))  # range(0, 5) <class 'range'>

    # 轉換為列表並且輸出
    print(list(r))  # [0, 1, 2, 3, 4]

    # range(start, stop)
    # 產生從start（含）到stop（不含）的數字序列
    print(list(range(1, 6)))  # Output: [1, 2, 3, 4, 5]

    # range(start, stop, step)
    # 產生從start（含）到stop（不含）的數字序列，間隔為step
    print(list(range(1, 10, 2)))  # Output: [1, 3, 5, 7, 9]
    ```
    _結果_
    ```bash
    range(0, 5) <class 'range'>
    [0, 1, 2, 3, 4]
    [1, 2, 3, 4, 5]
    [1, 3, 5, 7, 9]
    ```

<br>

2. 長度 `len`


    ```python
    r = range(5)
    print(len(r))  # prints: 5
    ```
    _結果_
    ```bash
    5
    ```

<br>

3. 搭配使用成員運算子 `in`


    ```python
    r = range(5)
    print(3 in r)  # True
    print(5 in r)  # False
    ```
    _結果_
    ```bash
    True
    False
    ```

<br>

4. 節省資源
    

    ```python
    # 這將不會佔用大量記憶體
    big_range = range(1000000000)
    ```

<br>

5. 搭配 `for-in` 迴圈使用


    ```python
    # 使用範圍來進行5次迭代
    for i in range(5):
        print(i)

    print('------------------')
    # 使用範圍來進行5次迭代
    for i in range(1, 6):
        print(i)

    print('------------------')
    # 使用範圍來進行有間距的迭代
    count = 0
    for i in range(1, 10, 2):
        count += 1
        print(i, count)

    print('------------------')
    # 若不需要使用索引，可以使用_來取代
    count = 0
    for _ in range(1, 10, 2):
        count += 1
        print(count)
    ```
    _結果_
    ```bash
    0
    1
    2
    3
    4
    ------------------
    1
    2
    3
    4
    5
    ------------------
    1 1
    3 2
    5 3
    7 4
    9 5
    ------------------
    1
    2
    3
    4
    5
    ```

<br>


6. 使用 `range()` 進行切片操作

    ```python
    r = range(10)
    # 從索引 2 到 7 的子序列
    sublist = r[2:7]
    print(list(sublist))  # Output: [2, 3, 4, 5, 6]
    ```

    _結果_
    ```bash
    [2, 3, 4, 5, 6]
    ```

<br>

7. 使用 `range()` 反向生成序列

    ```python
    # 使用負數作為step值，從大到小生成數字序列
    reversed_range = range(10, 0, -1)
    print(list(reversed_range))  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ```

    _結果_
    ```bash
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ```

<br>

8. 使用 `range()` 與 `enumerate()` 一起取得索引與值

    ```python
    fruits = ['apple', 'banana', 'cherry']
    for index, value in enumerate(fruits, start=1):
        print(f"{index}. {value}")
    ```

    _結果_
    ```bash
    1. apple
    2. banana
    3. cherry
    ```

<br>

9. 使用 `range()` 進行等差級數的計算

    ```python
    # 計算 1 到 100 的總和
    total = sum(range(101))
    print(total)  # Output: 5050
    ```

    _結果_
    ```bash
    5050
    ```

<br>

10. 透過 `range()` 建立多維陣列

    ```python
    matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
    for row in matrix:
        print(row)
    ```

    _結果_
    ```bash
    [1, 2, 3]
    [2, 4, 6]
    [3, 6, 9]
    ```

<br>

---

_END_