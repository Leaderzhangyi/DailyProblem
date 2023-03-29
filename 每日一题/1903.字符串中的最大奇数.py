#
# @lc app=leetcode.cn id=1903 lang=python3
#
# [1903] 字符串中的最大奇数
#

# @lc code=start
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num))[::-1]:#从后往前遍历字符串，如果遇到的字符是奇数，证明其前面到该字符的数字值最大
            char2int=int(num[i])
            if char2int%2 != 0:
                return num[:i+1]
        return ''
# @lc code=end

