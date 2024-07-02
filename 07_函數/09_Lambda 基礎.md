# lambda 表達式

<br>


1. 單一參數

    ```python
    # 這是一個接受一個參數，並回傳該參數加 10 的 lambda 函數
    add_ten = lambda x: x + 10
    print(add_ten(5))
    ```
    _結果_
    ```bash
    15
    ```

<br>



2. 多個參數

    ```python
    # 定義一個函式，將兩個數字相加後回傳結果
    add = lambda x, y: x + y  
    result = add(10, 20) 
    result
    ```
    _結果_
    ```bash
    30
    ```

<br>

3. 這是一個接受兩個參數，並回傳兩者相乘結果的 lambda 函數 

   - lambda 函數經常與 Python 的內置函數如 filter(), map(), 和 sorted() 等一起使用，下面範例裡的 key 參數決定了排序的方式，lambda x: x[1] 表示根據每個元素的第二個字符來排序。

    ```python
    multiply = lambda x, y: x * y
    print(multiply(3, 7))
    ```
    _結果_
    ```bash
    21
    ```

<br>

4. 用 lambda 函數將列表中的數字加倍 
    ```python
    nums = [1, 2, 3, 4, 5]
    doubled = list(map(lambda x: x * 2, nums))
    print(doubled)
    ```
    _結果_
    ```bash
    [2, 4, 6, 8, 10]
    ```

<br>

5. 用 lambda 函數過濾出列表中的偶數

    ```python
    nums = [1, 2, 3, 4, 5]
    evens = list(filter(lambda x: x % 2 == 0, nums))
    print(evens)
    ```
    _結果_
    ```bash
    [2, 4]
    ```

<br>

6. 使用 lambda 函數根據元素的第二個字符進行排序

    ```python
    words = ["apple", "banana", "cherry"]
    sorted_words = sorted(words, key=lambda x: x[1])
    print(sorted_words) 
    ```
    _結果_
    ```bash
    ['banana', 'apple', 'cherry']
    ```

<br>

7. 與 reduce() 函數一起使用
   - 這是一種常見的在列表上進行累積操作的方法。例如，可以使用 reduce() 和 lambda 函數來計算一個列表的所有元素的乘積。


    ```python
    # 
    from functools import reduce
    # 使用 lambda 函數計算列表中所有數字的乘積
    nums = [1, 2, 3, 4, 5]
    product = reduce(lambda x, y: x * y, nums)
    print(product)
    ```
    _結果_
    ```bash
    120
    ```

<br>

8. 找出列表中數字的絕對值最大的數
   - lambda 表達式也可以用在一些 Python 函數的參數中，這些函數接受一個函數作為參數。例如，max() 函數和 min() 函數可以接受一個 key 參數來決定如何比較元素，這裡，lambda x: abs(x) 函數用於計算每個數字的絕對值，並將其用於比較。


    ```python
    nums = [1, -2, 3, -4, -5]
    max_num = max(nums, key=lambda x: abs(x))
    print(max_num)
    ```
    _結果_
    ```bash
    -5
    ```

    
<br>

---

_END_

