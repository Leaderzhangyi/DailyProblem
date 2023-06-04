#
# @lc app=leetcode.cn id=942 lang=python3
#
# [942] 增减字符串匹配
#
from typing import List
# @lc code=start
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        i,j = 0,n
        k = 0
        res = []
        while k < n:
            if s[k] == "I":
                res.append(i)
                i += 1
            else:
                res.append(j)
                j -= 1 
            k += 1 
        res.append(i)
        return res 
# @lc code=end


res = Solution().diStringMatch(s = "IIII")
print(res)