# 參數 Parameter 與 引數 Argument 的異同

- 在 Python 中，參數 `Parameter` 和引數 `Argument` 雖然在一些場合可以交換使用，但是它們通常有著微妙的區別。

<br>


## 參數（Parameter）：

- 在`定義` 函數或方法時，我們在括號內列出的變數被稱為 `參數` ，代表了函數或方法的輸入規範。


```python
def add(a, b):  # 'a' 'b' 就是參數 parameters
    return a + b
```
<br>

## 引數（Argument）

- 引數是在 `調用` 函數或方法時，提供給括號內的 `實際值` ，它們是實際傳遞給函數或方法的具體值。

- 在這個例子中，定義了一個名為 add 的函數，它接受兩個參數 a 和 b。
- 然後調用這個函數，並傳遞了兩個引數 2 和 3 給它。

```python
# 2、3 是引數
result = add(2, 3)  
```

<br>


## 高階用法

    _Python 還支持一些更進階的參數和引數處理方式_

<br>

1. 預設參數 `Default Parameters`：允許在定義函數時為參數提供 `預設值`。

    ```python
    def greet(name="World"):
        return f"Hello, {name}!"

    print(greet())        # 輸出：Hello, World!
    print(greet("Alice")) # 輸出：Hello, Alice!
    ```

<br>

2. 關鍵字引數 `Keyword Arguments`：允許在調用函數時通過 `名稱` 明確地指定引數的值。

    ```python
    def introduce(first_name, last_name):
        return f"My name is {first_name} {last_name}"

    print(introduce(first_name="John", last_name="Doe"))  # 輸出：My name is John Doe
    ```

<br>

3. 可變長度引數 (Variable-length Arguments)：允許函數接受任意數量的引數。

- `*args`：用於傳遞任意數量的 `位置引數`，並將其儲存為 `元組`。
- `**kwargs`：用於傳遞任意數量的 `關鍵字引數` ，並將其儲存為 `字典`。

    ```python
    def print_args(*args, **kwargs):
        for arg in args:
            print(arg)
        for key, value in kwargs.items():
            print(f"{key} = {value}")

    print_args(1, 2, 3, a="apple", b="banana")
    ```
    _OUTPUT_
    ```bash
    1
    2
    3
    a = apple
    b = banana
    ```
  
<br>

---

_END_


