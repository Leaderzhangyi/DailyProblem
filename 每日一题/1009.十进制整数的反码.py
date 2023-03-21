#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 十进制整数的反码
#

# @lc code=start

# 原码+反码=(2^n)-1
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bins = bin(n)[2:]
        res = ""
        for ch in bins:
            if ch == "0":
                res += "1"
            else:
                res += "0"
        return int(res,2)
        
# @lc code=end

print(Solution().bitwiseComplement(5))