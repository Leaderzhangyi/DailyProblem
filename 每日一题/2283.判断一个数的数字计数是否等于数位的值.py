#
# @lc app=leetcode.cn id=2283 lang=python3
#
# [2283] 判断一个数的数字计数是否等于数位的值
#

# @lc code=start
from collections import Counter
class Solution:
    def digitCount(self, num: str) -> bool:
        num_count = Counter(num)
        # for i,n in enumerate(num):
        #     if num_count[str(i)] != int(n):
        #         return False
        # return True
        return all([False if num_count[str(i)] != int(n) else True for i,n in enumerate(num) ])
        # 列表生成式同时有 if-else则都放在for前面
        # 若只有if 则在for后面


# @lc code=end

print(Solution().digitCount(num = "1210"))