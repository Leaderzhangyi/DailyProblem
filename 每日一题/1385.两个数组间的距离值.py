#
# @lc app=leetcode.cn id=1385 lang=python3
#
# [1385] 两个数组间的距离值
#

from typing import List
# @lc code=start
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        cnt=len(arr1)
        for i in arr1:
            for j in arr2:
                if abs(i-j)<=d:
                    cnt-=1
                    break
        return cnt  

# @lc code=end

