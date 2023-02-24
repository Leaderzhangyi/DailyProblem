#
# @lc app=leetcode.cn id=1941 lang=python3
#
# [1941] 检查是否所有字符出现次数相同
#

# @lc code=start
from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        letters = len(set(s))
        x = Counter(s)
        return max(x.values())*letters == len(s)
# @lc code=end

