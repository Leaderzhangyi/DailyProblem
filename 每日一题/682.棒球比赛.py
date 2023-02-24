#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#
from typing import List
# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for item in operations:
            if item == "+":
                a = stack[-1]
                b = stack[-2]
                stack.append(a+b)
            elif item == "D":
                stack.append(stack[-1]*2)
            elif item == "C":
                stack.pop()
            else:
                stack.append(int(item))
            #print(stack)
        
        return sum(stack)
# @lc code=end


print(Solution().calPoints(operations = ["5","2","C","D","+"]))
