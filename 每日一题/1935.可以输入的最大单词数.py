#
# @lc app=leetcode.cn id=1935 lang=python3
#
# [1935] 可以输入的最大单词数
#

# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        n = len(words)
        for word in words:
            tmp = set(word)
            for elem in brokenLetters:
                #print(set(word))
                if elem in tmp:
                    n -= 1
                    break
        return n 

# @lc code=end

print(Solution().canBeTypedWords("leet code","lt"))