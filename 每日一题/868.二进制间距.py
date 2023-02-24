#
# @lc app=leetcode.cn id=868 lang=python3
#
# [868] 二进制间距
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        if binary.count('1') < 2:
            return 0
        res = 0
        i,j = 0,1
        while j < len(binary):
            if binary[i] == binary[j]:
                res = max(j-i,res)
              #  print(f"每次最大值:{res}")
                i = j
                j = i + 1
            else:
                j += 1
        return res 
# @lc code=end

print(Solution().binaryGap(22))