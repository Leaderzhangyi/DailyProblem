#
# @lc app=leetcode.cn id=804 lang=python3
#
# [804] 唯一摩尔斯密码词
#

# @lc code=start
from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        passwords = dict(zip([chr(i) for i in range(97,124)],[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]))
        return len(set(["".join([passwords[ch] for ch in word]) for word in words]))
# @lc code=end

