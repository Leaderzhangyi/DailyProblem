#
# @lc app=leetcode.cn id=1636 lang=python3
#
# [1636] 按照频率将数组升序排序
#
from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        res = []
        frequency = Counter(nums)
        frequency = sorted(frequency.items(),key=lambda x:(x[1],-x[0]))
        for item in frequency:
            for _ in range(item[1]):
                res.append(item[0])
        return res 

# @lc code=end

print(Solution().frequencySort(nums = [2,3,1,3,2]))

