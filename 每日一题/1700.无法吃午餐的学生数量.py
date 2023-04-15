#
# @lc app=leetcode.cn id=1700 lang=python3
#
# [1700] 无法吃午餐的学生数量
#

# @lc code=start
from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        like0 = students.count(0)
        like1 = students.count(1)
        for san in sandwiches:
            if san == 0 and like0 > 0:
                like0 -= 1
            elif san == 1 and like1 > 0:
                like1 -= 1
            else:
                return like0 + like1
        return 0
     
# @lc code=end

print(Solution().countStudents(students = [0,0,0,1,1,1,1,0,0,0], sandwiches = [1,0,1,0,0,1,1,0,0,0]))
