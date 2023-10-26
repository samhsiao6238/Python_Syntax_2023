# *args 和 **kwargs

_arguments and keyword arguments_

<br>

## 說明

1. 兩者都是 Python 正式的語法，被用在函數定義中，以允許函數接收 _可變數量_ 的引數。

2. args 和 kwargs 只是 `約定俗成的名稱`，並非保留字或特定語法。
  
3. args 是 arguments 的縮寫，表示 `位置引數元組` 。
  
4. kwargs 是 keyword arguments 的縮寫，表示 `關鍵字引數字典` 。

<br>

## *args

- 使用 *args 讓函數可以接收 `任意數量` 的 `位置引數` ，並將它們儲存在一個名為 `args` 的 `tuple` 中。
  
- 使用在不確定函數會接收多少個引數的情境。


```python
# 定義一個函式，接收任意數量的引數，並印出參數的型別與值
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
_結果_
```bash
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

<br>

## **kwargs

- **kwargs 的使用方式類似於 *args

- 允許接收任意數量的 `關鍵字引數`，並將它們儲存在一個名為 `kwargs` 的字典中，讓函數可以操作 key-value 組成的對。


```python
# 定義一個函式，接收任意數量的關鍵字參數，並印出參數的名稱與值
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')
# 輸出
print_kwargs(AAA='aaa', BBB='bbb', CCC=999)
```
_結果_
```bash
AAA = aaa
BBB = bbb
CCC = 999
```

<br>

## 同時接收 *args 和 **kwargs
 
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
_結果_
```bash
1
2
3
name = John
age = 30
```

<br>

---

_END_
