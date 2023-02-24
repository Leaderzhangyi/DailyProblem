#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#
from typing import List
# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        nums.sort(reverse=True)
        i,j = 0,1
        flag = 1
       # print(nums)
        while j < len(nums):
    
            if nums[i] > nums[j]:
                flag += 1
                i = j
                j += 1
            elif nums[i] == nums[j]:
                j += 1

            if flag == 3:
                return nums[j-1]
        if flag < 3:
            return max(nums)
# @lc code=end

print(Solution().thirdMax([1,1,1,3]))