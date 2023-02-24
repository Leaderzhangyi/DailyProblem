#
# @lc app=leetcode.cn id=1588 lang=python3
#
# [1588] 所有奇数长度子数组的和
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        arrlen = len(arr)
        res = 0
        for step in range(1,arrlen+1,2):
            for j in range(0,arrlen + 1 - step):
                res += sum(arr[j:j+step])
        return res
# @lc code=end

