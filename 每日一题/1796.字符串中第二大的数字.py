#
# @lc app=leetcode.cn id=1796 lang=python3
#
# [1796] 字符串中第二大的数字
#

# @lc code=start
class Solution:
    def secondHighest(self, s: str) -> int:
        res = set([int(ch) for ch in s if "0" <= ch <= "9"])
        

        if len(res) in [0,1]:
            return -1
        res = sorted(res)
       # print(res)
        return res[-2]
# @lc code=end

print(Solution().secondHighest(s = "sjhtz8344"))