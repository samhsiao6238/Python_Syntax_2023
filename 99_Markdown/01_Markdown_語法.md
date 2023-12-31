# Markdown 語法彙整

## 1. 表格

*在 Jupyter 的 Markdown 單元中繪製表格可以直接使用 Markdown 語法。*

| 頭部1  | 頭部2  |
|-------|--------|
| 資料1  | 資料2  |
| 資料3  | 資料4  |

## 2. 插入圖片

![替代文字](image.png)

## 3. 創建超連結

[連結 Google](https://www.google.com/)


## 4. 插入程式碼塊

```python
print('Hello, World!')
```

## 5. **創建數學公式**

*Jupyter 的 Markdown 支持 LaTeX 數學公式。你可以使用兩個美元符號來創建一個獨立的公式。*

### 5.1
    ```
    $$
    f(x) = x^2
    $$
    ```
### 5.2
這是一個行內公式：\($e^{i\pi}$ + 1 = 0\)

### 5.3
- 或是
    ```
    $$
    e^{i\pi} + 1 = 0
    $$
    ```

### 5.4
- 或者使用一個美元符號來創建內嵌的公式，在左右兩邊加上「$」

    ```
    $x^2$
    ```

    *假如要忽略「$」或「&&」要加上「```markdown」裝飾字*




## 6. 創建列表

    *可以使用星號、加號或是短橫線來創建無序列表，而創建有序列表則直接使用數字後面接上點號。*

- 列表項目1
- 列表項目2
- 列表項目3




## 7. 創建待辦列表

- [ ] 待辦事項1
- [x] 已完成事項1

## 8. 插入 HTML

    Markdown 也支持直接插入 HTML。
    
- *假如在 .ipynb 中運行*
    ```
    <div style="color: red">這是紅色文字。</div>
    ```

## 9. 縮排

&nbsp;&nbsp;(1)這是一段縮排的文字。

<blockquote>
(2)這是一段縮排的文字。
</blockquote>


> (3)這是一段縮排的文字。


<p style="margin-left: 40px;">
(4)這是一段縮排的文字。
</p>

---

END
