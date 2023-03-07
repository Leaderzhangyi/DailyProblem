#
# @lc app=leetcode.cn id=2094 lang=python3
#
# [2094] 找出 3 位偶数
#
from typing import List


# @lc code=start
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        nums = set()   # 目标偶数集合
        n = len(digits)
        # 遍历三个数位的下标
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    # 判断是否满足目标偶数的条件
                    if i == j or j == k or i == k:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num >= 100 and num % 2 == 0:
                        nums.add(num)
        # 转化为升序排序的数组
        res = sorted(list(nums))
        return res
# @lc code=end