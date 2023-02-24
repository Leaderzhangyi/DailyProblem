#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
from typing import List
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        n = len(nums)
        for i in range(n - 1):
            far = max(far, i + nums[i])
            if far <= i:
                return False
        return far >= n - 1

# @lc code=end

