#
# @lc app=leetcode.cn id=1486 lang=python3
#
# [1486] 数组异或操作
#

# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        tmp = [start + 2*i for i in range(n)]
        res = 0
        for i in tmp:
            res ^= i 
        return res 
# @lc code=end

