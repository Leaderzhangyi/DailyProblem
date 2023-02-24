#
# @lc app=leetcode.cn id=1089 lang=python3
#
# [1089] 复写零
#
from typing import List
# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # 老子一定写出双指针
        i,j = 0,1
        n = len(arr)
        while j < n:
            if arr[i] == 0:
                arr.insert(j,0)
                i = j + 1
                j = i + 1
                #print("j = ",j)
            else:
                i += 1
                j += 1
        new = len(arr)
        for _ in range(new - n):
            arr.pop()
        #print(arr)

# @lc code=end

print(Solution().duplicateZeros(arr =[1,0,2,3,4,5]))