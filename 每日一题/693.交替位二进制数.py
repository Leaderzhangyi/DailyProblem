#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return not ('11' in str(bin(n)) or '00' in str(bin(n)))
# @lc code=end

