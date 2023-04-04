#
# @lc app=leetcode.cn id=2042 lang=python3
#
# [2042] 检查句子中的数字是否递增
#



# ascii吗只能表示0-9 我估计只要字符串第一位比6小 那前者都是大的
# @lc code=start
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
        nums = [item for item in s.split(" ") if item.isdecimal()]
        for i in range(1,len(nums)):
            if nums[i - 1] >= nums[i] :
                print(nums[i],nums[i - 1])
                return False
        return True



        
# @lc code=end
print(Solution().areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))