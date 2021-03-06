'''据说古代有一个梵塔，塔内有三个底座A、B、C，A座上有64个盘子，盘子大小不等，
大的在下，小的在上。有一个和尚想把这64个盘子从A座移到C座，
但每次只能允许移动一个盘子，在移动盘子的过程中可以利用B座，
但任何时刻3个座上的盘子都必须始终保持大盘在下、小盘在上的顺序。
如果只有一个盘子，则不需要利用B座，直接将盘子从A移动到C即可。
和尚想知道这项任务的详细移动步骤和顺序。这实际上是一个非常巨大的工程，
是一个不可能完成的任务。根据数学知识我们可以知道，移动n个盘子需要2^n-1步，
64个盘子需要18446744073709551615步。如果每步需要一秒钟的话，
那么就需要584942417355.072年。'''

def hannuo(num, src, dst, temp=None):
    #声明用来记录移动次数的变量为全局变量
    global times
    #确认参数类型和范围
    assert type(num) == int, 'num must be integer'
    assert num > 0, 'num must > 0'
    #只剩最后或只有一个盘子需要移动，这也是函数递归调用的结束条件
    if num == 1:
        print('The {0} Times move:{1}==>{2}'.format(times, src, dst))
        times += 1
    else:
        #递归调用函数自身，
        #先把除最后一个盘子之外的所有盘子移动到临时柱子上
        hannuo(num-1, src, temp, dst)
        #把最后一个盘子直接移动到目标柱子上
        hannuo(1, src, dst)
        #把除最后一个盘子之外的其他盘子从临时柱子上移动到目标柱子上
        hannuo(num-1, temp, dst, src)
#用来记录移动次数的变量
times = 1
#A表示最初放置盘子的柱子，C是目标柱子，B是临时柱子
hannuo(3, 'A', 'C', 'B')
