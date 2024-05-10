# Walrus 運算子 

_`:=`，Assignment Expressions，海象運算子_

<br>

## 說明

1. `Python 3.8` 引入了 `Walrus 運算子`，官方稱為 `Assignment Expressions`，中文翻譯為 `海象運算子`，表示法為 `:=`，是一個新的語法特性。

<br>

2. 可在條件表達式內部執行賦值運算並傳出賦值結果，這對於在條件表達式中避免重複計算特別有用。

<br>

## 範例一

1. 程式碼：Walrus 運算子 `:=` 允許在 `列表推導式` 中 `直接生成並檢查隨機數`，選出大於 50 的數，如此每次迭代只調用一次 `random.randint(0, 100)`，提高了效率。

     ```python
     # 使用 Walrus 運算子在 list comprehension 中直接賦值和檢查
     import random
     print([n for _ in range(10) if (n := random.randint(0, 100)) > 50])
     ```

<br>

2. 程式碼：同樣使用Walrus 運算子 `:=` 在列表推導式中 `直接生成並檢查 x 是否大於 0`。

     ```python
     # 假設要在一個列表中找到第一個大於零的元素並傳回其平方值
     numbers = [0, -1, 2, -3, 4]
     squared = None

     # 語法：next(iterator, default)
     # next() 會嘗試從生成器或許下一個元素，如果沒有更多元素，也就是之前的元素都不滿足或列表為空，則返回預設值 None
     # next() 找到第一個滿足條件的元素後把值賦給 `n`，如此可避免二次計算或額外的查找呼叫。
     # 透過 is not None 來判斷當沒找到而是 None 的時候，條件判斷將不會進入區塊中
     if (n := next((x for x in numbers if x > 0), None)) is not None:
          squared = n ** 2
     print(squared)
     ```

<br>

3. 程式碼：在 `Streamlit` 中時常用到建立一個文字輸入框，並且捕獲用戶的輸入，假如用戶輸入非空格，函數便會傳輸出入的內容，並賦值給指定的變數。 

     ```python
     # `What is up?` 是指輸入框的預設文字，傳出的值是用戶的輸入
     if prompt := st.chat_input("What is up?"):
     write_message("user", prompt)
     handle_submit(prompt)
     ```

<br>

___

_END_