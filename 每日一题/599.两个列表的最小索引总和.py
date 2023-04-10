#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

from typing import List
# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = {}
        ll = []
        

        for item in list2:
            if item in list1:
                res[item] = list2.index(item) + list1.index(item)

        Min = min(res.values())

        for k,v in res.items():
            if Min == v:
                ll.append(k)
            #print(item)
        return ll 

# @lc code=end

print(Solution().findRestaurant(["happy","sad","good"],["sad","happy","good"]))