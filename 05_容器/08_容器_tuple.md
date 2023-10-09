# tuple（或稱「數組、元組」）

- 不可變的(Immutable)
- 有序序列，可通過索引訪問
- 成員可以是不同資料類型，成員也可以是數組
- 因為不可變，所以可用來做為字典(dict)的鍵(key)
- 因為 tuple 不可變，所以可作為不可變集合(set)的成員，而列表(list)因為可變所以不可作為 set 的成員。
- 可使用一個數組來打包一個函數同時傳出的多的回傳值。

---

## 初始化

- 因為不可變，所以初始化後重新指定數組的內容等同是建立新的數組
- 可用小括號「( )」建立
- 可用「,」相隔來建立，也稱為「打包」，反向動作稱為「解包」

*範例*

### 1. 初始化一個空元組

```python
my_tuple = ()
print(my_tuple, type(my_tuple))
```

```
    () <class 'tuple'>
```

### 2. 使用「,」初始化一個元組

```python
my_tuple = 1, 2, 3
print(my_tuple, type(my_tuple))
# 原本的 id
print(my_tuple, id(my_tuple))   # 結果：(1, 2, 3) 140704816316800
```

```
    (1, 2, 3) <class 'tuple'>
    (1, 2, 3) 140401150822848
```

### 3. 重新指定數組的成員

```python
my_tuple = (1, 2, 3)
# 重新指定後的 id
print(my_tuple, id(my_tuple))   # 結果：(1, 2, 3) 140704816316800
```

```
    (1, 2, 3) 140401151079872
```

### 4. 訪問元組的成員

```python
print(my_tuple[0]) # 1
```

```
    1
```

### 5. 成員可以是不同的資料型態

```python
my_tuple = (1, 2, 3, 'Hello', True)
print(my_tuple)
```

```
    (1, 2, 3, 'Hello', True)
```

### 6. 元組的成員不可以被修改

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

```
    發生錯誤，錯誤訊息： 'tuple' object does not support item assignment
```

---

## 特性

### 1. 只有一個成員的數組

- 定義一個只包含一個元素的元組
- 需要添加逗號來防止被誤認為數學表達式(加減乘除的括號)

```python
my_single_tuple = (1,)  
print(my_single_tuple)  # Output: (1,)
```

*輸出結果*

```
    (1,)
```

### 2. index 索引

```python
# 初始化一個元組
my_tuple = ('AAA', 'BBB', 'CCC', 'DDD', 'EEE')
print(my_tuple)  # ('AAA', 'BBB', 'CCC', 'DDD', 'EEE')

# 單一索引
print(my_tuple[0])  # AAA
# 負索引，從最後開始計算，-1 表示最後一個元素
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

```
    ('AAA', 'BBB', 'CCC', 'DDD', 'EEE')
    AAA
    EEE
    ('BBB', 'CCC')
    ('AAA', 'BBB')
    ('BBB', 'CCC', 'DDD', 'EEE')
    ('AAA', 'BBB', 'CCC', 'DDD', 'EEE')
```

### 3. len 長度

```python
# 初始化一個元組
my_tuple = ('AAA', 'BBB', 'CCC', 'DDD', 'EEE')
# 使用 len() 函式取得元組的長度，有傳出值
_len = len(my_tuple)
print(f'數組的長度是 {_len}')
```

*輸出結果*

```
    數組的長度是 5
```

### 4. count 計算

- count(element): 返回元组中出现的指定元素的次数

```python
my_tuple = ('AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'AAA')
# 計算 AAA 出現的次數
_count = my_tuple.count('AAA')
# 輸出結果
print(f'AAA 出現的次數 {_count}')  # AAA 出現的次數2
```

*輸出結果*

```
    AAA 出現的次數 2
```

### 5. 解包（相對於打包）

```python
# 初始化一個元組
my_tuple = ('AAA', 'BBB', 'CCC', 'DDD', 'EEE')

# 元組解包
a, b, c, d, e = my_tuple
print(f'a={a}, b={b}, c={c}, d={d}, e={e}')

```

*輸出結果*

```
    a=AAA, b=BBB, c=CCC, d=DDD, e=EEE
```

---END---
