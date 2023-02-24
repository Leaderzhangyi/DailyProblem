#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#
from typing import List
# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters)
        while l < r:
            mid = (l + r)//2
            if ord(letters[mid]) > ord(target):
                r = mid
            else:
                l = mid + 1
        if l == len(letters): return letters[0]
        return letters[l]
# @lc code=end

