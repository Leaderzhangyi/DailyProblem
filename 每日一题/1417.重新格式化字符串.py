#
# @lc app=leetcode.cn id=1417 lang=python3
#
# [1417] 重新格式化字符串
#

# @lc code=start
class Solution:
    def reformat(self, s: str) -> str:
        l = [i for i in s if 'a' <= i <= 'z']
        n = [i for i in s if '0' <= i <= '9']
        letters = len(l)
        nums = len(n)
        res = ""
        if abs(letters - nums) >= 2:
            return res
        all = min(letters,nums)
        for _ in range(all):
            if letters >= nums:
                res += l.pop(0)
                res += n.pop(0)
            elif letters < nums:
                res += n.pop(0)
                res += l.pop(0)

        while l:
            res += l.pop()
        while n:
            res += n.pop()
        return res 
# @lc code=end

print(Solution().reformat(s = "a1123"))