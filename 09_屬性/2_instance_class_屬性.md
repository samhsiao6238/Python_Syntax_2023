# Instance & Class

<br>

## 說明

1. Instance Attributes：這些屬性是特定於每個物件的，當以類別建立一個物件時，實例 instance 屬性將對於每個物件都是唯一的，也稱為 `實例屬性`、`物件屬性`。

2. Class Attributes：這些屬性是共享的，對於該類別的所有實例都是相同的。因此，當其中一個物件更改類屬性時，它對所有其他物件也將改變，也稱為 `類別屬性`、`靜態屬性 Static Attributes`、`型別屬性 Type Attributes`。

<br>

## 比較

### Instance Attributes 實體屬性

1. 範例

    ```python
    class MyClass:
        def __init__(self, value):
            self.instance_attribute = value  # 這是 instance attribute

    obj1 = MyClass(10)
    obj2 = MyClass(20)

    print(obj1.instance_attribute)  
    print(obj2.instance_attribute)  

    ```
    _結果_
    ```bash
    10
    20
    ```

<br>

### Class Attributes 類的屬性
   
_也稱為 Static Attributes 或 Type Attributes_

<br>

1. 特性

   - 常數：這些屬性通常不會改變，並在整個程式中提供固定的值。

   - 共享：所有的實例都使用相同的數值。

   - 狀態計數或跟蹤：可以用來跟踪與整個類別相關的信息，例如物件的計數。

<br>


2. 範例一

    ```python
    class MyClass:
        class_attribute = "這是 class attribute"  

        def __init__(self, value):
            self.class_attribute = value

    obj = MyClass("這是 instance attribute")
    print(obj.class_attribute)      # 輸出: 這是 instance attribute
    print(MyClass.class_attribute)  # 輸出: 這是 class attribute
    ```
    _結果_
    ```bash
    這是 instance attribute
    這是 class attribute
    ```

<br>


3. 範例 2

    ```python
    class MyClass:
        class_attribute = 0

        def __init__(self, value1, value2):
            MyClass.class_attribute = value1   # 更改 class attribute 的值
            self.instance_attribute = value2   # 設置 instance attribute 的值

    obj1 = MyClass(10, 10)
    print(MyClass.class_attribute)  # 顯示 MyClass 的 class_attribute
    print(obj1.class_attribute)     # 顯示 obj1 的 class_attribute
    print(obj1.instance_attribute)  # 顯示 obj1 的 instance_attribute
    print('======================')
    obj2 = MyClass(20, 20)
    print(MyClass.class_attribute)  # 顯示 MyClass 的 class_attribute (已被 obj2 修改)
    print(obj2.class_attribute)     # 顯示 obj2 的 class_attribute
    print(obj2.instance_attribute)  # 顯示 obj2 的 instance_attribute
    print('======================')
    print(MyClass.class_attribute)  # 顯示 MyClass 的 class_attribute (仍然是 obj2 所修改的)
    print(obj1.class_attribute)     # 顯示 obj1 的 class_attribute
    print(obj1.instance_attribute)  # 顯示 obj1 的 instance_attribute
    ```
    _結果_
    ```bash
    10
    10
    10
    ======================
    20
    20
    20
    ======================
    20
    20
    10
    ```

<br>

---

_END_
