#
# @lc app=leetcode.cn id=1672 lang=python3
#
# [1672] 最富有客户的资产总量
#
from typing import List
# @lc code=start
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(item) for item in accounts])
# @lc code=end

