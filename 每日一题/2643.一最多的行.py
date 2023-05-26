#
# @lc app=leetcode.cn id=2643 lang=python3
#
# [2643] 一最多的行
#
from typing import List
# @lc code=start
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        Max_one = -1
        Min_index = 0
        for i,item in enumerate(mat):
            ones = item.count(1)
            if Max_one < ones:
                Max_one = ones
                Min_index = i 
        
        return [Min_index,Max_one]

            
# @lc code=end

print(Solution().rowAndMaximumOnes(mat = [[0,0],[1,1],[0,0]]
))