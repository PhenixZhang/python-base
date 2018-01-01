import sys  # 引入 sys 模块
classmates = ['Joe','phenix','Michael','Ariel','Ashlee','Anika','Marie','Linda','Jenson']
iterator = iter(classmates)     # 将列表classmates创建为迭代器对象iterator
while True:
    try:                            #第一次引入sys模块中的try语句，是处理异常的有力武器
        print(next(iterator))
    except StopIteration:           #出现意外就执行下面的命令
        sys.exit()                  #退出系统

