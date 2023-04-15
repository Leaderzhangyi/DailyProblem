#
# @lc app=leetcode.cn id=1394 lang=python3
#
# [1394] 找出数组中的幸运数
#
from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        try:
            return max([item[0] for item in Counter(arr).items() if item[0]==item[1]])
        except:
            return -1

# @lc code=end

print(Solution().findLucky([2,2,2,3,3]))
