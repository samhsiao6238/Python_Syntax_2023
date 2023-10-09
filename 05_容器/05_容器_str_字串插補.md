# 字串差捕


## 1. 使用 f-string（在Python 3.6以上的版本可用）


```python
name = "John"
print(f"Hello, {name}!")
```
```
    Hello, John!
```

## 2. 使用.format()


```python
name = "John"
print("Hello, {}!".format(name))
```
```
    Hello, John!
```

## 3. 使用%


```python
name = "John"
print("Hello, %s!" % name)
```
```
    Hello, John!
```

## 4. !r

- 在 f-string 語法中，<font。 color='red'「!r」用於指定在插入值之前要對其調用 repr() 函數</font。

- repr() 函數會返回該物件的「官方字串表達句」，也就是說，該「官方字串表達句」應該足以讓 Python 能夠使用該「官方字串表達句」來重新創建或復刻該物件。(為求詳盡寫得有點咬舌)

- 如果在類中定義了 __repr__() 方法，那麼 repr() 函數就會調用這個方法來獲得「字串表示」。

- 這種表示方式的特點是，當你將這個字串傳給內建的 eval() 函數時，理論上應該可以重新生成該物件。

- 我們會嘗試讓 __repr__() 方法返回一個字串，這個字串能夠表達出如何創建一個與當前對象相同的新對象。

### 範例 1
```python
class Example:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Example({self.value})"

example = Example(5)

# 使用 f-string 和 !r 語法
print(f"The object is: {example!r}") 

```
```
    The object is: Example(5)
```

### 範例 2
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
v = Vector(1, 2)
v1 = repr(v)
print(v1, id(v1))
v2 = repr(v)
print(v2, id(v2))
v3 = eval(repr(v))
print(v3, id(v3))

```
```
    Vector(1, 2) 140510001281456
    Vector(1, 2) 140510001280240
    Vector(1, 2) 140510000952176
```

---

END
