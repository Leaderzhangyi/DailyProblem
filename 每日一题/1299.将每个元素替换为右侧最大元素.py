#
# @lc app=leetcode.cn id=1299 lang=python3
#
# [1299] 将每个元素替换为右侧最大元素
#
from typing import List
# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        tmp  = -1
        res = [-1]*len(arr)
       # print(list(reversed(range(len(arr)-1))))
        for i in reversed(range(len(arr)-1)): 
            res[i] = tmp = max(arr[i+1],tmp)  # 连等写法
        return res
# 从前往后以此求最大值会超时
# 从后求 只用比一个值

# @lc code=end
Solution().replaceElements([17,1,1,1,1,1,1])