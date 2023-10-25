# 字串

_Python 的字串是容器，與數組 tuple 一樣是不可變的變數型別_

1. 表達式

   ```python
   #
   str_1 = 'Hello_01'
   str_2 = "Hello_02"
   str_3 = '''Hello_03'''
   #
   print(str_1)
   print(str_2)
   print(str_3)
   ```

   ```bash
   Hello_01
   Hello_02
   Hello_03
   ```

<br>

2. 相加

   ```python
   str = 'Hello' + ', ' + 'World'
   print(str)
   ```

   _OUTPUT_

   ```bash
   Hello, World
   ```

<br>

3. 透過索引或稱 `下標` 取出指定位置的字元

   ```python
   str_1[2]
   ```

   ```bash
   'l'
   ```

<br>

4. 顯示一個範圍：透過 `切片` 運算 `:` 。

   ```python
   str_1[2:4]
   ```

   ```bash
   'll'
   ```

<br>

5. 顯示反轉

   ```python
   # 顯示反轉
   str_1[::-1]
   ```

   ```bash
   '10_olleH'
   ```

<br>

6. 轉換為小寫

   ```python
   str_1.lower()
   ```

   ```bash
   'hello_01'
   ```

<br>

7. 轉換為大寫

   ```python
   str_1.upper()
   ```

   _輸出_

   ```bash
   'HELLO_01'
   ```

<br>

8. 替換

   _字串本身是不可變的，透過置換後，原本的字串依舊不變，新的值要透過賦值（或稱「指定」）取得_

   ```python
   str_1 = 'Hello_01'
   s_2 = str_1.replace('l', 'x')
   print(str_1)
   print(s_2)
   ```

   _輸出_

   ```bash
   Hello_01
   Hexxo_01
   ```

<br>

9. 分割

   _跟置換相同，這並不會改變原本的內容_

   ```python
   str_1 = 'Hello_01'
   s_1 = str_1.split('_')
   print(str_1)
   print(s_1)
   ```

   _輸出_

   ```bash
   'Hello_01'
   ['Hello', '01']
   ```

<br>

10. 搜尋並傳回下標（索引）

    ```python
    str_1 = 'Hello_01'
    print(str_1.find('H'))
    print(str_1.find('0'))
    ```

    _輸出_

    ```bash
    0
    6
    ```

<br>

11. 刪除開頭與結尾的空白字串符

    ```python
    str_3 = ' Hello '
    s_3 = str_3.strip()
    print(str_3)
    print(s_3)
    ```

    _輸出：原字串不受影響，頭尾空格都還在_

    ```bash
     Hello 
    Hello
    ```


<br>

12. 串接

    - 是指使用 `指定字符` 來 `串接字串`
    - `strA.join(strB)` 以字串 `strA` 將 `strB` 連接起來成為新的字串

    ```python
    # join
    str_4 = 'Hello'
    str_5 = '_'
    # 將「_」插入「Hello」字串中
    str_5.join(str_4)
    ```

    _輸出 `str_5`_

    ```bash
    'H_e_l_l_o'
    ```

    _下面這樣舉例比較清楚_

    ```python
    # 用全形頓號將'12345'串起來
    str_4 = '、 '
    str_4_1 = str_4.join('12345')
    # 注意 str_4_1 的型態
    print(type(str_4_1))
    str_4_1
    ```

    _輸出_

    ```bash
    <class 'str'>
    '1、 2、 3、 4、 5'
    ```

    _特別注意_

    _也可以使用 `join` 串接 `list`，串接之後會 `轉型為字串`，也就是逐一取出串接為字串_

    ```python
    # 用全形頓號將['1', '2', '3', '4', '5']串起來
    str_4 = '、 '
    # 傳出字串
    str_4_2 = str_4.join(['1', '2', '3', '4', '5'])
    print(type(['1', '2', '3', '4', '5']))
    print(type(str_4_2))
    print(str_4_2)
    ```

    _輸出_

    ```bash
    <class 'list'>
    <class 'str'>

    '1、 2、 3、 4、 5'
    ```

<br>

13. 字串的長度

    ```python
    str_1 = 'H、e、l、l、o、_、0、1'
    s_1 = str_1.replace('、', '')
    print(str_1)
    print(s_1)
    # 長度
    print(len(str_1))
    print(len(s_1))
    ```

    _輸出_
    ```
    H、e、l、l、o、_、0、1
    Hello_01
    15
    8
    ```

<br>

14. 遍歷

    - 🔅 看一下 str_1 的內容

    ```python
    for i in str_1:
        print(i)
    ```

    _輸出_

    ```bash
    H
    e
    l
    l
    o
    _
    0
    1
    ```

    - 🔅 看一下 str_4_2 的內容與長度，因全形文字佔位2

    ```python
    for i in str_4_2:
        print(i)
    len(str_4_2)
    ```

    _輸出_

    ```bash
    1
    、

    2
    、

    3
    、

    4
    、

    5

    13
    ```

<br>

15. 比對字串

    - ⭕️ 透過 `+` id會相同

    ```python
    # 比對兩個字串的id是否相同
    s1 = 'hello'
    s2 = 'hello'
    # 透過「+」串接，id會相同
    s3 = 'hell' + 'o'
    print(s1, id(s1))  # 相同 ID 
    print(s2, id(s2))  # 相同 ID 
    print(s3, id(s3))  # 相同 ID 
    ```

    _🟰 結果_

    ```bash
    hello 4361139856
    hello 4361139856
    hello 4361139856
    ```

    - 🔅 透過 `join()` 串接，id會不同

    ```python
    s1 = 'hello'
    s4 = ''.join(['h', 'e', 'l', 'l', 'o'])
    print(s1, id(s1)) 
    print(s4, id(s4))  # 不同的 ID
    ```

    _結果_

    ```bash
    hello 4361139856
    hello 4366691104
    ```

    - 🔅 透過變數串接，id會不同

    ```python
    s1 = 'hello'
    s5 = 'o'
    s6 = 'hell' + s5
    print(s1, id(s1)) 
    print(s6, id(s6)) # 不同的 ID
    ```

    _結果_

    ```bash
    hello 4361139856
    hello 4366683952
    ```

    - 🔅 通過 `f-string` 格式化操作來創建字串，id會不同

    ```python
    s1 = 'hello'
    s7 = f'hell{s5}'
    print(s1, id(s1))
    print(s7, id(s7))
    ```

    _結果_

    ```bash
    hello 4361139856
    hello 4366683952
    ```

    - 🔅 字串內 `容包含特殊字符`，id 會不同

    ```python
    s10 = 'Hello!'
    s11 = 'Hello!'
    print(s10, id(s10))  # 不同的 ID
    print(s11, id(s11))  # 不同的 ID
    ```

    _結果_

    ```bash
    Hello! 4366693264
    Hello! 4366686784
    ```

<br>

16. 與 ASCII 的轉換

    ```python
    ascii_val = ord('A')  # 65
    char_from_ascii = chr(65)  # 'A'
    print(ascii_val)
    print(ascii_val)
    ```

    _OUTPUT_

    ```bash
    65
    'A'
    ```

<br>

---

_END_
