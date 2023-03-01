#
# @lc app=leetcode.cn id=1961 lang=python3
#
# [1961] 检查字符串是否为数组前缀
#

# @lc code=start
from itertools import accumulate
from typing import List
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        return True if s in accumulate(words) else False

        
# @lc code=end

