#
# @lc app=leetcode.cn id=1399 lang=python3
#
# [1399] 统计最大组的数目
#

# @lc code=start
from collections import Counter
class Solution:
    def countLargestGroup(self, n: int) -> int:
        # 智商退步
        # res = {}
        # for i in range(1,n+1):
        #     tmp = sum([int(i) for i in str(i)])
        #     res[tmp] = res.get(tmp,[])
        #     res[tmp].append(i)
        #    # res[tmp].append(i)
        # res_len = [len(v) for k,v in res.items()]
        # max_len = max(res_len)
        # #print(res)
        # return sum(1 for item in res_len if item == max_len)
        
        # 高级求个数
      #  print(list(map(lambda x: sum(map(int, str(x + 1))), range(n))))

        # 
        return max(Counter((Counter(map(lambda x: sum(map(int, str(x + 1))), range(n))).values())).items())[1]

# @lc code=end

print(Solution().countLargestGroup(264))
