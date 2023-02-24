#
# @lc app=leetcode.cn id=1380 lang=python3
#
# [1380] 矩阵中的幸运数
#

# @lc code=start
from typing import List
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row = [min(i) for i in matrix]
        col = [max(i) for i in zip(*matrix)]
        return [i for i in row if i in col]
# @lc code=end

print(Solution().luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
