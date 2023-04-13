#
# @lc app=leetcode.cn id=1716 lang=python3
#
# [1716] 计算力扣银行的钱
#

# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7 
        rest = n % 7
        res = 0
        for i in range(1,weeks+1):
            tmp = ((i + i + 6)*7 ) // 2
            res += tmp 
        y = rest + weeks
        x = weeks + 1 
        res += ((x + y) * rest  ) // 2
        return res 
# @lc code=end

print(Solution().totalMoney(20))