# 名稱改編（Name Mangling）

_Python 針對 `私有性` 所設計的 `名稱改編` 機制，因為改編後仍可訪問，屬於弱化版的私有性機制。_

_顧名思義，就是破壞原有命名，給它一個新的可識別名稱_

</br>

## 說明

1. 在 Python 中，若對類 class 裡面屬性或方法以雙下劃線 `__` 作為前綴命名，Python 會自動對其進行 `名稱改編（Name Mangling）`，或稱為 `名稱修飾`，可視作一種 `私有性` 的機制，主要目的是避免子類不小心重寫了基類中的這個私有屬性或方法。

2. 名稱修飾的過程是 Python 會將這個私有屬性的名稱改成 `_類別名稱__屬性名稱`，其中 `類別名稱` 就是這個私有屬性所屬類的名字，然後加上一個下底線 `_` 作為前綴，`屬性名稱` 就是這個私有屬性原本的名字以及兩個下底線前綴。

3. 這機制保證了即使子類中有同名的私有屬性，它們也不會覆蓋或影響到父類中的私有屬性，也是一種 `解耦`。

</br>

## 範例說明

_本範例說明 `私有性` 在繼承後由於 `名稱改編` 機制，讓父類的同名屬性不會因為子類的繼承而覆蓋。_

1. 以下範例中，子類與父類都有一個標示了 `私有性` 的同名屬性 `__private_var` 。
2. 當在子類中使用 `self._Base__private_var`，實際上是訪問 `父類的私有屬性`，而不是子類自己的私有屬性。
3. 這個 `名稱改編` 機制確保子類中的同名屬性，不會影響到基礎類中的同名屬性，從而避免了潛在的命名衝突和不希望的覆蓋。

<br>

## 範例程式碼

```python
# 父類 Base
class Base:
    def __init__(self):
        # 父類的 __private_var
        self.__private_var = "這是父類私有屬性"
    # 可顯示 __private_var 內容
    def show(self):
        print(self.__private_var)

# 子類 Derived，繼承 Base
class Derived(Base):
    def __init__(self):
        # 調用父類初始化器
        super().__init__()
        # 子類的 __private_var
        self.__private_var = "這是子類私有屬性"

    def display(self):
        print(self.__private_var)
        print(self._Base__private_var)

# 建立父類與子類物件
base = Base()
derived = Derived()
```

<br>

_父類物件調用自己的函數_

```python
base.show() 
```

_OUTPUT_

```bash
這是父類私有屬性
```

<br>

_子類物件調用自己的函數，無法使用父類的屬性名稱直接訪問，但依舊可以訪問_

```python
derived.display() 
```

_OUTPUT_

```bash
這是子類私有屬性
這是父類私有屬性
```

<br>

## 與沒有設定私有性的狀況做比較

```python
class Base:
  
    def __init__(self):
        self.shared_var = "這是父類的屬性"

    def show(self):
        print(self.shared_var)

class Derived(Base):
    def __init__(self):
        super().__init__()
        # 子類重寫了父類的同名屬性
        self.shared_var = "這是子類的屬性"

    def display(self):
        print(self.shared_var)
```

_實作_

```python
# 建立父類與子類物件
base = Base()
derived = Derived()
# 調用父類方法
base.show() 
# 子類調用父類方法
derived.show()
# 子類調用自己的方法
derived.display()
```

_OUTPUT_

```bash
這是父類的屬性
這是子類的屬性
這是子類的屬性
```

<br>

## 補充說明

1. 特別注意，這種機制並不能阻止外部程式碼存取或修改這些屬性，只是讓這種存取變得更加困難而已。


2. 如果要避免子類重寫父類的屬性或方法，可更直觀地透過 `設計和編碼約定` 來實現，也就是在文件中明確指出哪些屬性和方法是不應該在子類中被重寫，也可以使用 `單下線前綴` 來表示這是一個 `受保護` 的屬性或方法。雖然這依舊不會阻止子類別存取或修改它們，但這樣的命名是一種明確作為向其他開發者傳達了一個訊息： `請不要在子類別中重寫這些屬性或方法，除非你確切知道你在做什麼`。

3. 簡單說，就是使用了內建的機制並無法阻止子類改寫、外部訪問與外部修改，那就不要調用這個機制，改用口頭警告後果自負便可。 

<br>

---

_END_
