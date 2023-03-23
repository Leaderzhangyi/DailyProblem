#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        A,B = 1,0
        while n:
            tmp = n % 10
            B += tmp
            A *= tmp
            n //= 10
        #print(A,B)
        return A - B
# @lc code=end

