#
# @lc app=leetcode.cn id=1446 lang=python3
#
# [1446] 连续字符
#


# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        i,j = 0,1
        res = 1
        tmp = -1
        while j < len(s):
            if s[i] == s[j]:
                j += 1
                res += 1

            elif s[i] != s[j]:
                if tmp < res:
                    tmp = res
                res = 1
                i = j 
                j += 1
        return max(res,tmp)
# @lc code=end

print(Solution().maxPower(s = "cc"))