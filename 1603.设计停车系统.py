#
# @lc app=leetcode.cn id=1603 lang=python3
#
# [1603] 设计停车系统
#

# @lc code=start
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.catDict = {1:big,2:medium,3:small}

    def addCar(self, carType: int) -> bool:
        if self.catDict[carType] != 0:
            self.catDict[carType] -= 1
            return True
        
        return False
        



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
# @lc code=end

