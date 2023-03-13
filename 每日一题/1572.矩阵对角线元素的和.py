#
# @lc app=leetcode.cn id=1572 lang=python3
#
# [1572] 矩阵对角线元素的和
#
from typing import List
# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        flag = 0
        res = 0
        if n & 1 : #奇数
            flag = n // 2
            res -= mat[flag][flag]
        for i,item in enumerate(mat):
            tmp = item[i] + item[n - 1 - i]
            res += tmp 
    
        return res 
# @lc code=end


x = Solution().diagonalSum(mat = [[5]])
print(x)