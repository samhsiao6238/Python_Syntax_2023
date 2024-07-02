# 實例化 instantiate vs. 初始化 initiate

_在 Python 中，實例化（instantiate）和初始化（initiate）是兩個相關但區別明顯的概念。_

<br>

## 實例化（Instantiation）

實例化是指根據類的定義建立一個該類的實例的過程，當一個類被實例化時，Python 會呼叫該類的 `__new__` 方法來建立一個物件，然後呼叫 `__init__` 方法來初始化該物件的屬性，實例化的 `結果` 就是一個新的 `物件` ，或稱 `對象`。

```python
class MyClass:
    def __init__(self, value):
        self.value = value

# 實例化 MyClass，建立一個 MyClass 的實例
obj = MyClass(10)
```

<br>

## 初始化（Initiation）

初始化是指在一個對象 `被建立後`，設定它的 `初始狀態` 的過程，在 Python 中，這會在 `__init__` 方法中完成的，這個方法可以設置對象的屬性和執行其他需要在對象建立後立即執行的任何設置。

```python
class MyClass:
    def __init__(self, value):
        self.value = value  # 初始化 value 屬性

# obj 被實例化並初始化
obj = MyClass(10)
```

<br>

## 本質上的差異

1. 本質上，實例化是建立對象的過程，而初始化是設置對象初始狀態的過程。

2. 實例化通常涉及分配內存和建立對象，而初始化則是設置對象的內部狀態以便它能正常工作。

3. 初始化是在實例化之後，若有特殊需求，可以覆寫 `__new__` 方法來改變實例化的過程，或覆寫 `__init__` 方法來改變初始化的過程。


<br>

---

_END_