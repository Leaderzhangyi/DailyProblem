#
# @lc app=leetcode.cn id=1221 lang=python3
#
# [1221] 分割平衡字符串
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        flag = 0
        res = 0
        for ch in s:
            if ch == "R":
                flag += 1
            else:
                flag -= 1
            
            if flag == 0:
                res += 1
        return res 
# @lc code=end

