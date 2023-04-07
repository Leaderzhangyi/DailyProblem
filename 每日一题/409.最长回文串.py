#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # res_dict = Counter(s)
        # flag = False
        # res = 0
        # for item in res_dict.items():
        #     print(item)
        #     if not item[1] & 1:
        #         res += item[1]
        #     else:
        #         res += item[1] - 1
        #         flag = True
        #   #  print(f"res = {res}")
        # if flag:
        #     res += 1
        # return res 
       return len(s) - max(0,sum([s.count(chr)%2 for chr in set(s)]) - 1)



# @lc code=end

print(Solution().longestPalindrome(s = "abccccdd"))
