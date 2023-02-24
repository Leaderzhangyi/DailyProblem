#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#
from typing import List
# @lc code=start
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_index = []
        res = []
        for index,cr in enumerate(s):
            if cr == c:
                c_index.append(index)

        for index,cr in enumerate(s):
            tmp = min([abs(i-index) for i in c_index])
            res.append(tmp)
        
        return res 
# @lc code=end

