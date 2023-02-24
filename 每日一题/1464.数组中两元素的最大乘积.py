#
# @lc app=leetcode.cn id=1464 lang=python3
#
# [1464] 数组中两元素的最大乘积
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = max(nums)
        nums.remove(a)
        b = max(nums)
        return a*b + 1 -a -b 
# @lc code=end

