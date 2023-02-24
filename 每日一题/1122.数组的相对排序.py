#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#
from typing import List
# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort(key=lambda x:arr2.index(x) if x in arr2 else x+len(arr2))
        return arr1
# @lc code=end


gg = Solution().relativeSortArray(arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6])
print(gg)