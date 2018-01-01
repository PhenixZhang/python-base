def primenumber(a):             #定义素数函数，a为参数
    #此函数功能为输出a以内的素数，其中a自定义
    j=1
    list=[]                     #定义列表
    for i in range(3,a):        #for循环遍历3到a
        for j in range(2,i):    #内嵌for循环遍历2到i
            if(i%j == 0):         #判断i能否被j除尽
                break           #若为True 则终止循环
        if j == i-1:              #判断j是否等于i-1
            list.append(i)      #若为Ture则将i写入列表中
    return list                 #返回列表

if __name__ == "__main__":        #当模块被直接运行时，以下代码块将被运行
    p = int(input("please input number:"))     #输入参数
    print(primenumber(p))                       #运行函数并输出p以内的素数

