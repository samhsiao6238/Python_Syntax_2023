# 關於 call and invoke

在程式領域中，`invoke` 和 `call` 這兩個術語通常用來描述對函數或方法的執行過程，儘管在很多情況下這兩個詞可以互換使用，但在某些語境下它們可能會有細微的差異。

在 Python 中，`call` 通常用來描述直接執行一個函數或方法的操作，而 `invoke` 可能會在更廣泛或更抽象的語境中使用。

以下說明這兩個詞在 Python 語境中的一些細節。

<br>

## Call

<br>

### 函數與方法的呼叫過程

1. 函數呼叫 (Call)

    在 Python 中，執行一個函數或方法的操作通常透過在識別符後緊接一對圓括號 () 來完成，此行為稱為函數呼叫。

    ```python
    def greet(name):
        return f"Hello, {name}!"

    # 函數呼叫
    message = greet("Alice")
    print(message)
    ```

    _結果_:

    ```bash
    Hello, Alice!
    ```

2. 可呼叫物件 (callable)

    Python 通過 `callable` 內建函數提供了一種機制，用於判斷某個物件是否可以像函數那樣被呼叫。當物件實作了 `__call__` 魔術方法時，該物件成為可呼叫物件。

    ```python
    class Adder:
        def __call__(self, x, y):
            return x + y

    # 實例化類別以創建可呼叫物件
    add = Adder()
    print(callable(add))  # 判斷物件是否可呼叫
    print(add(2, 3))      # 呼叫物件
    ```

    _結果_:

    ```bash
    True
    5
    ```

3. 呼叫過程描述 (Call Description)

    呼叫過程在 Python 中指的是使用函數名稱，隨後附上一組包含參數的圓括號，從而觸發該函數執行的具體操作。這個過程是同步的，意味著函數將按照提供的參數進行操作，直到返回結果。

    ```python
    def sum(a, b):
        return a + b

    # 呼叫函數
    result = sum(1, 2)
    print(result)
    ```

    _結果_:

    ```bash
    3
    ```

<br>

## Invoke

1. `Invoke` 通常用來描述更廣泛的呼叫過程，可涉及到一些額外的機制或協定。
2. `Invoke` 在程式設計領域，通常指的是一種通過某些機制間接調用函數或方法的過程。
3. 在物件導向程式設計中， `invoke` 可用來描述對象方法的呼叫，特別是通過反射或其他動態機制執行的呼叫。
4. 在某些框架（framework）或庫（library）中，`invoke` 可能是一個特定的方法或函數，用來執行特定的操作或回調。

<br>


### 在 Python 中的 invoke

1. 反射（Reflection）: 在 Python 中可通過 `getattr` 或 `__getattribute__` 這樣的函數動態地獲取對象的屬性或方法，並通過 `()` 來調用它們，這就是一種 `invoke` 的操作。

```python
class Example:
    # 定義一個方法
    def say_hello(self):
        print("Hello!")

obj = Example()
method = getattr(obj, 'say_hello')
# 通過反射機制來調用 say_hello 方法
method()
```
_OUTPUT_
```bash
Hello!
```

<br>

2. 事件驅動或回調（Event-driven or Callback） 
   
   _在很多框架或庫中，我們會註冊一些回調函數來響應特定的事件，這些回調函數的調用通常是通過框架的內部機制來實現的，這就是一種 `invoke` 的操作。_

```python
def on_click(event):
    print("Button clicked!")

# 假設有一個 GUI 框架，我們註冊 on_click 函數來響應按鈕點擊事件
# button.register_click_event(on_click)
```

3. 通過字符串來調用函數
   
   _在一些動態語言或腳本語言中，有時候會根據字符串來動態地調用函數，這在 Python 中也可以通過反射來實現。_

```python
# 定義函數，輸出訊息
def print_something():
    print("呼叫 print_something 函數")

# 建立一個字串
function_name = "print_something"

# 通過 globals()[function_name] 獲取 print_something 函數對象。
# globals() 返回一個字典，這個字典包含了當前模塊的全局變量。
# 在這個字典中，'print_something' 是函數 print_something 的名稱
# 所以 globals()['print_something'] 返回 print_something 函數對象。
# () 是函數調用操作符，它會調用函數對象。
# 所以這行代碼最終調用了 print_something 函數，並且執行函數內部的代碼。
globals()[function_name]()
```
_OUTPUT_
```python
呼叫 print_something 函數
```

_這範例所要展示的就是 `invoke` 的機制，是一種更為動態和靈活的調用過程，這種調用可能涉及到一些間接性或額外的機制，也是為什麼 `invoke` 描述起來比較抽象的原因。_


<br>

---

_END_