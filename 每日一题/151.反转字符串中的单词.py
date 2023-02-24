#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        sl = s.strip().split(" ")
        print(sl)
        sl = [elem for elem in sl if elem != ""]
        sl.reverse()
        return " ".join(sl)

# @lc code=end

print(Solution().reverseWords("a good   example"))
