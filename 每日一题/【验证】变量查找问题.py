from ctypes import string_at
from sys import getsizeof
from binascii import hexlify
res = []
for i in range(1,4):
    print(f"{i}次".center(50,"="))
    def test(i):
        # print(globals())
        # print(locals())
        return i
    #print("调用测试:",test())
    res.append(test)

print(res)
print(res[0]())
print(res[1]())
print(res[2]())
