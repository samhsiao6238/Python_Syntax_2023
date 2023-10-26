_進階用法_

# 魔法方法 `__getitem__` 

<br>

## 說明

1. `__getitem__()` 是 Python 中的 `魔術方法`，用於覆寫當使用 `方括號` 取值時的行為。
2. 例如從一個列表或字典取值時，背後的實作就是 `__getitem__()` 方法。

</br>

## 實作/覆寫 `__getitem__`

1. 一個類實作了 `__getitem__()` 並不會因此讓它的實體成為迭代器。
2. 要使一個物件成為迭代器，必須實作 `__iter__()` 和 `__next__()` 方法。
3. 當自定義一個類並實作 `__getitem__()` 方法時，可以根據需求回傳相對應的值

</br>

### 範例

1. 範例

    ```python
    class SimpleClass:
        def __getitem__(self, index):
            return index

    # 創建實體
    obj = SimpleClass()

    # 使用 __getitem__ 方法
    print(obj[2]) 
    ```
    _OUTPUT_
    ```bash
    2 # 傳回索引值
    ```

</br>

<br>

## 使用 `__getitem__` 進行迭代

1. 當物件實作了 `__getitem__` 但沒有實作 `__iter__` 時，Python 會嘗試將其視為一個 `序列` 來進行迭代。

2. Python 會從 0 開始索引，直到遇到 `IndexError` 。

<br>

### 範例

1. 範例
    
    ```python
    class SequenceClass:
        data = [1, 2, 3, 4, 5]
        # 實作 __getitem__，傳回索引
        def __getitem__(self, index):
            return self.data[index]
        def __len__(self):
            return len(self.data)

    # 創建實體
    seq = SequenceClass()

    # 使用 for 迴圈進行迭代
    for item in seq:
        print(item)
    ```
    _輸出_
    ```bash
    1
    2
    3
    4
    5
    ```    
    
    _▶️ 輸出查看一下_
    ```python
    print(seq)
    ```
    _輸出_
    ```bash
    <__main__.SequenceClass object at 0x10436ec60>
    ```
    
    _▶️ 假如索引超出範圍_
    ```python
    # 輸出
    try:
        print(seq[10]) 
    except IndexError:
        print("IndexError: 索引超出範圍!")
    ```
    _輸出_
    ```bash
    IndexError: 索引超出範圍!
    ```


<br>

---

_END_