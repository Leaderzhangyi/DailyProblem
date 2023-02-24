#
# @lc app=leetcode.cn id=1337 lang=python3
#
# [1337] 矩阵中战斗力最弱的 K 行
#
from typing import List
# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = {}
        for id,item in enumerate(mat):
            res[id] = sum(item)
        res = sorted(res.items(),key=lambda x:x[1])
        return [i[0] for i in res[:k]]
# @lc code=end


r = Solution().kWeakestRows(mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3)
print(r)