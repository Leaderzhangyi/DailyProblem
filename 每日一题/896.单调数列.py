#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        i,j = 0,1
        flag = None
        while j < len(nums):
            if nums[i] < nums[j] and flag != False:
                flag = True # 标记为递增
                i = j
                j += 1
            elif nums[i] > nums[j] and flag != True:
                flag = False
                i = j
                j += 1
            elif nums[i] == nums[j]:
                i = j
                j += 1
            else:
                return False

        return True
# @lc code=end

