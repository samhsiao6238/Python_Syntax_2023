# set 集合

_set 是 Python 的基本數據結構之一，用於存儲不重複的元素序列。_

<br>

## 說明

1. `成員不可重複` : 這是 set 的一個核心特點，確保其中的每個元素都是唯一的。

2. `成員必須為不可變資料類型` : 也就是可有例如 tuple 這樣的不可變數據類型成員，但不能有如 list 或 dict 這類可變數據類型的成員。

3. `set 是可變的` : 儘管 set 中的成員必須是不可變的，但 `set 本身是可以變的` 。

4. `無序` : set 的元素是無序的，因此不能像 list 或 tuple 那樣使用索引來訪問它的元素。

5. `可進行集合運算` : set 支持各種集合運算，如聯集、交集和差集。

6. `雜湊性` : 只有不可變的數據類型可以被哈希（hash）【備註 1】，這使得 set 能夠快速檢查某個元素是否存在。
   
7. 由於集合元素的 `唯一性` ，對於重複的元素，集合只會保留一個。

8. 集合本身是不可索引的。

9. 集合不會保存元素的插入順序，每次迭代集合時可能會看到不同的順序。

<br>

## 初始化

1. 初始化一個空集合 

    ```python
    my_set = set()
    ```

2. 使用大括號 {}
   
    _⚠️ 特別注意，使用大括號 {} 初始化時，如果不添加任何元素，則會建立一個空字典而不是空集合。_
  
    ```python
    # 使用大括號初始化，但不能初始化空集合，因為 {} 是用來初始化空字典的
    my_set = {1, 2, 3, 4}
    ```   

3. 從其他數據結構初始化

    ```python
    # 通過 list 初始化
    my_set_from_list = set([1, 2, 3, 3])  # 輸出：{1, 2, 3}

    # 通過 tuple 初始化
    my_set_from_tuple = set((1, 2, 3, 3))  # 輸出：{1, 2, 3}

    # 通過字串初始化
    my_set_from_string = set("hello")  # 輸出：{'h', 'e', 'l', 'o'}
    ```

<br>

## 方法

<br>

1. 添加成員 add(elem)

   - 添加時如有相同元素存在，則不做任何事情。
   - 只能添加不可變類型的數據，例如：整數、字串、元組。不能添加列表、字典或其他集合。
   - 之所以不能添加可變數據類型，因為可變數據類型的內容可以改變，如此可能影響集合成員的唯一性。

    ```python
    # 初始化
    my_set = set()
    # 添加元素
    my_set.add('AAA')
    my_set.add('BBB')
    print(my_set)

    # 重複添加元素
    my_set.add('AAA')
    my_set.add('BBB')
    my_set.add('CCC')
    my_set.add('DDD')
    my_set.add('EEE')
    # 輸出，無序
    print(my_set)
    ```
    _結果_
    ```bash
    {'AAA', 'BBB'}
    {'DDD', 'BBB', 'EEE', 'CCC', 'AAA'}
    ```

<br>

2. 移除成員 remove(elem)

    - 從集合中移除指定的元素。
    - 如果元素不存在，會拋出 KeyError。
    - 使用 discard(elem) 方法可避免前項異常，因為它不會在元素不存在時拋出異常。

    ```python
    # 初始化一個集合
    my_set = {'AAA', 'BBB', 'CCC'}
    # 移除元素
    my_set.remove('AAA')
    print(my_set) 
    # 如果元素不存在
    try:
        my_set.remove('DDD')
    except KeyError as e:
        print(f'KeyError is {e}')
    ```
    _結果_
    ```bash
    {'CCC', 'BBB'}
    KeyError is 'DDD'
    ```

<br>


3. 長度 len

   - 返回集合的元素數量。

    ```python
    # 初始化一個集合
    my_set = {'AAA', 'BBB', 'CCC'}

    # 查看集合長度
    print(len(my_set))  # Output: 3
    ```
    _結果_
    ```bash
    3
    ```

<br>


4. 成員運算子

    - 成員運算子用於檢查元素是否存在於集合中。

    ```python
    # 初始化一個集合
    my_set = {'AAA', 'BBB', 'CCC'}

    # 測試元素是否在集合中
    print('AAA' in my_set)  # Output: True
    print('DDD' in my_set)  # Output: False
    ```
    _結果_
    ```bash
    True
    False
    ```

<br>

5. discard(elem) 從集合中刪除元素

   - 從集合中移除指定的元素，如果元素不存在，則不進行任何操作，不會拋出異常。


    ```python
    # 初始化一個集合
    my_set = {'AAA', 'BBB', 'CCC'}
    #
    my_set.discard('BBB')
    print(my_set)

    #
    my_set.discard('DDD')
    print(my_set)
    ```
    *輸出結果*
    ```bash
    {'AAA', 'CCC'}
    {'AAA', 'CCC'}
    ```

<br>


6. pop() 

   - 刪除並返回集合中的一個隨機元素；
   - 如果集合沒有成員（空），則拋出 KeyError。


    ```python
    # 初始化一個集合
    my_set = {'AAA', 'BBB'}
    #
    elem = my_set.pop()
    print(elem)
    print(my_set)

    # 再取一次
    elem = my_set.pop()
    print(elem)
    print(my_set)

    # 已經空，捕捉錯誤
    try:
        my_set.pop()
    except KeyError:
        print('集合已經空了')

    ```
    *輸出結果*
    ```bash
    AAA
    {'BBB'}
    BBB
    set()
    集合已經空了
    ```

<br>


7. clear()

   - 移除集合中的所有元素。

    ```python
    # 初始化一個集合
    my_set = {'AAA', 'BBB', 'CCC'}
    #
    my_set.clear()
    print(my_set)
    ```
    _結果_
    ```bash
    set()
    ```

<br>


8. update()

   - 用於將兩個集合的所有項目添加到當前集合中。

    ```python
    # 初始化兩個集合
    set1 = {'AAA', 'BBB', 'CCC'}
    set2 = {'DDD', 'EEE'}
    #
    set1.update(set2)
    print(set1)
    ```
    _結果_
    ```bash
    {'AAA', 'BBB', 'CCC', 'DDD', 'EEE'}
    ```

<br>

9. intersection_update()

   - 用於保留只有當前集合和指定集合共同的元素。

    ```python
    # 初始化兩個集合
    set1 = {'AAA', 'BBB', 'CCC'}
    set2 = {'BBB', 'EEE'}
    #
    set1.intersection_update(set2)
    print(set1)
    ```
    _結果_
    ```bash
    {'BBB'}
    ```

<br>

10. difference_update()

   - 用於移除當前集合中存在於指定集合的所有元素。

    ```python
    # 初始化兩個集合
    set1 = {'AAA', 'BBB', 'CCC'}
    set2 = {'BBB', 'EEE'}
    #
    set1.difference_update(set2)
    print(set1)
    ```
    _結果_
    ```bash
    {'AAA', 'CCC'}
    ```

<br>

11. symmetric_difference_update()

   - 用於保留只在當前集合或指定集合中存在的元素。

    ```python
    # 初始化兩個集合
    set1 = {'AAA', 'BBB', 'CCC'}
    set2 = {'BBB', 'EEE', 'FFF'}
    #
    set1.symmetric_difference_update(set2)
    print(set1)
    ```
    _結果_
    ```bash
    {'AAA', 'CCC', 'EEE', 'FFF'}
    ```

<br>


## 集合的數學操作 

1.  union 
2.  intersection 
3.  difference

<br>

- 以下使用這個數據操作

    ```python
    # 初始化兩個集合
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    ```

<br>

1. 聯集

    ```python
    print(set1.union(set2))
    ```
    *輸出結果*
    ```bash
    {1, 2, 3, 4, 5, 6}
    ```

<br>

2. 交集
 
    ```python
    print(set1.intersection(set2))
    ```
    *輸出結果*
    ```bash
    {3, 4}
    ```

<br>

3. 差集， se1 - set2 （與 symmetric_difference 不同）

    ```python
    print(set1.difference(set2))
    print(set2.difference(set1))
    ```
    *輸出結果*
    ```bash
    {1, 2}
    {5, 6}
    ```

<br>

4. 對稱差集

    ```python
    print(set1.symmetric_difference(set2))
    ```
    *輸出結果*
    ```bash
    {1, 2, 5, 6}
    ```

<br>

5. isdisjoint()

   - 判斷兩個集合是否包含相同的元素，如果沒有返回 True，否則返回 False

    ```python
    print(set1.isdisjoint(set2))
    ```
    *輸出結果*
    ```bash
    False
    ```

<br>

6. issubset() 

   - 判斷集合的所有元素是否都包含在指定集合中，如果是則返回 True，否則返回 False
  
    ```python
    print(set1.issubset(set2))
    ```
    *輸出結果*
    ```bash
    False
    ```

<br>

7. issuperset()

   - 判斷指定集合的所有元素是否都包含在原始的集合中，如果是則返回 True，否則返回 False
  
    ```python
    print(set1.issuperset(set2)) 
    ```
    *輸出結果*
    ```bash
    False
    ```

<br>

8. ⚠️ `|` 和 `&`

   - 在 set 類型中，`|` 和 `&` 運算子被重載 `overloaded` 來表示集合的`聯集 union` 和 `交集 intersection `。

    ```python
    a = {1, 2, 3}
    b = {3, 4, 5}
    # 使用運算子
    union_result = a | b
    intersection_result = a & b
    #
    print(union_result)
    print(intersection_result)
    ```
    ```bash
    {1, 2, 3, 4, 5}
    {3}
    ```


<br>

## 關於哈希值

1. 在Python中，可以使用內置的 `hash()` 函數來取得不可變變數的哈希值。
2. 哈希值是基於物件的內容計算得出的，所以相同的內容會有相同的哈希值。
3. 在不同的 Python 運行時或版本之間，對相同內容的哈希計算可能會有所不同。

    ```python
    # 整數的哈希值就是整數本身，無論在快取範圍內外
    hash_value_int = hash(123)
    print(hash_value_int)

    # 取得字串的哈希值
    hash_value_str = hash("hello")
    print(hash_value_str)

    # 取得元組的哈希值
    hash_value_tuple = hash((1, 2, 3))
    print(hash_value_tuple)

    # 可變變數不能取得它的哈希值
    # 強取將引發TypeError
    try:
        hash_value_list = hash([1, 2, 3])
    except TypeError as e:
        print(f"TypeError is {e}")
    ```
    _OUTPUT_
    ```bash
    123
    8871333279202546856
    529344067295497451
    TypeError is unhashable type: 'list'
    ```


<br>

---

_END_
