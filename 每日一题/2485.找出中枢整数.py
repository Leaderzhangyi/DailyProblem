#
# @lc app=leetcode.cn id=2485 lang=python3
#
# [2485] 找出中枢整数
#

# @lc code=start
class Solution:
    def pivotInteger(self, n: int) -> int:
        m = n * (n + 1) // 2
        x = int(m ** 0.5)
        return x if x * x == m else -1


# @lc code=end

