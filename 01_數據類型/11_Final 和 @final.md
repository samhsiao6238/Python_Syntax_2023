# Final 和 @final

<br>

## 說明

1. `Final` 可用來標記變數或類型成員不應被更改或繼承。

2. `@final` 裝飾器用來指示子類不應覆。

<br>

## 範例

1. 程式碼。

    ```python
    from typing import Final, final

    RATE: Final = 0.05

    @final
    class Base:
        def done(self) -> None:
            print("No override please")

    class Derived(Base):
        def done(self) -> None:  # 這將引發錯誤
            print("Trying to override")
    ```

<br>

___

_END_