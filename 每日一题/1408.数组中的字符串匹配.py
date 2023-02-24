#
# @lc app=leetcode.cn id=1408 lang=python3
#
# [1408] 数组中的字符串匹配
#
from typing import List

# @lc code=start
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return list(set([a for a in words for b in words if a!=b and a in b]))

# @lc code=end

