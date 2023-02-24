#
# @lc app=leetcode.cn id=1450 lang=python3
#
# [1450] 在既定时间做作业的学生人数
#

# @lc code=start
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        for item in zip(startTime,endTime):

            if item[0] <= queryTime <= item[1]:
                res += 1
        return res 
# @lc code=end

