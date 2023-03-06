#
# @lc app=leetcode.cn id=1837 lang=python3
#
# [1837] K 进制表示下的各位数字总和
#

# @lc code=start
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        remainder = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        # 当n大于0的时候执行循环
        res = ""
        while n:
            res = remainder[n % k] + res
            n //= k
        return sum(map(int,list(res)))
 
# if __name__ == '__main__':
#     decimal, x = map(int, input().split())
#     print(Solution().sumBase(decimal, x))

# @lc code=end

