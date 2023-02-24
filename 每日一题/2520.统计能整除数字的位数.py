#
# @lc app=leetcode.cn id=2520 lang=python3
#
# [2520] 统计能整除数字的位数
#

# @lc code=start
class Solution:
    def countDigits(self, num: int) -> int:
        flag = 0
        tmp = list(map(int,list(str(num))))
        for i in tmp:
            if num % i == 0:
                flag += 1
        return flag
# @lc code=end

