#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        flag = 0
        tmp_dict = {5:0,10:0,20:0}
        for m in bills:
            if m == 5:
                tmp_dict[m] += 1
            elif m == 10:
                tmp_dict[m] += 1
                tmp_dict[5] -= 1
                if tmp_dict[5] < 0:
                    return False
            else:
                if tmp_dict[10] >= 1 and tmp_dict[5]>=1:
                    tmp_dict[10] -= 1
                    tmp_dict[5] -= 1
                    tmp_dict[20] += 1
                elif tmp_dict[5] >= 3:
                    tmp_dict[5] -= 3
                else:
                    return False
        return True


# @lc code=end
