#
# @lc app=leetcode.cn id=1967 lang=python3
#
# [1967] 作为子字符串出现在单词中的字符串数目
#
from typing import List
# @lc code=start
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(1 for item in patterns if item in word)
# @lc code=end

