dict = {'首行政':'中南楼','南行政':'中原楼','教学楼':'文泰楼','图书馆':'逸夫楼'}    #定义字典
print(dict.keys())                  #用keys()函数输出字典中的键
print(dict.values())                #用values()函数输出字典中的值
for key,value in dict.items():      #引入for循环结构 用items()函数遍历字典中的键值对
    print(key,value)                #分别输出键值对
