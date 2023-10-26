# 屬性 

    _Property ＆ Attribute_

- 關於裝飾字屬性（property）將在裝飾字部分做進一步說明。

<br>

## Attribute 屬性

- 在 Python 中，類別實體的變數稱為 `屬性 Attribute` 。

- 這些變數可以在建立物件當下，或建立完成之後的任何時候直接 `set 設置` 和 `get 獲取` 。


```python
# 自訂類別
class MyClass:
    # 初始化函式
    def __init__(self):
        # 定義屬性
        self.attribute = "這是 attribute"

# 建立物件
obj = MyClass()
# 印出物件的屬性
print(obj.attribute)
# 修改物件的屬性
obj.attribute = "這是修改後的 attribute"
print(obj.attribute)
```

```bash
這是 attribute
這是修改後的 attribute
```

<br>

## Property 屬性

- 在 Python 中，Property 是一種特殊類型的屬性，使得方法可以被像一般的屬性那樣訪問。

- Property 允許開發者在物件上定義像屬性一樣可操作的方法，當這些方法被當作屬性訪問時，它們會自動執行。
  
- Property 可以使用 @property 裝飾器來定義，一旦方法被標註為 @property，那麼該方法可以像普通屬性那樣被訪問，而不需要加上()，並可使用 @method_name.setter 和 @method_name.deleter 來定義設置屬性值和刪除屬性的行為。

- 讓開發者對屬性有更多的控制，例如可以在這些方法中添加驗證、緩存、記錄等行為。
  
- 讓開發者可以在獲取、設置和刪除屬性時進行額外的操作。


```python
# 定義類別
class MyClass:
    # 初始化函式
    def __init__(self):
        # 這是一個私有屬性(attribute)，不希望直接被訪問，而是通過 property 操控。
        self._attribute = None

    # 這是屬性的 getter 方法，當訪問這個屬性時，會執行此方法。
    @property
    def attribute(self):
        print("---Getting attribute---")
        return self._attribute

    # 這是屬性的 setter 方法，當嘗試設定這個屬性的值時，會執行此方法。
    @attribute.setter
    def attribute(self, value):
        print("---Setting attribute---")
        self._attribute = value

    # 這是屬性的 deleter 方法，當嘗試刪除這個屬性時，會執行此方法。
    @attribute.deleter
    def attribute(self):
        print("---Deleting attribute---")
        del self._attribute

# 建立物件
obj = MyClass()

# 賦予物件的屬性一個值，會自動執行 setter
obj.attribute = "我賦予物件 property"

# 印出物件的屬性，這會自動呼叫 getter 來取得屬性的值
print(obj.attribute)

# 刪除物件的屬性，這會自動呼叫 deleter
del obj.attribute
```

```bash
---Setting attribute---
---Getting attribute---
我賦予物件 property
---Deleting attribute---
```

<br>

---

_END_
