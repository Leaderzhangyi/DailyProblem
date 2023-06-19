#
# @lc app=leetcode.cn id=2129 lang=python3
#
# [2129] 将标题首字母大写
#

# @lc code=start
class Solution:
    def capitalizeTitle(self, title: str) -> str:
  
        return " ".join([word.capitalize() if len(word) > 2 else word.lower() for word in title.split(" ")])
# @lc code=end


print(Solution().capitalizeTitle(title = "capiTalIze Of titLe"))