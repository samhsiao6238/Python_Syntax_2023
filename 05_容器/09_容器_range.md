# 主題 range 

## 說明

- range 是一個內建的類別，且有一個同名的內建函數 range()，可用於創建 range 物件。

- range 的物件是一個 *不可變的* 數字序列，並常常用在迴圈中進行特定次數的迭代。

- range 物件佔用的記憶體空間與 *range 的成員數量大小* 無關，只與 range 的起始、結束和間隔大小有關。這使得 range 對象在表示大範圍時非常高效。

---

## 應用

### 1. 使用 range() 函數創建範圍


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
```
    range(0, 5) <class 'range'>
    [0, 1, 2, 3, 4]
    [1, 2, 3, 4, 5]
    [1, 3, 5, 7, 9]
```

### 2. 長度


```python
r = range(5)
print(len(r))  # prints: 5
```
```
    5
```

### 3. 搭配使用成員運算子 in


```python
r = range(5)
print(3 in r)  # True
print(5 in r)  # False
```
```
    True
    False
```

### 4. 節省資源


```python
# 這將不會佔用大量記憶體
big_range = range(1000000000)
```

### 5. 搭配 for-in 迴圈使用


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
```
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

---

END
