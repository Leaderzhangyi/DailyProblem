#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#

# @lc code=start
from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = (s1 + " "+s2).split()
        words = Counter(words)
        
        #print([item[0] for item in words.items() if item[1] == 1])
        return [item[0] for item in words.items() if item[1] == 1]
# @lc code=end

