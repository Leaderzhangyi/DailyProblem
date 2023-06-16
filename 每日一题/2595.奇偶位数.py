#
# @lc app=leetcode.cn id=2595 lang=python3
#
# [2595] 奇偶位数
#
from typing import List
# @lc code=start
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        odd = 0
        even = 0
        for index,ch in enumerate(bin(n)[2:][::-1]):
            if index % 2 == 0 and ch == '1':
                even += 1
            elif index % 2 != 0 and ch == '1':
                odd += 1
        return [even,odd]

# @lc code=end



res = Solution().evenOddBit(2)
print(res)