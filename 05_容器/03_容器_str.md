# 字串

*Python 的字串是容器，與數組 tuple 一樣是不可改變的變數型別*

## 1. 表達

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

```
    Hello_01
    Hello_02
    Hello_03
```

## 2. 相加

```python
str = 'Hello' + ', ' + 'World'
print(str)
```

    Hello, World

## 3. 透過索引或稱「下標」取出指定位置的字元

```python
str_1[2]
```

```
    'l'
```

## 4-1. 顯示一個範圍

```python
str_1[2:4]
```

```
    'll'
```

## 4-2. 顯示反轉

```python
# 顯示反轉
str_1[::-1]
```

```
    '10_olleH'
```

## 5-1. 轉換為小寫

```python
str_1.lower()
```

```
    'hello_01'
```

## 5-2. 轉換為大寫

```python
str_1.upper()
```

```
    'HELLO_01'
```

## 6. 替換

   字串本身是不可變的，透過置換後，原本的字串依舊不變，新的值要透過賦值（或稱「指定」）取得

```python
str_1.replace('l', 'L')
```

```
    'HeLLo_01'
```

## 7. 分割

*跟置換相同，這並不會改變原本的內容*

```python
str_1.split('_')
```

```
    ['Hello', '01']
```

```python
str_1
```

```
    'Hello_01'
```

## 8. 搜尋並傳回下標（索引）

```python
str_1.find('0')
```

```
    6
```

## 9. 刪除開頭與結尾的空白字串符

```python
str_1.strip()
```

```
    'Hello_01'
```

## 10. 串接(是指「使用指定字符串接字串」)

- strA.join(strB) 以字串 strA 將 strB 連接起來成為新的字串

```python
# join
str_4 = 'Hello'
str_5 = '_'
# 將「_」插入「Hello」字串中
str_5.join(str_4)
```

```
    'H_e_l_l_o'
```

*下面這樣舉例比較清楚*

```python
# 用全形頓號將'12345'串起來
str_4 = '、 '
str_4_1 = str_4.join('12345')
# 注意 str_4_1 的型態
print(type(str_4_1))
str_4_1
```

```
    <class 'str'

    '1、 2、 3、 4、 5'
```

*特別注意*

*也可以使用「join」串接 list，串接之後會轉型為字串，也就是逐一取出串接為字串*

```python
# 用全形頓號將['1', '2', '3', '4', '5']串起來
str_4 = '、 '
# 傳出字串
str_4_2 = str_4.join(['1', '2', '3', '4', '5'])
print(type(['1', '2', '3', '4', '5']))
print(type(str_4_2))
str_4_2
```

```
    <class 'list'
    <class 'str'

    '1、 2、 3、 4、 5'
```

## 11. 字串的長度

```python
str_1.replace('、', '')
print(str_1)
# 長度
len(str_1)
```

```
    Hello_01

    8
```

## 12. 遍歷

- 看一下 str_1 的內容

```python
for i in str_1:
    print(i)
```

```
    H
    e
    l
    l
    o
    _
    0
    1
```

- 看一下 str_4_2 的內容與長度，因全形文字佔位2

```python
for i in str_4_2:
    print(i)
len(str_4_2)
```

```
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

## 13. 比對字串

```python
# 比對兩個字串的id是否相同
s1 = 'hello'
s2 = 'hello'
print(s1, id(s1))  # 相同 ID 
print(s2, id(s2))  # 相同 ID 
# 透過「+」串接，id會相同
s3 = 'hell' + 'o'
print(s3, id(s3))  # 假設輸出 140240571615392
# 透過 join() 串接，id會不同
s4 = ''.join(['h', 'e', 'l', 'l', 'o'])
print(s4, id(s4))  # 不同的 ID
# 透過變數串接，id會不同
s5 = 'o'
s6 = 'hell' + s5
print(s6, id(s6))  # 不同的 ID
# 通過f-string格式化操作來創建字串，id會不同
s7 = f'hell{s5}'
print(s7, id(s7))  # 不同的 ID
# 字串內容包含特殊字符，id會不同
s10 = 'Hello!'
s11 = 'Hello!'
print(s10, id(s10))  # 不同的 ID
print(s11, id(s11))  # 不同的 ID
```


## 14. 與 ASCII 的轉換

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
