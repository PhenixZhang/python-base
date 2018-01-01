f = lambda x, y, z :x+y+z       #功能是输出三个参数之和，参数规则同def
print('和 =',f(1,2,3))

L = [lambda x: x+2, lambda x: x*2, lambda x: x**2]      #定义包含三个lambda函数的列表，功能是分别输出参数的+2、*2和2次方
print ("L =", L[0](1), L[1](2), L[2](3))
