#
# @lc app=leetcode.cn id=1025 lang=python3
#
# [1025] 除数博弈
#

# @lc code=start
class Solution:
    def divisorGame(self, n: int) -> bool:
        return False if n & 1  else True
# @lc code=end

