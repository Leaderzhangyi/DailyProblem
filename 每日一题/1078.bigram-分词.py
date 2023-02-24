#
# @lc app=leetcode.cn id=1078 lang=python3
#
# [1078] Bigram 分词
#
from typing import List
# @lc code=start
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        _f = text.split(" ")
        res = [_f[i+2] for i in range(len(_f)-2) if _f[i] == first and _f[i+1]==second]
        return res 
                
        
# @lc code=end

x = Solution().findOcurrences(text = "we will we will rock you", first = "we", second = "will")
print(x)

