#
# @lc app=leetcode.cn id=1748 lang=python3
#
# [1748] 唯一元素的和
#
from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = Counter(nums)
        res = 0
        #print(ans)
        for (k,v) in ans.items():
            if v == 1:
                res += k
        return res 
# @lc code=end

print(Solution().sumOfUnique(nums = [1,2,3,2]))

