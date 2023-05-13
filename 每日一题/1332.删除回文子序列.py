#
# @lc app=leetcode.cn id=1332 lang=python3
#
# [1332] 删除回文子序列
#

# @lc code=start
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return (s!=s[::-1]) + 1
            
        
        
# @lc code=end


print(Solution().removePalindromeSub(s = "abb"))