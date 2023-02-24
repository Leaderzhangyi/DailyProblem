#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#
from typing import List
# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        res = []
        i,j = 0,0
        while True:
            res.append(pushed[i])
            while res[-1] == popped[j]:
                #while True:
                res.pop()
                j += 1
                if not len(res):
                    break
            i += 1
            if i == len(pushed):
                break
        if not len(res):
            return True
        else:
            return False
                    

# @lc code=end
ss = Solution().validateStackSequences(pushed = [2,1,0], popped = [1,2,0])
print(ss)
