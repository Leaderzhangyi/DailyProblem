#
# @lc app=leetcode.cn id=1051 lang=python3
#
# [1051] 高度检查器
#
from typing import List

# @lc code=start
import copy
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        old = heights.copy()
        heights.sort()
        new = heights
       # print(old,new)
        return sum([1 for i,j in zip(old,new) if i != j])
        
# @lc code=end

print(Solution().heightChecker(heights = [1,1,4,2,1,3]))
