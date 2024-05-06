"""
這個腳本是提供給 mypy 測試使用
"""
from typing import List


def list_sum(numbers: List[int]) -> int:
    """返回列表中所有數字的和"""
    return sum(numbers)


# 正確的調用
result = list_sum([1, 2, 3])
print("Sum:", result)

# 包含類型錯誤的調用
# 會引起 MyPy 檢查錯誤，因為傳入的是字串而非整數列表
result2 = list_sum("hello")  
print("This call is incorrect:", result2)
