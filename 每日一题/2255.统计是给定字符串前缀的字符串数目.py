#
# @lc app=leetcode.cn id=2255 lang=python3
#
# [2255] 统计是给定字符串前缀的字符串数目
#
from typing import List
# @lc code=start
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum([1 for word in words if word == s[:len(word)]])

# @lc code=end

x=Solution().countPrefixes(words = ["a","b","c","ab","bc","abc"], s = "abc")
print(x)