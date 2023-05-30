#
# @lc app=leetcode.cn id=1598 lang=python3
#
# [1598] 文件夹操作日志搜集器
#
from typing import List

# @lc code=start
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for item in logs:
            if item == "../":
                res -= 1 
                if res < 0:
                    res = 0
                continue
            elif item == "./":
                continue
            res += 1 
        
        return res if res >= 0 else 0 

# @lc code=end

print(Solution().minOperations(logs = ["d1/","d2/","./","d3/","../","d31/"]))
