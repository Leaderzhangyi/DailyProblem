#
# @lc app=leetcode.cn id=598 lang=python3
#
# [598] 范围求和 II
#

from typing import List
# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        Mininterval = [40001,40001]
        if len(ops) == 0:
            return m * n 
        for item in ops:
            if Mininterval[0] >= item[0]:
                Mininterval[0] = item[0]
            if Mininterval[1] >= item[1]:
                Mininterval[1] = item[1]
        return Mininterval[0] * Mininterval[1]

# @lc code=end

print(Solution().maxCount( m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]))