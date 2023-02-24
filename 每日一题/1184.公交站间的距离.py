#
# @lc app=leetcode.cn id=1184 lang=python3
#
# [1184] 公交站间的距离
#
from typing import List
# @lc code=start
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s = min(start,destination)
        d = max(start,destination)
        d1,d2=0,0
        for i in range(len(distance)):
            if i >= s and i < d:
                d1 += distance[i]
            else:
                d2 += distance[i]
        return d1 if d1 < d2 else d2
# @lc code=end

 
print(Solution().distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 3))