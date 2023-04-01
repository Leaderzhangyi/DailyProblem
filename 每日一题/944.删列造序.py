#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#
from typing import List
# @lc code=start
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for item in zip(*strs):
            # print(item)
            # print(sorted(item))
            if list(item) != sorted(item):
                res += 1
        return res 

# @lc code=end

print(Solution().minDeletionSize(["cba","daf","ghi"]))