#
# @lc app=leetcode.cn id=1550 lang=python3
#
# [1550] 存在连续三个奇数的数组
#
from typing import List
# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)-2):
            if arr[i] & 1 and arr[i+1] & 1 and arr[i+2] & 1:
                return True

        return False


# @lc code=end

