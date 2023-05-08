#
# @lc app=leetcode.cn id=2553 lang=python3
#
# [2553] 分割数组中数字的数位
#
from typing import List
# @lc code=start
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        #return [y for item in list(map(str,nums)) for y in list(map(int,list(item)))]
        return [d for x in nums for d in map(int, str(x))]

        
# @lc code=end

print(Solution().separateDigits(nums = [13,25,83,77]))