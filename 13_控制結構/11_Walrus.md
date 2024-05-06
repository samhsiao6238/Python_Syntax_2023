# Walrus 運算子 

_`:=`_

## 說明

1. Python 3.8 引入了 `Walrus 運算子`，表示法為 `:=`，可在條件表達式內部執行賦值運算，這對於在條件表達式中避免重複計算特別有用。

```python
# 假設要在一個列表中找到第一個大於零的元素並傳回其平方值
numbers = [0, -1, 2, -3, 4]
squared = None

# `next()` 函數嘗試找到第一個滿足條件的元素，而這個值會被賦給 `n`，避免了二次計算或額外的查找呼叫。
if (n := next((x for x in numbers if x > 0), None)) is not None:
     squared = n ** 2
print(squared)
```

