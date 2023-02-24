#
# @lc app=leetcode.cn id=1370 lang=python3
#
# [1370] 上升下降字符串
#

# @lc code=start
from collections import OrderedDict


class Solution:
    def sortString(self, s: str) -> str:
        ss = sorted(s)
        cnt = OrderedDict()
        for ch in ss:
            if ch not in cnt:
                cnt[ch] = 1
            else:
                cnt[ch] += 1
        res = ""
        print(cnt)
        while len(res) < len(ss):
            for k, v in cnt.items():
                if v > 0:
                    res += k
                    cnt[k] -= 1

            for k, v in reversed(cnt.items()):
                if v > 0:
                    res += k
                    cnt[k] -= 1
        return res
# @lc code=end

res = Solution().sortString(s = "aaaabbbbcccc")
print(res)
