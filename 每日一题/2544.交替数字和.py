#
# @lc app=leetcode.cn id=2544 lang=python3
#
# [2544] 交替数字和
#

# @lc code=start
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        return sum([int(i) for i in list(str(n))]) - sum(([0] + [int(i) for i in list(str(n))])[::2]) * 2
# @lc code=end

