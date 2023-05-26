#
# @lc app=leetcode.cn id=1656 lang=python3
#
# [1656] 设计有序流
#
from typing import List
# @lc code=start
class OrderedStream:
    def __init__(self, n: int):
        self.data, self.ptr = [None] * n, 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey - 1] = value
        ans = []
        while self.ptr < len(self.data) and self.data[self.ptr]:
            ans.append(self.data[self.ptr])
            self.ptr += 1
        return ans 


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
# @lc code=end

