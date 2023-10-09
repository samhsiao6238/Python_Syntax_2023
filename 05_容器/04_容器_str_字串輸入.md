# 透過鍵盤輸入


```python
user_input = input("請輸入一些文字: ")
print(f"你輸入了: {user_input}")
```
*輸出結果*
```
    你輸入了: 123
```

## 輸入同時轉型

### 獲取用戶輸入，並將其轉換為整數
```python
user_input = int(input("請輸入一個整數："))
user_input += 10
print(f"你輸入的整數加上 10 等於 {user_input}。")
```
```
你輸入的整數加上 10 等於 20。
```

### 獲取用戶輸入，並將其轉換為浮點數
```python
user_input = float(input("請輸入一個浮點數："))
print(f"你輸入的浮點數加上 0.5 等於 {user_input + .5}。")
```
```
    你輸入的浮點數加上 0.5 等於 11.5。
```

---END---
