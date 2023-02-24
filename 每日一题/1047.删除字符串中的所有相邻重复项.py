#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ss in s:
            if len(stack) and stack[-1] == ss:
                stack.pop()
            else:
                stack.append(ss)
        return "".join(stack)
# @lc code=end

print(Solution().removeDuplicates("aababaab"))