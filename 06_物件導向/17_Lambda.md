# Lambda 函數

Lambda 函數在 Python 中是一種快速定義 `單行函數` 的語法，也稱為 `匿名函數`，因為這些函數不需要一個正式的名稱。

<br>

## Lambda 函數的語法

```python
lambda arguments: expression
```

- `lambda` 是一個關鍵字，用來表示這是一個 `匿名函數`。
- `arguments` 是傳入函數的參數，可以有多個，用逗號分隔。
- `expression` 是一個只有一行的表達式，其結果會被返回。

<br>

## 範例

_列舉幾個範例說明_

<br>

### 範例 1：簡單的 Lambda 函數

```python
add = lambda x, y: x + y
print(add(2, 3))
```

_結果_

```bash
5
```
展示如何定義一個簡單的 Lambda 函數來執行加法。
_`add` 是指向匿名函數的本身，而非返回值。_

<br>

### 範例 2：在 `map()` 函數中使用 Lambda

`map()` 函數用來對可迭代物件中的每一個元素應用一個函數。

```python
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))
```

_結果_

```bash
[1, 4, 9, 16, 25]
```

演示了如何使用 Lambda 函數對一個列表中的每個數字進行平方。
_`squared` 是指向由 map 函數所返回的迭代器本身。_

<br>

### 範例 3：在 `filter()` 函數中使用 Lambda

`filter()` 函數用來過濾可迭代物件中的元素。

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))
```

_結果_

```bash
[2, 4, 6]
```

演示如何使用 Lambda 函數來過濾出列表中的偶數。
_`even_numbers` 是指 filter 函數返回的迭代器本身，而不是返回的值。_

<br>

### 範例 4：在 `sorted()` 函數中使用 Lambda

`sorted()` 函數用來對可迭代物件進行排序。

```python
pairs = [(1, 'one'), (4, 'four'), (3, 'three'), (2, 'two')]
# 使用每個成員的第一個子成員：1、4、3、2 進行排序
sorted_pairs = sorted(pairs, key=lambda x: x[0])
print(sorted_pairs)
# 使用第二個子成員進行排序，先比較第一個字母，相同再比較第二個
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)
```

_結果_

```bash
[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

演示如何使用 Lambda 函數來根據元組的子元素進行排序。

<br>

---

_END_