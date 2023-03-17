#
# @lc app=leetcode.cn id=2119 lang=python3
#
# [2119] 反转两次的数字
#

# @lc code=start
from typing import List
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # 老实人思路
        # tmp = str(num)[::-1]
        # if int(str(int(tmp))[::-1]) == num:
        #     return True
        # return False

        # 聪明人
        if len(str(num)) == 1:
            return True
        if str(num)[-1] == '0':
            return False
        return True


# @lc code=end

