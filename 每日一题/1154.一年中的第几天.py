#
# @lc app=leetcode.cn id=1154 lang=python3
#
# [1154] 一年中的第几天
#

# @lc code=start
class Solution:
    def dayOfYear(self, date: str) -> int:
        res = [31,29,31,30,31,30,31,31,30,31,30,31]
        rr = [31,28,31,30,31,30,31,31,30,31,30,31]
        year,month,day = map(int,date.split("-"))
        ans = sum(res[:month - 1]) + day
        if year % 4 != 0:
            ans = sum(rr[:month - 1]) + day
        elif year % 100 == 0:
            if year % 400 != 0:
                ans = sum(rr[:month - 1]) + day
        return ans            
# @lc code=end

