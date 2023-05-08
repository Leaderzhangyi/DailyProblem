#
# @lc app=leetcode.cn id=2582 lang=python3
#
# [2582] 递枕头
#

# @lc code=start
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        k, t = divmod(time, n - 1)
        return n - t if k % 2 else 1 + t


# @lc code=end

print(Solution().passThePillow(n = 3,time = 6))