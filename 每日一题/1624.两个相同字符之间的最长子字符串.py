#
# @lc app=leetcode.cn id=1624 lang=python3
#
# [1624] 两个相同字符之间的最长子字符串
#


# @lc code=start
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max = -500
        for index,cr in enumerate(s):
            tmp = s.rfind(cr)
            if tmp != -1:
                ans = tmp - index - 1
                if max < ans:
                    max = ans
        if max < 0:
            return -1
        else:
            return max                    


# @lc code=end

print(Solution().maxLengthBetweenEqualCharacters(s = "cbzcy"))