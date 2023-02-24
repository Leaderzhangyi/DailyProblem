#
# @lc app=leetcode.cn id=830 lang=python3
#
# [830] 较大分组的位置
#
from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if len(s) < 3:
            return []
        st = 0
        ed = st + 1
        flag = 0
        stack = []
        while ed<len(s):
            if s[st] == s[ed]:
                while ed <len(s) and  s[st] == s[ed] :
                    ed += 1
                if (ed - st) >= 3:
                    stack.append([st,ed-1])
            else:
                st = ed 
                ed += 1
        return stack
# @lc code=end
res = Solution().largeGroupPositions(s = "aaa")
print(res)
