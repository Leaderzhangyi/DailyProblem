#
# @lc app=leetcode.cn id=1389 lang=python3
#
# [1389] 按既定顺序创建目标数组
#
from typing import List
# @lc code=start
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for num,i in zip(nums,index):
            res.insert(i,num)
        return res 
# @lc code=end

