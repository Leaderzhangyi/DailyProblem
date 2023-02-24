#
# @lc app=leetcode.cn id=1342 lang=python3
#
# [1342] 将数字变成 0 的操作次数
#

# @lc code=start
class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num != 0:
            res += 1
            if num & 1:
                num -= 1
            else:
                num //= 2
        return res
# @lc code=end

