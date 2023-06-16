#
# @lc app=leetcode.cn id=1758 lang=python3
#
# [1758] 生成交替二进制字符串的最少操作数
#

# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        res = 0
        for index,v in enumerate(s):
            if int(v) == index % 2:
                res += 1
        return min(res,len(s) - res)

# @lc code=end

