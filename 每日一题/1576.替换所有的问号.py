#
# @lc app=leetcode.cn id=1576 lang=python3
#
# [1576] 替换所有的问号
#

# @lc code=start
class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i]== "?":
                for ch in "abc":
                    if not (i > 0 and s[i-1]==ch or i < len(s)-1 and s[i+1]==ch):
                        s[i] = ch
                        break
        return "".join(s)

# @lc code=end

print(Solution().modifyString("?abva"))                

# input:
#     - 数据集样本量n x_1, x_2.....x_n
#     - 簇中心数量K c_1, c_2..c_k
#     - 最大迭代次数t

# output:
#     - medoids: k个中心点的坐标
#     - clusters: 数据点所属簇的索引列表


# medoids = 随机选择k个数据点为聚类中心

# for _ in range(t):  # 迭代次数
#     d = 0
#     for i in range(n):
#         if i not in medoids:  # n - k
#             for j in range(k):  # k
#                 new_medoids[j] = i

#                 for m in range(n):
#                     if m not in new_medoids:  # n - k
#                         d += dist(new_medoids, data[m]) # 计算每个距离代价
#                 if d < 之前距离:
#                     medoids = new_medoids # 替换原来的中心点为当前中心点
# return medoids
