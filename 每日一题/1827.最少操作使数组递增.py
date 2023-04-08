#
# @lc app=leetcode.cn id=1827 lang=python3
#
# [1827] 最少操作使数组递增
#

from typing import List 
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0 
        if len(nums) == 1:
            return res 
        for i in range(1,len(nums)):
          #  print("res = ",nums)
            if nums[i] > nums[i - 1]:
                continue
            else:
                diff = abs(nums[i] - nums[i - 1]) + 1
                res += diff
                nums[i] += diff
        return res 

# @lc code=end

print(Solution().minOperations([1,1,1]))