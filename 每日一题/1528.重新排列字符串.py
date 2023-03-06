#
# @lc app=leetcode.cn id=1528 lang=python3
#
# [1528] 重新排列字符串
#
from typing import List
# @lc code=start
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ""
        tmp = [0 for _ in range(len(s))]
        for i,c in zip(indices,s):
            tmp[i] = c
        return "".join(tmp)

# @lc code=end

