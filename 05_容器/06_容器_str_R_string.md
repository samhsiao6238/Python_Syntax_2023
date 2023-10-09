# r-string

- 在 Python 中，可以使用 r-string (raw string) 來表示檔案路徑。
- 若在字串前加上 'r' 或 'R'，Python 會將這個字串視為原始字串，並不會將其內部的反斜線 \ 當作轉義字符處理。
- 這在處理檔案路徑時很有用，尤其是在 Windows 系統中，因為 Windows 的檔案路徑使用的是反斜線 \。

## 1. windows

- 在此範例中，r 告訴 Python 將字串作為 *原始字串 *來處理，因此，反斜線 \ 不會被視為轉義字符。


```python
filepath = r'C:\Users\Username\Documents\file.txt'
print(filepath)
```
*輸出結果*
```
    C:\Users\Username\Documents\file.txt
```

## 2. MacOS/Linux 

- 在 MacOS 和 Linux 中，檔案路徑使用正斜線 /，所以不需要使用 r-string。


```python
filepath = '/Users/username/Documents/file.txt'
```

## 3. 跨平台

- 在跨平台的狀況下，可以使用 os 模組的 os.path.join() 函數來組合檔案路徑。
- os.path.join() 函數會根據作業系統選擇正確的路徑分隔符號，因此在 Windows 中會使用反斜線 \，而在 MacOS/Linux 中會使用正斜線 /。


```python
import os

filepath = os.path.join('Users', 'username', 'Documents', 'file.txt')
print(filepath)  # 在 Windows 中將輸出 'Users\username\Documents\file.txt'，在 MacOS/Linux 中將輸出 'Users/username/Documents/file.txt'
```
*輸出結果*
```
    Users/username/Documents/file.txt
```

---

END
