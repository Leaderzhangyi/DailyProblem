#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#
from typing import List
# @lc code=start
import copy
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        vis = [[0 for _ in item] for item in image]
        tmp = copy.deepcopy(image)
        def check(x:int,y:int,old:int) -> bool:
            # 检查是否出界 
            if 0 <= x < len(image) and 0 <= y < len(image[0]):
                # 检查是否标记
                if vis[x][y] == 0 and old == image[x][y]:
                    return True
            return False
        
        def dfs(i,j):
            vis[i][j] = 1 # mark 
            tmp[i][j] = color
          #  print(f"当前坐标为：{i,j},值为{image[i][j]}")
            for item in [[1,0],[-1,0],[0,1],[0,-1]]: # 右、左、下、上
                kx = i + item[0]
                ky = j + item[1]
            #    print(f"移动坐标:{kx,ky}")
                if check(kx,ky,image[i][j]):
                    tmp[kx][ky] = color
                    dfs(kx,ky)
            return
        dfs(sr,sc)
        return tmp

# @lc code=end

print(Solution().floodFill(image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 2))