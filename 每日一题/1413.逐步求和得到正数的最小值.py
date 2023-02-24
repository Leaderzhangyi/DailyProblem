#
# @lc app=leetcode.cn id=1413 lang=python3
#
# [1413] 逐步求和得到正数的最小值
#
from typing import List

# @lc code=start
from itertools import accumulate
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        return max(-min(accumulate(nums)),0) + 1
        

# @lc code=end

print(Solution().minStartValue(nums = [-3,2,-3,4,2]))