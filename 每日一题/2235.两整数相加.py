#
# @lc app=leetcode.cn id=2235 lang=python3
#
# [2235] 两整数相加
#

# @lc code=start
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        for i in range(-200,201):
            if i - num1 == num2:
                return i 
        
# @lc code=end

