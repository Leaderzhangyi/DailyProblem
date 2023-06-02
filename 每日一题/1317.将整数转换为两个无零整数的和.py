#
# @lc app=leetcode.cn id=1317 lang=python3
#
# [1317] 将整数转换为两个无零整数的和
#
from typing import List
# @lc code=start
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        res = []
        flag = 0
        new = n
        while True:
            new = new - 1
            flag += 1 
            if str(new).count('0') == 0 and str(flag).count('0') == 0:
                res.append(flag),res.append(new)
                break
        return res 
# @lc code=end


print(Solution().getNoZeroIntegers(n = 4102))