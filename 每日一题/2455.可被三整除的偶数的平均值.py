#
# @lc app=leetcode.cn id=2455 lang=python3
#
# [2455] 可被三整除的偶数的平均值
#
from typing import List
# @lc code=start
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        def isEven(x):
            if not x & 1:
                if not x % 3:
                    return True
        res = list(filter(isEven,nums))
        if len(res) == 0:
            return 0
        else:
            return sum(res)//len(res) 
            
# @lc code=end
print(Solution().averageValue(nums = [1,2,4,7,10]))




