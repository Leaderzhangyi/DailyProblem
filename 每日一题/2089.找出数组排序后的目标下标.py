#
# @lc app=leetcode.cn id=2089 lang=python3
#
# [2089] 找出数组排序后的目标下标
#
from typing import List
# @lc code=start
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # lowB 写法
        # if target not in nums:
        #     return []
        # nums.sort()
        # return [i for i in range(len(nums)) if nums[i] == target]
        a,b = 0,0
        for num in nums:
            if num < target:
                a += 1
            elif num == target:
                b += 1
        return list(range(a,a+b))
# @lc code=end

Solution().targetIndices([1,2,5,2,3],target=3)