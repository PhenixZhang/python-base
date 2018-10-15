import random   #导入random随机数模块
x = random.randint(1, 100)      #x为1-100间任意随机数
y = random.randint(1, 100)      #y为1-100间任意随机数
if x > y:                       #if条件控制
    print('x = ', x)
elif x == y:                    #等价于else if
    print('x+y = ', x + y)
else:
    print('y = ', y)
