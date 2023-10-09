# 主題：set 集合

- 成員不可重複且成員須為不可變資料類型（如 tuple）

- set 是可變變數，但其成員為不可變

- 無序，不可透過索引訪問

- 雜湊，可雜湊（成員不同類型）不可變類型資料，如整數、浮點數、字符串、數組

- 運算上類似於數學中的集合，可進行聯集、交集、差集操作

---

## 初始化

```python
# 初始化一個空集合
my_set = set()
```

## 方法

### 1. 添加成員 add

```python
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

```
    {'AAA', 'BBB'}
    {'DDD', 'BBB', 'EEE', 'CCC', 'AAA'}
```

</b>

### 2. 移除成員 remove


```python
# 初始化一個集合
my_set = {'AAA', 'BBB', 'CCC'}
# 移除元素
my_set.remove('AAA')
print(my_set) 
```

```
    {'CCC', 'BBB'}
```

</b>

### 3. 長度 len


```python
# 初始化一個集合
my_set = {'AAA', 'BBB', 'CCC'}

# 查看集合長度
print(len(my_set))  # Output: 3
```

```
    3
```

</b>

### 4. 成員運算子


```python
# 初始化一個集合
my_set = {'AAA', 'BBB', 'CCC'}

# 測試元素是否在集合中
print('AAA' in my_set)  # Output: True
print('DDD' in my_set)  # Output: False
```

```
    True
    False
```

</b>

### 5. 集合的數學操作 

- union 
- intersection 
- difference


```python
# 初始化兩個集合
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
```

#### 聯集
```python
print(set1.union(set2))
```
    *輸出結果*
```
    {1, 2, 3, 4, 5, 6}
```

#### 交集
```python
print(set1.intersection(set2))
```
    *輸出結果*
```
    {3, 4}
```

#### 差集， se1 - set2 （與 symmetric_difference 不同）
```python
print(set1.difference(set2))
print(set2.difference(set1))
```
    *輸出結果*
```
    {1, 2}
    {5, 6}
```

#### 對稱差集
```python
print(set1.symmetric_difference(set2))
```
    *輸出結果*
```
    {1, 2, 5, 6}
```

#### isdisjoint()
- 判斷兩個集合是否包含相同的元素，如果沒有返回 True，否則返回 False
```python
print(set1.isdisjoint(set2))
```
    *輸出結果*
```
False
```

#### issubset() 

- 判斷集合的所有元素是否都包含在指定集合中，如果是則返回 True，否則返回 False
  
```python
print(set1.issubset(set2))
```
    *輸出結果*
```
    False
```

#### issuperset()

- 判斷指定集合的所有元素是否都包含在原始的集合中，如果是則返回 True，否則返回 False
  
```python
print(set1.issuperset(set2)) 
```
    *輸出結果*
```
    False
```

</b>

### 6. discard(elem) 從集合中刪除元素

- 如果元素不存在，則不進行任何操作。


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
```
    {'AAA', 'CCC'}
    {'AAA', 'CCC'}
```

</b>

### 7. pop() 刪除並返回集合中的一個隨機元素

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
```
    AAA
    {'BBB'}
    BBB
    set()
    集合已經空了
```

</b>

### 8. clear() 刪除集合中的所有元素


```python
# 初始化一個集合
my_set = {'AAA', 'BBB', 'CCC'}
#
my_set.clear()
print(my_set)
```

```
    set()
```

---

END
