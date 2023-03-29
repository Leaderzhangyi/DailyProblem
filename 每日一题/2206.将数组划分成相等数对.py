#
# @lc app=leetcode.cn id=2206 lang=python3
#
# [2206] 将数组划分成相等数对
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
      #  print(list(cnt % 2 == 0 for _, cnt in Counter(nums).items()))
        return all(cnt&1 == 0 for _, cnt in Counter(nums).items())
# @lc code=end


Solution().divideArray(nums = [3,2,3,2,2,2])
