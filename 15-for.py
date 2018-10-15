for i in range(1,6):                # 控制行数为6行，每行开始遍历
   for j in range(1, i+1):          # 在第i行上输出i个*
      print("*",end='  ')           # end= 是参数，设定结束字符
   print('\r')                      # 换行
