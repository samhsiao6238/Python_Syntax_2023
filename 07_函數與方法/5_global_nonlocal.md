# global 和 nonlocal

<br>

## 說明
1. Python 中的兩個關鍵字，用於 _變數的作用範圍_ 管理。

2. global 可以在函數或其他局部作用範圍內部修改全局變數。

3. nonlocal 主要用在巢狀函數中，使得在巢狀函數的內部函數中可以修改巢狀函數的外部函數的變數。

</br>


## 1. global

- global 關鍵字可以在函數或其他局部作用範圍內部修改全局變數。

- 如果沒有使用 global 關鍵字，在函數內部賦值給變數時，將僅僅創建或修改一個新的局部變數，而不會影響到全局變數。

    ```python
    x = 10
    # 定義函數
    def change_global_x():
        global x  # 指明要使用的是全局的 x
        x = 20

    # 調用函數
    change_global_x()
    print(x)
    ```

    _輸出結果_

    ```bash
    20
    ```

</br>

## 2. nonlocal

- `nonlocal` 關鍵字的作用和 `global` 類似，但它主要用在 `巢狀函數（nested function）` 中。

- 可使在 `巢狀函數` 的 `內部函數` 中，可以修改 `外部函數` 的變數。

    ```python
    def outer():
        x = 10
        def inner():
            # 指明我們要使用的是外部函數的x
            nonlocal x  
            x = 20
        inner()
        print(x)  

    outer()
    ```
    _輸出結果_
    ```bash
    20
    ```
    _註解起來比較看看_
    ```python
    def outer():
        x = 10
        def inner():
            # 指明我們要使用的是外部函數的x
            # nonlocal x  
            x = 20
        inner()
        print(x)  

    outer()
    ```
    _輸出結果_
    ```bash
    10
    ```


</br>

## 3. 比較

- 上述範例若改用 `global` ，將輸出 `10`
  
  _示範在 `巢狀函數` 中使用 global_

    ```python
    
    def outer():
        x = 10
        def inner():
            # 指明我們要使用的是外部函數的x
            global x  
            x = 20
        inner()
        print(x)

    outer()
    ```
    _輸出結果_
    ```
        10
    ```

<br>

---

_END_
