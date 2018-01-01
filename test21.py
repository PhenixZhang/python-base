import sys          #导入import模块
print("此脚本路径：",sys.argv)     #输出此脚本路径
print('—'*100)
print("此模块存放路径：",sys.path)  #输出此模块存放路径
print('—'*100)
print(dir(sys))                     #内置dir()函数可找到模块内所有参数，并以字符串列表形式返回