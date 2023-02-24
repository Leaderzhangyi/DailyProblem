#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#
from typing import List
# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        return nums

# @lc code=end

print(Solution().maximumProduct(nums = [1,2,3]))