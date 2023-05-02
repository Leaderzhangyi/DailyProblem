#
# @lc app=leetcode.cn id=2490 lang=python3
#
# [2490] 回环句
#

# @lc code=start
class Solution:
    def isCircularSentence(self, s: str) -> bool:
        a=s.split(' ')
        print(x[-1]==a[(i+1)%len(a)][0] for i,x in enumerate(a))
        return all(x[-1]==a[(i+1)%len(a)][0] for i,x in enumerate(a))


        
            

# @lc code=end

r = Solution().isCircularSentence(s = "leetl")
print(r)
