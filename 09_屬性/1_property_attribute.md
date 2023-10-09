# 主題：屬性

- 關於裝飾字屬性（property）將在裝飾字部分做進一步說明。

## Attribute
- 在 Python 中，類別的實例變數通常被稱為屬性（Attribute）。

- 這些變數可以在建立物件當下，或建立完成之後的任何時候直接設置和獲取。


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
obj.attribute = "這是新的 attribute"
print(obj.attribute)
```

```
    這是 attribute
    這是新的 attribute
```

## Property 

- 是一種特殊類型的屬性

- property 提供了一種在物件上定義可操作的屬性的方法。
  
- 可以使用 @property 裝飾器創建屬性，然後再用相同名稱的方法來添加 @method.setter 和 @method.deleter。

- 讓開發者對屬性有更多的控制，例如可以在這些方法中添加驗證、緩存、記錄等行為。
  
- 讓開發者可以在獲取、設置和刪除屬性時進行額外的操作。


```python
# 定義類別
class MyClass:
    # 初始化函式
    def __init__(self):
        # 定義屬性(attribute)
        self._attribute = None

    # 將屬性定義為 property，預設為 getter
    @property
    def attribute(self):
        print("---Getting attribute---")
        return self._attribute

    # 定義屬性，並設定 setter
    @attribute.setter
    def attribute(self, value):
        print("---Setting attribute---")
        self._attribute = value

    # 定義屬性，並設定 deleter
    @attribute.deleter
    def attribute(self):
        print("---Deleting attribute---")
        del self._attribute

# 建立物件
obj = MyClass()
# 建立物件的屬性，會自動執行 setter
obj.attribute = "我賦予物件 property"
# 印出物件的屬性，會先執行 getter，再印出
print(obj.attribute)
# 刪除物件的屬性，會自動執行 deleter
del obj.attribute
```

```
    ---Setting attribute---
    ---Getting attribute---
    我賦予物件 property
    ---Deleting attribute---
```

---

END
