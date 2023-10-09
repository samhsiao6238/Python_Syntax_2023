# Python 私有性的設計
- 本範例說明私有性在繼承後由於 `名稱改編` 機制，讓父類的同名屬性不會因為子類的繼承而覆蓋。

</br>

## 範例說明

- 子類 Derived 繼承父類 Base。
- 子類與父類都有一個標示了私有的同名屬性 `__private_var` 。
- 當在 Derived 中使用 self._Base__private_var，實際上是訪問  `父類的私有屬性`，而不是子類自己的私有屬性。
- 這個 `名稱改編` 機制確保子類中的同名屬性，不會影響到基礎類中的同名屬性，從而避免了潛在的命名衝突和不希望的覆蓋。

```python
class Base:
    def __init__(self):
        self.__private_var = "這是父類私有屬性"

    def show(self):
        print(self.__private_var)

# 繼承
class Derived(Base):
    def __init__(self):
        # 調用父類初始化器
        super().__init__()
        # 子類私有屬性
        self.__private_var = "這是子類私有屬性"

    def display(self):
        print(self.__private_var)
        print(self._Base__private_var)

base = Base()
derived = Derived()
```
- 父類物件調用父類的函數
```python
base.show() 
```
_OUTPUT_
```bash
這是父類私有屬性
```

- 子類物件調用子類的函數
```python
derived.display() 
```
_OUTPUT_
```bash
這是子類私有屬性
這是父類私有屬性
```

## 範例比較

```python
class Base:
    
    def __init__(self):
        self.shared_var = "這是父類的屬性"

    def show(self):
        print(self.shared_var)

class Derived(Base):
    def __init__(self):
        super().__init__()  # Call the constructor of the base class
        self.shared_var = "這是子類的屬性"

    def display(self):
        print(self.shared_var)

```
```python
base = Base()
derived = Derived()
```
```python
base.show() 
```
_OUTPUT_
```bash
這是父類的屬性
```

- 子類物件調用子類的函數
```python
derived.display() 
```
_OUTPUT_
```bash
這是子類的屬性
```

- 子類物件調用父類的函數
- 已經被覆寫
```python
derived.show()
```
_OUTPUT_
```bash
這是子類的屬性
```

---

END