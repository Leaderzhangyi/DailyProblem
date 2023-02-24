#
# @lc app=leetcode.cn id=888 lang=python3
#
# [888] 公平的糖果交换
#
from typing import List
# @lc code=start
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA, sumB = sum(aliceSizes), sum(bobSizes)
        delta = (sumA - sumB) // 2
        rec = set(aliceSizes)
        ans = None
        for y in bobSizes:
            x = y + delta
            if x in rec:
                ans = [x, y]
                break
        return ans
# @lc code=end

