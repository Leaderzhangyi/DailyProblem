#
# @lc app=leetcode.cn id=1475 lang=python3
#
# [1475] 商品折扣后的最终价格
#
from typing import List
# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        i,j = 0,1
        while i < len(prices) - 1:
            #print("i= %d,j= %d"%(i,j))
            diff = prices[i] - prices[j]
            if diff >= 0:
                prices[i] = diff
                i += 1
                j = i + 1
            else:
                j += 1
            
            if j > len(prices) - 1:
                i += 1
                j = i + 1
             
        return prices
            
# @lc code=end

print(Solution().finalPrices(prices = [10,1,1,6]))