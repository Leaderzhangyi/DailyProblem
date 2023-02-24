#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if guess(mid) <= 0:
                right = mid   # 答案在区间 [left, mid] 中
            else:
                left = mid + 1   # 答案在区间 [mid+1, right] 中
        
        # 此时有 left == right，区间缩为一个点，即为答案
        return left

# @lc code=end

