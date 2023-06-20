#
# @lc app=leetcode.cn id=1844 lang=python3
#
# [1844] 将所有数字用字符替换
#

# @lc code=start
class Solution:
    def replaceDigits(self, s: str) -> str:
        res = []
        for i in range(1,len(s),2):
            op = chr(ord(s[i-1]) + int(s[i]))
            res.append(s[i-1])
            res.append(op)
        if len(s) & 1:
            res.append(s[-1])
        return "".join(res)
            

# @lc code=end


print(Solution().replaceDigits(s = "a1b2c3d4e"))