#
# @lc app=leetcode.cn id=1732 lang=python3
#
# [1732] 找到最高海拔
#

from typing import List
# @lc code=start
from itertools import accumulate
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = list(accumulate(gain))
        #print(max([0]+res))
        return max([0]+res)
            

# @lc code=end

Solution().largestAltitude(gain = [-5,1,5,0,-7])