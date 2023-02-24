#
# @lc app=leetcode.cn id=1266 lang=python3
#
# [1266] 访问所有点的最小时间
#
from typing import List
# @lc code=start
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        for i in range(n-1):
            Xdiff = abs(points[i+1][0] - points[i][0])
            Ydiff = abs(points[i+1][1] - points[i][1])
            res += max(Xdiff,Ydiff)
        return res 

print(Solution().minTimeToVisitAllPoints(points = [[3,2],[-2,2]]))            

# @lc code=end

