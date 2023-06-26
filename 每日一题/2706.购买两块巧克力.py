#
# @lc app=leetcode.cn id=2706 lang=python3
#
# [2706] 购买两块巧克力
#
from typing import List
# @lc code=start
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        ans = prices[0] + prices[1]
        if ans > money:
            return money
        else:
            return money - ans  
# @lc code=end

