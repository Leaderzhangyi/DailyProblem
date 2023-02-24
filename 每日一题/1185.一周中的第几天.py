#
# @lc app=leetcode.cn id=1185 lang=python3
#
# [1185] 一周中的第几天
#

# @lc code=start
import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        tmp = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
        t = datetime.date(year,month,day)
        return tmp[t.weekday()]
# @lc code=end

print(Solution().dayOfTheWeek(day = 31, month = 8, year = 2019))
