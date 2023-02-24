#
# @lc app=leetcode.cn id=2441 lang=python3
#
# [2441] 与对应负数同时存在的最大正整数
#

# @lc code=start
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        i,j = 0,len(nums) - 1
        while i < j:
            if nums[i] + nums[j] > 0:
                j -= 1
            elif nums[i] + nums[j] < 0:
                i += 1
            else:
                return nums[j]
        return -1
# @lc code=end

