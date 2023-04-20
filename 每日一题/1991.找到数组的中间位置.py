#
# @lc app=leetcode.cn id=1991 lang=python3
#
# [1991] 找到数组的中间位置
#

from typing import List
# @lc code=start
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
           # print(sum(nums[:i]),sum(nums[i+1:]))
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i 
        return -1
            

# @lc code=end


print(Solution().findMiddleIndex(nums = [2,3,-1,8,4]))
