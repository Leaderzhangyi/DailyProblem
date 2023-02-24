#
# @lc app=leetcode.cn id=1200 lang=python3
#
# [1200] 最小绝对差
#
from typing import List
# @lc code=start


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        Mdiff = 1e9
        res = []
        for i in range(len(arr) - 1):
            if arr[i + 1]-arr[i] < Mdiff:
                res.clear()
            if arr[i + 1] - arr[i] <= Mdiff:
                Mdiff = arr[i + 1] - arr[i]
                res.append([arr[i], arr[i+1]])
                

        return res


# @lc code=end

print(Solution().minimumAbsDifference(arr=[40, 11, 26, 27, -20]))
