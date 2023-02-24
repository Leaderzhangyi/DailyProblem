#
# @lc app=leetcode.cn id=2418 lang=python3
#
# [2418] 按身高排序
#
from typing import List
# @lc code=start
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tmp = dict(zip(heights,names))
        #print(tmp)
        new = sorted(tmp.items(),key = lambda x:x[0],reverse=True)
        return [item[1] for item in new]
# @lc code=end

ss = Solution().sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170])
print(ss)
