#
# @lc app=leetcode.cn id=2103 lang=python3
#
# [2103] 环和杆
#

# @lc code=start
from collections import defaultdict
class Solution:
    def countPoints(self, rings: str) -> int:
        if len(rings) < 6:
            return 0
        res = {}
        for i in range(1,len(rings),2):
            res.setdefault(rings[i],[]).append(rings[i - 1])
        return len([1 for v in res.values() if len(set(v)) == 3])

# @lc code=end
print(Solution().countPoints(rings = "B0B6G0R6R0R6G9"))
