#
# @lc app=leetcode.cn id=1684 lang=python3
#
# [1684] 统计一致字符串的数目
#
from typing import List
# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        basic = len(allowed)
        cmp = list(allowed)
        flag = len(words)
        for item in words:
            ans = set(item)
            if len(ans) > basic:
                flag -= 1
                continue
            else:
                for elem in ans:
                    if elem not in cmp:
                        flag -= 1
                        break
                
        return flag
# @lc code=end

h = Solution().countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"])
print(h)

