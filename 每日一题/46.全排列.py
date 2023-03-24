#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# -*- encoding: utf-8 -*-
'''
@Description:	[46] 全排列
@Date:	2023/03/24 10:06:25
@Author:	ZinkCas
@version:	1.0
'''

# @lc code=start
from typing import List
from itertools import permutations, combinations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # AK版
        # res = permutations(nums,len(nums))
        # return list(res)

        # 手写DFS版本
        res = []
        nlen = len(nums)
        vis = [False for _ in range(-10, 11)]

        def dfs(tmp: List[int]):
            if len(tmp) == nlen:
                res.append(tmp[:]) # 烦死了这深浅拷贝 浅拷贝只是拷贝数据的第一层，不会拷贝子对象
                return
            
            for i in range(nlen):
                if vis[nums[i]] == False:
                    tmp.append(nums[i])
                    vis[nums[i]] = True
                    #print(tmp)
                    dfs(tmp)
                    tmp.pop()
                    vis[nums[i]] = False

        dfs([])
        return res


# @lc code=end


print(Solution().permute(nums=[1, 2, 3]))
