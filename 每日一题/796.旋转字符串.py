#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        n = len(s)
        for _ in range(n):
            tmp = s[1:] + s[0]
            if tmp == goal:
                return True
            s = tmp 
        return False
# @lc code=end

