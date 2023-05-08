#
# @lc app=leetcode.cn id=1859 lang=python3
#
# [1859] 将句子排序
#

# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        sentences = s.split()
        sentences.sort(key=lambda x:x[-1])
        return " ".join([word[:-1] for word in sentences])
# @lc code=end

print(Solution().sortSentence(s = "is2 sentence4 This1 a3"))
