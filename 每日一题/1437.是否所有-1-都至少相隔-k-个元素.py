#
# @lc app=leetcode.cn id=1437 lang=python3
#
# [1437] 

#

from typing import List
# @lc code=start


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        for i,val in enumerate(nums):
            if val == 1:
                for value in nums[i + 1:i+k +1]:
                    if value == 1:
                        return False
        return True

# @lc code=end
