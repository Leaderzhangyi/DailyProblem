#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        flag = 0
        res = []
        for elem in s:
            if elem == "(":
                if flag > 0:
                    res.append(elem)
                flag += 1
            elif elem == ")":
                flag -= 1
                if flag > 0:
                    res.append(elem)
        return "".join(res) 
        
# @lc code=end

res = Solution().removeOuterParentheses(s = "(()())(())(()(()))")
print(res)