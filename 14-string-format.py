i = 1
while i <= 9:                                    # 外层循环控制行数
     j=1
     while j <= i:                               # 内层循环控制列数
          mut =j * i
          print("%d*%d=%d"%(j,i,mut), end=" ")   # %前后分别为输出格式和输出内容
          j += 1                                 # j递加
     print("\t")                                 #  \t代表制表符 让其横竖依次排列
     i += 1                                      #  i递加
