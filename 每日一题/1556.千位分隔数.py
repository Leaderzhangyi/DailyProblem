#
# @lc app=leetcode.cn id=1556 lang=python3
#
# [1556] 千位分隔数
#

# @lc code=start
class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = str(n)
        if len(ans) < 4:
            return ans 
        res = ""
        flag = 0
        for i,c in enumerate(ans[::-1]):
            flag += 1 
            res += c
            if flag == 3 and i != len(ans)-1:
                print(i)
                flag = 0
                res+="."
        return res[::-1]         
        
# @lc code=end

res = Solution().thousandSeparator(123456789)
print(res)
