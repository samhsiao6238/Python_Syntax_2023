# tuple
_或稱 `數組`、`元組`_

<br>

## 說明

1. 不可變的 `Immutable` ；
2. 有序序列，可通過索引訪問；
3. 成員可以是不同資料類型，成員也可以是數組；
4. 因為不可變，所以 `可` 作為字典 `dict` 的鍵 `key`；
5. 因為不可變，所以 `可` 作為不可變集合 `set` 的成員；
6. 補充說，因為列表 `list` 是可變的，所以不可作為 `dict` 的鍵，也不可作為 `set` 的成員；
7. 可使用一個數組來打包一個函數同時傳出的多的回傳值。

<br>

## 初始化

- 因為不可變，所以初始化後重新指定數組的內容等同是建立新的數組；
- 可用小括號 `( )` 建立；
- 可用 `,` 相隔來建立，也稱為 `打包`，反向動作稱為 `解包` 。

<br>

1. 初始化一個空元組

    ```python
    my_tuple = ()
    print(my_tuple, type(my_tuple))
    ```
    _結果_
    ```bash
    () <class 'tuple'>
    ```

2. 使用 `,` 初始化一個元組

    ```python
    my_tuple = 1, 2, 3
    print(my_tuple, type(my_tuple))
    # id
    print(my_tuple, id(my_tuple))
    ```
    _結果_
    ```bash
    (1, 2, 3) <class 'tuple'>
    (1, 2, 3) 140401150822848
    ```

3. 重新指定數組的成員

    ```python
    my_tuple = (1, 2, 3)
    # 重新指定後的 id
    print(my_tuple, id(my_tuple))
    ```
    _結果_
    ```bash
    (1, 2, 3) 140401151079872
    ```

4. 訪問元組的成員

    ```python
    print(my_tuple[0]) # 1
    ```
    _結果_
    ```bash
    1
    ```

5. 成員可以是不同的資料型態

    ```python
    my_tuple = (1, 2, 3, 'Hello', True)
    print(my_tuple)
    ```
    _結果_
    ```bash
    (1, 2, 3, 'Hello', True)
    ```

6. 元組的成員不可以被修改

- 可透過 try-except 來捕捉錯誤

    ```python
    try:
        # 嘗試修改元組的成員
        my_tuple[0] = 100
    except TypeError as e:
        # 顯示錯誤訊息
        print(f'發生錯誤，錯誤訊息： {e}')
    ```

    *輸出結果*

    ```bash
    發生錯誤，錯誤訊息： 'tuple' object does not support item assignment
    ```

<br>

## 方法

<br>

1. 只有一個成員的數組

   - 定義一個只包含一個元素的元組
   - 需要添加逗號來防止被誤認為數學表達式(加減乘除的括號)

    ```python
    my_single_tuple = (1,)  
    print(my_single_tuple)
    ```

    *輸出結果*
    ```bash
    (1,)
    ```

<br>

2. index 索引

    ```python
    # 初始化一個元組
    my_tuple = ('AAA', 'BBB', 'CCC', 'DDD', 'EEE')
    # 輸出原本索引內容
    print(my_tuple)  # ('AAA', 'BBB', 'CCC', 'DDD', 'EEE')

    # 使用索引值
    print(my_tuple[0])  # AAA
    # 負索引值，從最後開始計算，-1 表示最後一個元素
    print(my_tuple[-1])  # EEE

    # 範圍索引，或稱切片
    print(my_tuple[1:3])  # ('BBB', 'CCC')
    # 範圍索引，從0開始，到索引2(不包含)的元素
    print(my_tuple[:2])  # ('AAA', 'BBB')
    # 範圍索引，從索引1開始，到最後一個元素
    print(my_tuple[1:])  # ('BBB', 'CCC', 'DDD', 'EEE')
    # 範圍索引，從頭到尾
    print(my_tuple[:])  # ('AAA', 'BBB', 'CCC', 'DDD', 'EEE')
    ```

    *輸出結果*
    ```bash
    ('AAA', 'BBB', 'CCC', 'DDD', 'EEE')
    AAA
    EEE
    ('BBB', 'CCC')
    ('AAA', 'BBB')
    ('BBB', 'CCC', 'DDD', 'EEE')
    ('AAA', 'BBB', 'CCC', 'DDD', 'EEE')
    ```

<br>

3. len 長度

    ```python
    # 初始化一個元組
    my_tuple = ('AAA', 'BBB', 'CCC', 'DDD', 'EEE')
    # 使用 len() 函式取得元組的長度，有傳出值
    _len = len(my_tuple)
    print(f'數組的長度是 {_len}')
    ```

    *輸出結果*

    ```bash
    數組的長度是 5
    ```

<br>

4. count 計算

- count(element): 返回元组中出现的指定元素的次数

    ```python
    my_tuple = ('AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'AAA')
    # 計算 AAA 出現的次數
    _count = my_tuple.count('AAA')
    # 輸出結果
    print(f'AAA 出現的次數 {_count}')  # AAA 出現的次數2
    ```

    *輸出結果*

    ```bash
    AAA 出現的次數 2
    ```

<br>

5. 解包（相對於打包）

    ```python
    # 初始化一個元組
    my_tuple = ('AAA', 'BBB', 'CCC', 'DDD', 'EEE')

    # 元組解包
    a, b, c, d, e = my_tuple
    print(f'a={a}, b={b}, c={c}, d={d}, e={e}')
    ```

    *輸出結果*

    ```bash
    a=AAA, b=BBB, c=CCC, d=DDD, e=EEE
    ```

<br>


6. 透過 `+` 來連接元組，透過 `*` 來重複元組。

    ```python
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    # 連接
    joined_tuple = tuple1 + tuple2
    print(joined_tuple)  # (1, 2, 3, 4, 5, 6)

    # 重複
    repeated_tuple = tuple1 * 3
    print(repeated_tuple)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)
    ```

    *輸出結果*

    ```bash
    (1, 2, 3, 4, 5, 6)
    (1, 2, 3, 1, 2, 3, 1, 2, 3)
    ```

<br>

7. `in` 和 `not in`

   可以使用 `in` 和 `not in` 關鍵字來檢查元組中是否包含特定的元素。

    ```python
    my_tuple = ('AAA', 'BBB', 'CCC', 'DDD', 'EEE')

    # 檢查是否包含
    if 'AAA' in my_tuple:
        print("AAA 存在於數組中")

    if 'ZZZ' not in my_tuple:
        print("ZZZ 不存在於數組中")
    ```

    *輸出結果*

    ```bash
    AAA 存在於數組中
    ZZZ 不存在於數組中
    ```

<br>

8. `index` 方法

    `index(element)`：返回元組中第一次出現的指定元素的索引，如果元素不存在，則會引發一個異常。

    ```python
    my_tuple = ('AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'AAA')

    # 查找元素 AAA 第一次出現的索引位置
    index_position = my_tuple.index('AAA')
    print(f'AAA 在數組中的索引位置是 {index_position}')
    ```

    *輸出結果*

    ```bash
    AAA 在數組中的索引位置是 0
    ```

<br>

9. 循環訪問元組中的所有元素

    使用 for 迴圈來迭代和訪問元組中的所有元素。

    ```python
    my_tuple = ('AAA', 'BBB', 'CCC', 'DDD', 'EEE')

    for item in my_tuple:
        print(item)
    ```

    *輸出結果*

    ```bash
    AAA
    BBB
    CCC
    DDD
    EEE
    ```

<br>

10. `enumerate`

    使用 `enumerate` 可以在迴圈中獲取元組中元素的索引和值。

    ```python
    my_tuple = ('AAA', 'BBB', 'CCC', 'DDD', 'EEE')

    for index, value in enumerate(my_tuple):
        print(f'索引 {index} 的值是 {value}')
    ```

    *輸出結果*

    ```bash
    索引 0 的值是 AAA
    索引 1 的值是 BBB
    索引 2 的值是 CCC
    索引 3 的值是 DDD
    索引 4 的值是 EEE
    ```

<br>

---

_END_
