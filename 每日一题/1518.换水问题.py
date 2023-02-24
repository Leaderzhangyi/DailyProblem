#
# @lc app=leetcode.cn id=1518 lang=python3
#
# [1518] 换水问题
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        etive = numBottles
        empty = numBottles
        res = etive
        while etive:
            etive = empty // numExchange
            empty = empty % numExchange + etive
            res += etive
         #   print(f"换了{etive}瓶")
        return res
# @lc code=end

print(Solution().numWaterBottles(numBottles = 15, numExchange = 4))