#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量

from typing import List
# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1:
            return stones[0]
        elif n == 2:
            return abs(stones[1] - stones[0])
        else:
            stones.sort()
            if stones[n - 3] == 0:
                return stones[n - 1] - stones[n - 2]
            stones[n - 1] = stones[n - 1] - stones[n - 2]
            stones[n - 2] = 0
            return self.lastStoneWeight(stones)
# @lc code=end

