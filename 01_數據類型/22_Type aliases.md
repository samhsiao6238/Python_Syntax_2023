# 類型別名

_Type aliases，Python 3.12 開始，引入了新的 `type` 語句來明確建立類型別名_

<br>

## 說明

1. 在 Python 中，類型別名 `Type aliases` 提供了一種方式來簡化複雜的類型聲明或增強程式碼的可讀性。

2. Python 3.12 所引入的新語句 `type` 可明確建立類型別名，這有助於區分 `普通變量賦值` 和 `類型別名的定義`，在此之前，開發者通常透過簡單的賦值來建立類型別名。

3. 使用類型別名有助於在重用同一類型定義，當需要修改類型時，只需在一處進行更改，避免重複類型定義的錯誤和不一致。

<br>

## 範例

1. 定義類型別名：以下程式碼建立了一個名為 `Vector` 的類型別名，它與 `list[float]` 等效，這表示 `Vector` 可以用來表示一個浮點數列表。

    ```python
    # 使用 `type` 語句建立類型別名
    type Vector = list[float]
    ```

<br>

2. 類型別名可以被用於函數定義中，以提高程式碼的清晰度和維護性；在以下程式碼中， `scale` 函數使用 `Vector` 來指定參數和返回類型，這使得函數更易於理解和維護，尤其是在涉及複雜數據結構或在多處使用相同類型的情況下。

    ```python
    # 使用類型別名
    def scale(scalar: float, vector: Vector) -> Vector:
        return [scalar * num for num in vector]

    new_vector = scale(2.0, [1.0, -4.2, 5.4])
    ```

<br>

3. 簡化複雜的類型聲明：在以下範例中，`Server` 類型別名簡化了 `broadcast_message` 函數的參數類型，相比之下，如果不使用類型別名，類型聲明會顯得非常冗長且難以閱讀。

    ```python
    from collections.abc import Sequence
    from typing import TypeAlias

    type ConnectionOptions = dict[str, str]
    type Address = tuple[str, int]
    type Server = tuple[Address, ConnectionOptions]

    # 簡化的函數
    def broadcast_message(message: str, servers: Sequence[Server]) -> None:
        ...
    # 未使用類型別名時的參數相對複雜
    def broadcast_message_explicit(
            message: str,
            servers: Sequence[tuple[tuple[str, int], dict[str, str]]]) -> None:
        ...
    ```

<br>

___

_END_
