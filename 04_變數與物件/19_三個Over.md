# Python 中有三個 Over

1. override 覆寫：當子類中定義了與父類同名的方法或屬性時，子類的方法或屬性會覆寫父類的，這就是所謂的方法覆寫或屬性覆寫。
2. overwrit 覆蓋
3. overload 多載：Python不支援傳統意義上的函數重載，但可以使用預設參數、可變參數等技巧來達到相似的效果。

<br>

## 說明

1. Override (覆寫)

    當子類別定義了與父類別同名的方法時，該方法會覆寫父類別中的方法，稱為方法覆寫（Method Override）。

    ```python
    class Parent:
        def say_hello(self):
            return "Hello from Parent"

    class Child(Parent):
        def say_hello(self):
            return "Hello from Child"

    # 使用子類別建立實例
    child_instance = Child()
    print(child_instance.say_hello())
    ```

    _結果_

    ```bash
    Hello from Child
    ```

<br>

2. Overwrite (覆蓋)

    在 Python 中，變數或資料的覆蓋指的是將一個變數的內容替換為新的內容。

    ```python
    # 變數資料覆蓋
    variable = "Original"
    print(variable)

    variable = "Overwritten"
    print(variable)
    ```

    _結果_

    ```bash
    Original
    Overwritten
    ```

<br>

3. Overload (多載)

    雖然 Python 本身不支援傳統的函數多載，但是可以通過預設參數值或是可變參數列表來模擬多載的行為。

    ```python
    def func(a, b=None):
        if b is not None:
            return a + b
        else:
            return a

    print(func(10))
    print(func(10, 20))
    ```

    _結果_

    ```bash
    10
    30
    ```

<br>

4. 多載還可以使用 `*args` 和 `**kwargs` 捕獲任意數量的未命名和命名參數。

    ```python
    def func(*args, **kwargs):
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)

    func(1, 2, 3, a='foo', b='bar')
    ```

    _結果_

    ```bash
    Positional arguments: (1, 2, 3)
    Keyword arguments: {'a': 'foo', 'b': 'bar'}
    ```


<br>

---

_END_
