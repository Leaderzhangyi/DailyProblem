#
# @lc app=leetcode.cn id=1768 lang=python3
#
# [1768] 交替合并字符串
#

# @lc code=start
from itertools import zip_longest
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        for x, y in zip_longest(word1, word2):
            print(x,y)
            if x: ans.append(x)
            if y: ans.append(y)
        return ''.join(ans)
# @lc code=end

Solution().mergeAlternately(word1 = "abcd", word2 = "pq")
