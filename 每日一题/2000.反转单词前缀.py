#
# @lc app=leetcode.cn id=2000 lang=python3
#
# [2000] 反转单词前缀
#

# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # print(word.find(ch))
        # print(word[:word.find(ch)+1][::-1])
        return word[:word.find(ch)+1][::-1] + word[word.find(ch)+1:]
# @lc code=end

print(Solution().reversePrefix(word = "abcdefd", ch = "d"))