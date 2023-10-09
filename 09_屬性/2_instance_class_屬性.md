# 主題：Instance & Class

- Instance Attributes 可稱為實例屬性、物件屬性。

- Class Attributes 可稱為類別屬性，也可表示為 Static Attributes 、Type Attributes。

---

## 1. Instance Attributes


```python
class MyClass:
    def __init__(self, value):
        self.instance_attribute = value  # 這是 instance attribute

obj1 = MyClass(10)
obj2 = MyClass(20)

print(obj1.instance_attribute)  
print(obj2.instance_attribute)  

```

```
    10
    20
```

</b>

## 2. Class Attributes
   
    *也稱為 Static Attributes 或 Type Attributes*

- 常數

- 共享

- 狀態計數或跟蹤

</b>

### 範例 1
```python
class MyClass:
    class_attribute = "這是 class attribute"  

    def __init__(self, value):
        self.class_attribute = value

obj = MyClass("這是 instance attribute")
print(obj.class_attribute)      # 輸出: 這是 instance attribute
print(MyClass.class_attribute)  # 輸出: 這是 class attribute
```

```
    這是 instance attribute
    這是 class attribute
```

</b>

### 範例 2
```python
# class/static attributes
class MyClass:
    class_attribute = 0

    def __init__(self, value1, value2):
        MyClass.class_attribute = value1
        self.instance_attribute = value2


obj1 = MyClass(10, 10)
print(MyClass.class_attribute)
print(obj1.class_attribute)
print(obj1.instance_attribute)
print('======================')
obj2 = MyClass(20, 20)
print(MyClass.class_attribute)
print(obj2.class_attribute)
print(obj2.instance_attribute)
print('======================')
print(MyClass.class_attribute)
print(obj1.class_attribute)
print(obj1.instance_attribute)

```

```
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

---

END
