# 主題：Dict 字典

<br>

## 說明

1. 鍵值（key-value）對：由鍵（key）和值（value）對應組成，每個 key 在 dict 中是唯一的，並且要對應一個值。

2. 可變的 `mutable`。

3. 無序的，不能透過索引 `index` 或下標 `subscript` 訪問，僅可透過 `key` 訪問。

4. `key` 鍵可以是任何的不可變類型，如整數、浮點數、字串或一整個數組。


<br>

## 初始化

<br>

1. 使用大括號 `{}` 創建一個空的字典

    ```python
    empty_dict = {}
    print(empty_dict, type(empty_dict))  # {} <class 'dict'>
    ```

    _結果_
    ```bash
    {} <class 'dict'>
    ```

<br>

2. 使用大括號 `{}` 及鍵值對創建字典

    ```python
    fruit_colors = {
        'apple': 'red',
        'banana': 'yellow',
        'cherry': 'red'
    }
    print(fruit_colors)
    ```

    _結果_
    ```bash
    {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}
    ```

<br>

3. 使用內建函數 `dict()` 創建字典

    ```python
    # 從鍵值對列表創建
    animals = dict([('cat', 'meow'), ('dog', 'bark')])
    print(animals)
    
    # 使用關鍵字參數創建
    grades = dict(Alice=85, Bob=90, Charlie=88)
    print(grades)
    ```

    _結果_
    ```bash
    {'cat': 'meow', 'dog': 'bark'}
    {'Alice': 85, 'Bob': 90, 'Charlie': 88}
    ```

<br>

4. 使用 `dict.fromkeys()` 創建具有相同值的鍵值對

    ```python
    keys = ['a', 'b', 'c']
    value = 0
    new_dict = dict.fromkeys(keys, value)
    print(new_dict)
    ```

    _結果_
    ```bash
    {'a': 0, 'b': 0, 'c': 0}
    ```

<br>

5. 字典包容式 (dict comprehension) 創建

    ```python
    squares = {x: x*x for x in range(1, 6)}
    print(squares)
    ```

    _結果_
    ```bash
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    ```

<br>


## 方法

<br>

1. 新增元素

    ```python
    my_dict = {}
    my_dict['DDD'] = 'ddd'
    # 輸出
    print(f"my_dict['DDD']: {my_dict['DDD']}")
    ```
    _結果_
    ```bash
    my_dict['DDD']: ddd
    ```
    
<br>

2. 修改元素

    ```python
    my_dict['AAA'] = 'AAA'
    # 輸出
    print(f"my_dict['AAA']: {my_dict['AAA']}")
    ```
    _結果_
    ```bash
    my_dict['AAA']: AAA
    ```

<br>

3. 字典解析 (Dictionary Comprehension)

- 這是一種快速創建字典的方法
- 如果想創建一個將數字映射到其平方的字典，可以使用字典解析。


    ```python
    # 字典解析式
    # {key: value for 變數 in 迭代物件}
    square_dict = {x: x*x for x in range(1, 6)}
    print(square_dict)  # 輸出：{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    ```
    _結果_
    ```bash
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    ```

<br>

4. get 取值
 
 
   - 當不確定一個鍵是否存在於字典中時，可以使用 get 方法來取得該鍵的值。
   - 如果鍵不存在，get 方法會傳回 None 或指定的默認值，而不會發生錯誤使系統崩潰，這是一種安全的方法。


    ```python
    # 初始化字典
    data = {"AAA": "aaa", "BBB": 333}
    # 取出 address 這個 key 對應的值，預設 None 的時候返回的內容為'N/A'
    print(data.get("CCC", "N/A"))   # 'N/A'
    # 若沒有預設值，會傳出 None
    print(data.get("DDD"))   # 'None'
    # None 的資料類型就是 None Type
    print(type(data.get("DDD"))) # <class 'NoneType'>
    # 有值的話直接傳出
    print(data.get("AAA", "N/A"))      # 輸出：'aaa'
    ```
    _結果_
    ```bash
    N/A
    None
    <class 'NoneType'>
    aaa
    ```

<br>

5. setdefault 設定預設值

   - 使用 key 進行查詢，若有對應的 value 會回傳指定 key 的 value，如果該 key 不存在於字典中，則添加 key 並設定其值為默認值。


    ```python
    # 建立字典
    data = {'AAA': 'aaa', 'BBB': 777, 'CCC': 'ccc'}

    # 設定 address，並給定預設值
    data.setdefault("CCC", "N/A")
    print(data)  # 輸出：{'name': 'John', 'age': 30, 'address': 'N/A'}
    # 直接賦值
    data.setdefault("DDD", "123456789")
    print(data)
    # 沒預設值，就是 None
    data.setdefault("other")
    print(data)
    ```
    _結果_
    ```bash
    {'AAA': 'aaa', 'BBB': 777, 'CCC': 'ccc'}
    {'AAA': 'aaa', 'BBB': 777, 'CCC': 'ccc', 'DDD': '123456789'}
    {'AAA': 'aaa', 'BBB': 777, 'CCC': 'ccc', 'DDD': '123456789', 'other': None}
    ```

<br>

6. update 更新字典

   - 更新字典的值或者添加新的 key-value


    ```python
    # 建立一個字典
    data = {'AAA': 'aaa', 'BBB': 777, 'CCC': 'ccc'}
    print(data)
    # 更新 BBB 並加入 DDD
    data.update({"BBB": 999, "DDD": "USA"})
    #
    print(data)  # 輸出：{'name': 'John', 'age': 31, 'address': 'USA'}
    ```
    _結果_
    ```bash
    {'AAA': 'aaa', 'BBB': 777, 'CCC': 'ccc'}
    {'AAA': 'aaa', 'BBB': 999, 'CCC': 'ccc', 'DDD': 'USA'}
    ```

<br>

7. 遍歷字典
   
   - 使用 keys()、values() 和 items() 方法分別返回字典的鍵、值和鍵值對。

   - 回傳時輸出的「dict_keys」「dict_values」「dict_items」是 *視圖物件（view objects）* 的類型。


    ```python
    # 建立一個字典
    data = {'AAA': 'aaa', 'BBB': 777, 'CCC': 'ccc'}
    # 取出 keys
    print(type(data.keys()), data.keys())
    # 取出 values
    print(type(data.values()), data.values()) 
    # 取出 key-value
    print(type(data.items()), data.items()) 
    ```
    _結果_
    ```bash
    <class 'dict_keys'> dict_keys(['AAA', 'BBB', 'CCC'])
    <class 'dict_values'> dict_values(['aaa', 777, 'ccc'])
    <class 'dict_items'> dict_items([('AAA', 'aaa'), ('BBB', 777), ('CCC', 'ccc')])
    ```

<br>

8. dict_keys

   - 這個物件是一個包含字典所有鍵的視圖。
   - 可以用於迭代，支持成員檢查。
   - 支持集合操作，例如 union、intersection 和 difference。


    ```python
    d = {'a': 1, 'b': 2, 'c': 3}
    # 取出 keys
    keys = d.keys()
    # 輸出型態
    print(type(keys))  # <class 'dict_keys'>
    # 透過「in」做成員檢查
    print('a' in keys)  # True
    # 集合運算
    print(keys & {'b', 'c', 'd'})  # {'b', 'c'}
    ``` 
    _結果_
    ```bash
    <class 'dict_keys'>
    True
    {'b', 'c'}
    ```

<br>

9. dict_values

   - 是一個包含字典所有值的視圖物件。
   - 可以用於迭代，並且也支持成員檢查。
   - 但由於字典的值不需要是唯一的，所以不支援集合操作。


    ```python
    # 初始化字典
    d = {'a': 1, 'b': 2, 'c': 3}
    # 取出 values
    values = d.values()
    print(type(values))  # <class 'dict_values'>
    # 透過「in」做成員檢查
    print(1 in values)  # True
    ```
    _結果_
    ```bash
    <class 'dict_values'>
    True
    ```

<br>

10.  dict_items

     - 這個物件是一個包含字典所有 (鍵, 值) 對的視圖。
     - 可以用於迭代。
     - 支持成員檢查。
     - 支持集合操作。


    ```python
    # 初始化字典
    d = {'a': 1, 'b': 2, 'c': 3}
    # 讀取 items
    items = d.items()
    # 輸出型態
    print(type(items))  # <class 'dict_items'>
    # 透過「in」做成員檢查，每個 key-value 為一個 tuple
    print(('a', 1) in items)  # True
    print(('a', 2) in items)  # False
    ```
    _結果_
    ```bash
    <class 'dict_items'>
    True
    False
    ```

<br>

11.   del 刪除字典中的元素

     - del 透過「key」進行索引刪除，會刪除整個鍵值對(key-value)


    ```python
    # 字典
    data = {"name": "John", "age": 30}
    # 刪除，沒傳出值問題，因為 data["name"] 本來就是取值的運算
    del data["name"]
    # 查看
    print(data)  # 輸出：{'age': 30}
    ```
    _結果_
    ```bash
    {'age': 30}
    ```

<br>

12.  取出 pop

    - 實質取出會刪除，
    - 與 del 除語法不同外，pop 有回傳值，del 沒有。


    ```python
    # 字典
    data = {"AAA": "aaa", "BBB": 100}
    # 刪除，透過 pop+key 取出值
    _pop = data.pop("AAA")
    # 查看取出的值
    print(_pop)   # 輸出：aaa
    # 查看剩下的值
    print(data)   # 輸出：{'BBB': 100}
    ```
    _結果_
    ```bash
    aaa
    {'BBB': 100}
    ```

<br>

13.  使用 in 檢查鍵是否存在：這是檢查字典是否包含某個鍵的快速方法。


    ```python
    # 字典
    data = {"AAA": "aaa", "BBB": 'bbb'}
    # 使用 in 檢查 key 是否存在
    print("AAA" in data)  # 輸出：True
    print("CCC" in data)  # 輸出：False
    # 若要檢查某個 value 是否存在，可透過 values 取出
    print("aaa" in data.values())  # 輸出：True
    #
    _val = data.values()
    print(type(_val))
    print(_val)
    print(25 in data.values())  # 輸出：False
    ```
    _結果_
    ```bash
    True
    False
    True
    <class 'dict_values'>
    dict_values(['aaa', 'bbb'])
    False
    ```

<br>

14. 字典視圖 view 
 
    - 在 Python 中，當對一個字典調用 .values() 方法時，會得到一個 dict_values 物件。
    - 它是一個具有特殊行為的物件，不是完全獨立的數據類型。
    - 這個視圖（view）物件提供了字典值的動態視圖反映即時狀態，如果字典的內容變化，視圖物件也會即時地變化。


    ```python
    # 字典
    my_dict = {1: 'aaa', 2: 'bbb', 3: 'ccc', 4: 'ddd'}

    # (1)透過 .values 取值並轉為 list
    values = list(my_dict.values())
    # 輸出
    print(values)

    # (2)透過 .values 取值並轉為 tuple
    values = tuple(my_dict.values())
    # 輸出
    print(values)

    # (3)直接取值 values 會傳出 dict_values 物件
    val = my_dict.values()
    # 輸出
    print(type(val), ' : ', val)
    ```
    _結果_
    ```bash
    ['aaa', 'bbb', 'ccc', 'ddd']
    ('aaa', 'bbb', 'ccc', 'ddd')
    <class 'dict_values'>  :  dict_values(['aaa', 'bbb', 'ccc', 'ddd'])
    ```

<br>

15.  與 json 進行互相轉換


    ```python
    # 載入套件
    import json

    # 建立一個字典
    my_dict = {"name": "Alice", "age": 25}

    # 將字典轉換為 JSON 字串
    my_json = json.dumps(my_dict)
    print(my_json)

    # 將 JSON 字串轉換回字典
    my_dict_again = json.loads(my_json)
    print(my_dict_again)
    ```
    _結果_
    ```bash
    {"name": "Alice", "age": 25}
    {'name': 'Alice', 'age': 25}
    ```

<br>

16. update 更新


    ```python
    # 初始化字典
    my_dict = {"AAA": "aaa", "BBB": "bbb", "CCC": "ccc"}
    print(my_dict)

    # dict.update(mapping)：使用字典更新字典
    # dict.update(mapping)
    my_dict.update({"BBB": "BBB", "CCC": "CCC"})
    print(my_dict)

    # dict.update(iterable)：使用可迭代物件（如列表）內的數組逐一更新字典
    my_dict.update([("DDD", "ddd"), ("EEE", "eee")])
    print(my_dict)

    # dict.update(kwargs)：使用關鍵字參數中的key-value更新字典，可傳入多個
    my_dict.update(FFF='fff')
    print(my_dict) 

    # dict.update(mapping)：使用字典更新字典
    my_dict.update({'HHH': 'hhh', 'III': 'iii'})
    print(my_dict)

    # dict.update(**kwargs)：使用關鍵字參數中的key-value更新字典
    my_dict.update(JJJ='jjj', KKK='kkk')
    print(my_dict) 
    ```
    _結果_
    ```bash
    {'AAA': 'aaa', 'BBB': 'bbb', 'CCC': 'ccc'}
    {'AAA': 'aaa', 'BBB': 'BBB', 'CCC': 'CCC'}
    {'AAA': 'aaa', 'BBB': 'BBB', 'CCC': 'CCC', 'DDD': 'ddd', 'EEE': 'eee'}
    {'AAA': 'aaa', 'BBB': 'BBB', 'CCC': 'CCC', 'DDD': 'ddd', 'EEE': 'eee', 'FFF': 'fff'}
    {'AAA': 'aaa', 'BBB': 'BBB', 'CCC': 'CCC', 'DDD': 'ddd', 'EEE': 'eee', 'FFF': 'fff', 'HHH': 'hhh', 'III': 'iii'}
    {'AAA': 'aaa', 'BBB': 'BBB', 'CCC': 'CCC', 'DDD': 'ddd', 'EEE': 'eee', 'FFF': 'fff', 'HHH': 'hhh', 'III': 'iii', 'JJJ': 'jjj', 'KKK': 'kkk'}
    ```

<br>

---

_END_
