#
# @lc app=leetcode.cn id=1470 lang=python3
#
# [1470] 重新排列数组
#
from typing import List
# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        s = [nums[j] for i in range(n) for j in range(i,len(nums),n)]
        #print(s)
        return s 
# @lc code=end

print(Solution().shuffle(nums = [1,1,2,2], n = 2))