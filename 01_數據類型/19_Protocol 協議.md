# Protocol 協議

_內建模組 typing 的功能_

<br>

## 說明

1. 從 Python 3.8 開始，`typing` 模組引入了 `Protocol`，允許定義一組方法集合作為一個接口，任何實現了這些方法的類都被視為實作了該接口，也就成為該協定的實現類，而無需透過繼承來實現。

2. 這是一種結構型子類化（duck typing）的形式，也就是擴展了 Python 的 `duck typing` 能力，允許進行更細緻的類型檢查和保證，提高程式碼的靈活性和安全性，同時在不綁定具體類實現的情況下，強制確保某些類提供特定的方法。

<br>

## 範例

1. 程式碼。

    ```python
    from typing import Protocol

    # 定義一個 Protocol，名為 Closable
    class Closable(Protocol):
        def close(self) -> None:
            ...

    # 定義一個函數，它接受一個包含 Closable 物件的列表
    def close_things(things: List[Closable]) -> None:
        for thing in things:
            thing.close()

    # 定義兩個類，它們各自實現了 close 方法
    class File:
        def close(self) -> None:
            print("File closed")

    class Connection:
        def close(self) -> None:
            print("Connection closed")

    # 建立 File 和 Connection 的實例，並將它們傳遞給 close_things 函數
    close_things([File(), Connection()])  # 正確執行
    ```

<br>

2. 以上程式碼中，`Closable` 是一個協議且定義了一個 close 方法，任何具有 close 方法的類都可以視為 Closable，這是一個典型的 _結構型子類化應用_，`File` 和 `Connection` 類雖然沒有明確繼承自 `Closable`，但由於它們實現了 close 方法，根據協議的要求，它們都被視為 Closable 的實例。

<br>

3. `close_things` 函數接受一個 Closable 物件列表，並調用列表中每個對象的 close 方法，這表示此函數期望其參數列表中的每個對象都遵循 Closable 協議。 

<br>

___

_END

