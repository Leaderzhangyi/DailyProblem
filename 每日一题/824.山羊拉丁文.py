#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#

# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(" ")
        for id,word in enumerate(words):
            if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                words[id] = word + "ma" + (id+1) * "a"
            else:
                words[id] = word[1:] + word[0] + "ma" + (id+1) * "a"

        return " ".join(words)
# @lc code=end

