# 輸入字串


<br>

1. 透過鍵盤輸入

    ```python
    user_input = input("請輸入一些文字: ")
    print(f"你輸入了: {user_input}")
    ```
    *輸出結果*
    ```bash
    你輸入了: 123
    ```

<br>

2. 輸入同時轉型

    _獲取用戶輸入，並將其轉換為整數_

    ```python
    # 使用 `int` 將用戶輸入的字串轉型為整數
    user_input = int(input("請輸入一個整數："))
    # 對轉型後的整數進行運算
    user_input += 10
    print(f"你輸入的整數加上 10 等於 {user_input}。")
    ```
    _結果_
    ```bash
    你輸入的整數加上 10 等於 20。
    ```

    _獲取用戶輸入，並將其轉換為浮點數_

    ```python
    user_input = float(input("請輸入一個浮點數："))
    print(f"你輸入的浮點數加上 0.5 等於 {user_input + .5}。")
    ```
    _結果_
    ```bash
    你輸入的浮點數加上 0.5 等於 11.5。
    ```

<br>

---

_END_
