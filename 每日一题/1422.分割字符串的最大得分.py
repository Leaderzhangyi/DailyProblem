#
# @lc app=leetcode.cn id=1422 lang=python3
#
# [1422] 分割字符串的最大得分
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        Max = -1
        for i in range(len(s)-1):
            print(s[0:i+1],s[i+1:])
            tmp = s[0:i+1].count("0") + s[i+1:].count("1")
            if Max < tmp:
                Max = tmp
        return Max 
# @lc code=end


print(Solution().maxScore(s = "011101"))
