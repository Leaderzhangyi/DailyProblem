#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#

from typing import List
# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def check(i):
            for j in str(i):
                if j=="0":
                    return False
                else:
                    if i%int(j)!=0:
                        return False
            return True
        res=[]
        for i in range(left, right+1):
            if check(i):
                res.append(i)
        return res
# @lc code=end

print(Solution().selfDividingNumbers(1,22))