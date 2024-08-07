# `覆寫 override` 與 `多載 Overload`

_在 Python 中，不能在同一個類別中定義兩個名稱相同的方法，否則後者會覆寫前者。但可以使用預設參數、可變參數等方式達到類似的效果；另外，Python 不支持真正的多載，但可以通過其他方式實現類似效果。_

<br>

## 覆寫 override

1. 覆寫是子類別提供父類別中已定義的方法的特定實作。當子類別繼承了父類別的某個方法，但想要改變該方法的行為時，可以在子類別中重新定義該方法。

<br>

2. 覆寫的方法必須具有與父類別中原始方法相同的名稱、回傳類型及參數列表。

<br>

3. 在 Java、C# 等語言中，可以使用 `@Override` 標註來明確表示一個方法是覆寫的。在 Python 中，沒有這樣的標註，但可以通過相同的方法名稱來實現覆寫。

<br>

4. 覆寫範例。

    ```python
    class Animal:
        def speak(self):
            return "Animal speaks"

    class Dog(Animal):
        # 覆寫父類別的 speak 方法
        def speak(self):
            return "Dog barks"
    
    animal = Animal()
    dog = Dog()
    print(animal.speak())
    print(dog.speak())
    ```

    _輸出_

    ```bash
    Animal speaks
    Dog barks
    ```

<br>

## 多載 Overload

1. 多載是在同一個類別中，根據參數的數量和類型，定義多個名稱相同但參數列表不同的方法。在 Python 中，不支持真正的多載，但可以通過預設參數、可變參數或參數類型檢查來實現類似效果。

<br>

2. 被多載的方法共享相同的名稱，但具有不同的參數列表（可以是不同數量的參數或不同類型的參數）。

<br>

3. 回傳類型不能被用來區分多載的方法。

<br>

4. 預設參數實現多載。

    ```python
    def add(a, b=0, c=0):
        return a + b + c
    
    # 以預設參數實現多載
    print(add(1))
    print(add(1, 2))
    print(add(1, 2, 3))
    ```

    _輸出_

    ```bash
    1
    3
    6
    ```

<br>

5. 使用可變位置參數 `*args` 來實現多載。

    ```python
    class Calculator:
        def add(self, *args):
            if len(args) == 2:
                return args[0] + args[1]
            elif len(args) == 3:
                return args[0] + args[1] + args[2]
            else:
                raise ValueError("Invalid number of arguments")
    
    calc = Calculator()
    print(calc.add(1, 2))
    print(calc.add(1, 2, 3))
    ```

    _輸出_

    ```bash
    3
    6
    ```

<br>

6. 使用參數類型檢查實現多載。

    ```python
    def add(a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + " " + b
        else:
            return "Invalid types"
    
    print(add(1, 2))
    print(add("Hello", "World"))
    print(add(1, "World"))
    ```


    _輸出_

    ```bash
    3
    Hello World
    Invalid types
    ```

<br>

___

_END_