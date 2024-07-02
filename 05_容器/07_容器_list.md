# List 列表

<br>

## 特性

- 可變 `mutable`

- 有序

- 成員可以是不同類型的元素

<br>

## 初始化

_Python 在初始化 `list` 提供了多種方法。_

1. 使用方括號

    ```python
    # 初始化一個空的 list
    my_list = []
    ```

2. 使用 `list()` 建構函數

    ```python
    # 使用 list() 來初始化一個空的 list
    my_list = list()
    ```

3. 初始值給予

    ```python
    # 初始化一個有初值的 list
    my_list = [1, 2, 3, 4, 5]
    ```

4. 使用串列生成式 (list comprehension)

    ```python
    # 使用串列生成式建立一個 list，每個元素是前10個整數的平方
    squares = [x**2 for x in range(10)]
    ```

5. 使用 `*` 運算子進行重複

    ```python
    # 建立一個有 10 個 0 的 list
    zeros = [0] * 10
    ```

6. 使用 `list()` 建構函數將其他可迭代的資料型態轉為 `list`

    ```python
    # 將字串轉換為 list
    char_list = list("hello")
    ```

7. 使用內建函數 `range()`

    ```python
    # 使用 range() 建立一個0到9的整數 list
    numbers = list(range(10))
    ```

<br>


## 方法


1. append 加入

   - append(element) 
   - 將一個元素(element)添加到列表的最後
  
    ```python
    # 建立空的 list
    my_list = []
    # 加入一個元素
    my_list.append("a")
    print(my_list)
    # 再加入一個元素
    my_list.append("b")
    print(my_list)
    ```
    *輸出結果*
    ```bash
    ['a']
    ['a', 'b']
    ```

<br>

2. insert 插入

   - insert(index, element)
   - 在指定位置插入一個元素

    ```python
    # 建立一個 list
    my_list = ["a", "b"]
    # 在 index = 1 的位置插入一個元素 "c"
    my_list.insert(1, "c")  
    print(my_list) # ['a', 'c', 'b']
    # 傳出的結果為 None，因為 insert() 方法沒有回傳值
    _return_value = my_list.insert(1, "d")
    print(f'觀察是否回傳值：{_return_value}') # None
    # d 還是有加入到 list 中
    print(my_list) # ['a', 'd', 'c', 'b']
    ```
    *輸出結果*
    ```bash
    ['a', 'c', 'b']
    觀察是否回傳值：None
    ['a', 'd', 'c', 'b']
    ```

<br>

3. extend 加入多個元素

   - extend(iterable) 
   - 將一個可迭代物件的所有元素添加到列表的末尾

   ```python
   # 建立空的 list
   my_list = []
   # 加入多個元素
   my_list.extend(["d", "e", "f"])
   print(my_list) # ['d', 'e', 'f']
   # 再加入多個元素
   my_list.extend(["g", "h", "i"])
   print(my_list) # ['d', 'e', 'f', 'g', 'h', 'i']
   ```
    *輸出結果*
    ```bash
    ['d', 'e', 'f']
    ['d', 'e', 'f', 'g', 'h', 'i']
    ```

<br>

4. remove 移除

   - remove(element): 移除列表中第一個出現的指定元素
   - 若有多個相同的元素，只會移除第一個出現的元素
   - 若指定的元素不存在，則會發生 ValueError

    ```python
    # 建立一個 list
    my_list = ["b", "a", "b", "c", "d", "e", "f"]
    # 移除一個元素
    my_list1 = my_list.remove("b")
    print(my_list) # ['a', 'b', 'c', 'd', 'e', 'f']

    # 使用 remove() 方法移除一個不存在的元素
    # 若指定的元素不存在，則會發生 ValueError
    # 因為會發生錯誤，所以使用 try-except 來做例外處理
    try:
        # 嘗試移除一個不存在的元素 "z"
        my_list.remove("z")
    except ValueError as e:
        # 若發生 ValueError，則會執行 except 區塊
        # 並且將錯誤訊息儲存在變數 e 中
        print(f'發生錯誤：{e}')

    # 會改變原本的 list，所以不會有回傳值
    # 嘗試移除 "b" 並且觀察回傳值
    return_value = my_list.remove("b")
    print(f'觀察是否回傳值：{return_value}') # None

    ```
    *輸出結果*
    ```bash
    ['a', 'b', 'c', 'd', 'e', 'f']
    發生錯誤：list.remove(x): x not in list
    觀察是否回傳值：None
    ```

<br>

5. pop 取出一個元素

   - pop(index): 移除並傳出列表中指定位置的元素
   - 若沒有指定位置，則會移除並傳出最後一個元素

    ```python
    # 建立一個 list
    my_list = ["a", "b", "c", "d", "e", "f"]
    # 取出一個元素，預設是最後一個元素
    my_list.pop()
    print(my_list) # ['a', 'b', 'c', 'd', 'e']
    # 取出指定位置的元素並觀察傳出值
    _element = my_list.pop(3)
    print(my_list) # ['a', 'b', 'c', 'e']
    # 取出的元素
    print(f'取出的元素是 {_element}') # d
    ```
    *輸出結果*
    ```bash
    ['a', 'b', 'c', 'd', 'e']
    ['a', 'b', 'c', 'e']
    取出的元素是 d
    ```

<br>

6. index 找出元素的位置

   - index(element): 返回列表中第一個出現的指定元素的索引

    ```python
    # 建立一個 list
    my_list = ["a", "BBB", "c", "BBB", "d", "e", "f"]
    # 找出元素的位置
    _index = my_list.index("BBB")
    print(f'第一次出現 BBB 的索引位置是 {_index}') # 1
    ```
    *輸出結果*
    ```bash
    第一次出現 BBB 的索引位置是 1
    ```

<br>

7. count 計算元素出現的次數

   - count(element): 返回列表中出現的指定元素出現的次數

    ```python
    # 建立一個 list
    my_list = ["a", "b", "c", "d", "EE", "EE", "EE"]
    # 計算元素「EE」出現的次數
    _count = my_list.count("EE")
    print(f'元素 EE 出現的次數 = {_count}') # 3
    ```
    *輸出結果*
    ```bash
    元素 EE 出現的次數 = 3
    ```

<br>

8. sort 排序
   - 沒有傳出值
   - 可以設置參數 reverse=True 來反向排序
   - 會直接改變原來的數列 my_list


    ```python
    # 建立一個沒有排序的list
    my_list = [ "b", "a", "d", "e", "c", "f"]
    # 排序，預設是由小到大，會直接改變原來的數列 my_list
    my_list.sort()
    print(my_list) # ['a', 'b', 'c', 'd', 'e', 'f']
    # 反向排序
    my_list.sort(reverse=True)
    print(my_list) # ['f', 'e', 'd', 'c', 'b', 'a']
    # 沒有傳出值
    return_value = my_list.sort()
    print(f'傳出值為 {return_value}') # None
    ```
    *輸出結果*
    ```bash
    ['a', 'b', 'c', 'd', 'e', 'f']
    ['f', 'e', 'd', 'c', 'b', 'a']
    傳出值為 None
    ```

<br>

9. reverse 反轉

   - 沒有傳出值
   - 會直接改變原來的數列 my_list

    ```python
    # 建立一個list
    my_list = ["a", "b", "c", "d", "e", "f"]
    # 反轉，會直接改變原來的數列 my_list
    my_list.reverse()
    print(my_list) # ['f', 'e', 'd', 'c', 'b', 'a']
    # 沒有傳出值
    return_value = my_list.reverse()
    print(f'傳出值為 {return_value}') # None
    ```
    *輸出結果*
    ```bash
    ['f', 'e', 'd', 'c', 'b', 'a']
    傳出值為 None
    ```

<br>

10. copy 淺複製

    - 兩個數列的內容相同，但不是同一個物件

    ```python
    # 建立一個list
    my_list = ["a", "b", "c", "d", "e", "f"]
    # 複製
    my_list_copy = my_list.copy()
    print(my_list_copy) # ['a', 'b', 'c', 'd', 'e', 'f']
    # 比較兩個 list 是否相等
    print(my_list == my_list_copy) # True
    # 比較兩個 list 是否為同一個物件
    print(my_list is my_list_copy) # False
    ```
    *輸出結果*
    ```bash
    ['a', 'b', 'c', 'd', 'e', 'f']
    True
    False
    ```

<br>

11. clear 清除

     - clear 會清除所有元素
     - 會直接改變原來的數列 my_list
     - 沒有傳出值

    ```python
    # 建立一個list
    my_list = ["a", "b", "c", "d", "e", "f"]
    # 清除
    my_list.clear()
    print(my_list)
    # 沒有傳出值
    return_value = my_list.clear()
    print(f'傳出值為 {return_value}') # None
    ```
    *輸出結果*
    ```bash
    []
    傳出值為 None
    ```

<br>

12. 負數索引

- 範例

    ```python
    # 建立一個list
    my_list = ["a", "b", "c", "d", "e", "f"]
    # 傳出最後一個元素的值
    print(my_list[-1]) # f
    # 傳出倒數第二個元素的值
    print(my_list[-2]) # e
    ```
    *輸出結果*
    ```bash
    f
    e
    ```

<br>

---

_END_
