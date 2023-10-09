# 主題：*args 和 **kwargs

- 兩者都是 Python 正式的語法，被用在函數定義中，以允許函數接收 *可變數量* 的參數。

- args 和 kwargs 只是約定俗成的名稱，並非保留字或語法。
  
- args 是 arguments 的縮寫，表示位置參數列表。
  
- kwargs 是 keyword arguments 的縮寫，表示關鍵字參數字典。



## *args

- 使用 *args 讓函數可以接收任意數量的位置參數，並將它們儲存在一個名為「args」的 tuple 中。
  
- 使用在不確定函數會接收多少個參數的情境。


```python
# 定義一個函式，接收任意數量的參數，並印出參數的型別與值
def print_args(*args):
    # args是一個tuple
    print(type(args))
    print('------------------')
    # 逐一印出args的元素
    for arg in args:
        print(type(arg))
        print(arg)

# 呼叫函式，傳入1, 2, 3, 'four'四個引數
print_args(1, 2, 3, 'four')
```

```
    <class 'tuple'>
    ------------------
    <class 'int'>
    1
    <class 'int'>
    2
    <class 'int'>
    3
    <class 'str'>
    four
```

## **kwargs

- **kwargs 的使用方式類似於 *args

- 允許接收任意數量的關鍵字參數，並將它們儲存在一個名為「kwargs」的字典中，讓函數可以操作 key-value 組成的對。


```python
# 定義一個函式，接收任意數量的關鍵字參數，並印出參數的名稱與值
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')
# 輸出
print_kwargs(AAA='aaa', BBB='bbb', CCC=999)
```

```
    AAA = aaa
    BBB = bbb
    CCC = 999
```

### 同時接收
 
- 函數可以同時接收 *args 和 **kwargs，在這種情況下，*args 必須出現在 **kwargs 之前。


```python
# 定義一個函式，接收任意數量的引數與關鍵字參數，並印出參數的名稱與值
def print_args_and_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f'{key} = {value}')
# 呼叫函式，傳入1, 2, 3, name='John', age=30五個引數
print_args_and_kwargs(1, 2, 3, name='John', age=30)
```

```
    1
    2
    3
    name = John
    age = 30
```

---

END
