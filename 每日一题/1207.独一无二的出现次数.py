#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#
from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(Counter(arr)) == len(set(Counter(arr).values()))
# @lc code=end

print(Solution().uniqueOccurrences([1,2,2,1,1,3]))