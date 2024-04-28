# 重要觀念

_尚未分類的部分_

<br>

## 位置參數與關鍵字參數


1. 位置參數 (Positional Arguments)：它們是在函數調用時基於它們的位置（即順序）被傳遞的參數。例如，在 `add(1, 2)` 中，`1` 和 `2` 就是位置參數。

2. 可變位置參數 (Varargs or *args)：這允許你在函數調用時傳遞任意數量的位置參數。它們在函數內部被視為一個元組。例如，在 `add(1, 2, 3, 4)` 中，如果 `add` 函數被定義為 `def add(*args)`, 那麼 `args` 在函數內部會是一個元組 `(1, 2, 3, 4)`。

3. 關鍵字參數 (Keyword Arguments)：在函數調用時，它們是基於名稱（而不是位置）被傳遞的參數。例如，`add(a=1, b=2)` 中，`a` 和 `b` 是關鍵字參數。

4. 可變關鍵字參數 (**kwargs or **args)：這允許你傳遞任意數量的關鍵字參數。它們在函數內部被視為一個字典。例如，如果 `add` 函數被定義為 `def add(**kwargs)`, 而你調用 `add(a=1, b=2, c=3)`, 那麼 `kwargs` 在函數內部會是一個字典 `{'a': 1, 'b': 2, 'c': 3}`。

<br>

## 覆寫 (override)」和 多載 (overload)

1. 覆寫 (Override)
   - 覆寫是子類別提供父類別中已定義的方法的特定實作。當子類別繼承了父類別的某個方法，但想要改變該方法的行為時，可以在子類別中重新定義該方法。
   - 覆寫的方法必須具有與父類別中原始方法相同的名稱、回傳類型及參數列表。
   - 在 Java、C# 等語言中，可以使用 `@Override` 標註來明確表示一個方法是覆寫的。

2. 多載 (Overload)
   - 多載是在同一個類別中，根據參數的數量和類型，定義多個名稱相同但參數列表不同的方法。
   - 被多載的方法共享相同的名稱，但具有不同的參數列表（可以是不同數量的參數或不同類型的參數）。
   - 回傳類型不能被用來區分多載的方法。

<br>

### 說明

1. 在 Python 中不能在同一個類別中定義兩個名稱相同的方法，否則後者會覆寫前者。但可以使用預設參數、可變參數等方式達到類似的效果。

<br>

### 範例

1. 覆寫

    ```python
    class Animal:
        def speak(self):
            return "Animal speaks"

    class Dog(Animal):
        # 覆寫父類別的 speak 方法
        def speak(self):
            return "Dog barks"

    class Calculator:
        # 多載 add 方法
        def add(self, a, b):
            return a + b

        # 另一個多載的 add 方法，接受三個參數
        def add(self, a, b, c):
            return a + b + c
    ```



2. 多載：預設參數

    ```python
    def add(a, b=0, c=0):
        return a + b + c
    
    # 以預設參數實現多載
    add(1)          # 結果為 1
    add(1, 2)       # 結果為 3
    add(1, 2, 3)    # 結果為 6
    ```

   
3. 範例：使用可變位置參數 *args 來實現多載

    ```python
    class Calculator:
        def add(self, *args):
            if len(args) == 2:
                return args[0] + args[1]
            elif len(args) == 3:
                return args[0] + args[1] + args[2]
            else:
                raise ValueError("Invalid number of arguments")

    ```

4. 範例：使用參數類型檢查

    ```python
    def add(a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + " " + b
        else:
            return "Invalid types"
    ```

<br>


---

_END：持續補充中_