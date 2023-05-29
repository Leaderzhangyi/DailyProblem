#
# @lc app=leetcode.cn id=2164 lang=python3
#
# [2164] 对奇偶下标分别排序
#
from typing import List
# @lc code=start
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
       # print(sorted(nums[::2]))
        nums[::2] = sorted(nums[::2])
        nums[1::2] = sorted(nums[1::2],reverse=True)
        #print(nums)
        return nums
                           

# @lc code=end


print(Solution().sortEvenOdd(nums = [4,1,2,3]))