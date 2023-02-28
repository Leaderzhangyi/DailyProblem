#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        a,b,c = 0,1,1
        nums = [0,1,1]
        for i in range(3,38):
            tmp = nums[i-3] + nums[i-2] + nums[i-1]
            nums.append(tmp)

        return nums[n]


# @lc code=end

