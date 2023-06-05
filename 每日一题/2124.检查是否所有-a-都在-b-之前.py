#
# @lc app=leetcode.cn id=2124 lang=python3
#
# [2124] 检查是否所有 A 都在 B 之前
#

# @lc code=start
class Solution:
    def checkString(self, s: str) -> bool:
        b = s.find("b")
        a = s.rfind("a")
        if b == -1 or a == -1:
            return True

        return True if a<b else False
# @lc code=end

