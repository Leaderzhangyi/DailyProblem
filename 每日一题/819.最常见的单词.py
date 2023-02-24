#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#
from typing import List
# @lc code=start
from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        simple = '[’!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~，。,]'
        paragraph = re.sub(simple," ",paragraph)
        #print(paragraph)
        paragraph = paragraph.lower().split()
        word_nums = Counter(paragraph)
        #print(word_nums)
        for word,val in sorted(word_nums.items(),key=lambda x:x[1],reverse=True):
            if word not in banned:
                return word
# @lc code=end


print(Solution().mostCommonWord(paragraph = "a, a, a, a, b,b,b,c, c",
banned = ["a"]))