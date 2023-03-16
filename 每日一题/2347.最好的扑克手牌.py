#
# @lc app=leetcode.cn id=2347 lang=python3
#
# [2347] 最好的扑克手牌
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return 'Flush'

        counter = Counter(ranks)

        if len(counter) == 5:
            return 'High Card'
        
        if any(cnt >= 3 for cnt in counter.values()):
            return 'Three of a Kind'

        return 'Pair'
# @lc code=end

