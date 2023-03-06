#
# @lc app=leetcode.cn id=1694 lang=python3
#
# [1694] 重新格式化电话号码
#

# @lc code=start
class Solution:
    def reformatNumber(self, number: str) -> str:
        n = number.replace(' ', '')
        n = n.replace('-', '')
        n = [n[i : min(len(n), i + 3)] for i in range(0, len(n), 3)]
        n = '-'.join(n)
        if n[-2] == '-':
            n = n[:-3] + '-' + n[-3] + n[-1]
        return n

# @lc code=end

