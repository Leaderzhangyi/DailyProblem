#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def ccc(n):
            res = 0
            while n != 0:
                n &= (n-1)
                res += 1
            return res
        ans = [] 
        for i in range(12):
            for j in range(60):
                if ccc(i) + ccc(j) == turnedOn:
                    ans.append(str(i)+":"+("0"+str(j) if j < 10 else str(j)))
        
        return ans 

# @lc code=end

