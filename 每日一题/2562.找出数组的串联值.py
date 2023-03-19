#
# @lc app=leetcode.cn id=2562 lang=python3
#
# [2562] 找出数组的串联值
#
from typing import List
# @lc code=start
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0
        i,j = 0,len(nums) - 1
        while i <= j:
            if i == j:
                tmp = str(nums[i]) 
            else:
                tmp = str(nums[i]) + str(nums[j])
          #  print(f"tmp = {tmp}")
            res += int(tmp)
            i += 1
            j -= 1

        return res 

# @lc code=end


print(Solution().findTheArrayConcVal(nums = [5,14,13,8,12]))
