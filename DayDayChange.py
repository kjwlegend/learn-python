import math
import random

'''
交易成功时， 每天净值增长 30%
失败时，亏损15%

交易天数：x

F=P*(1+i)^n
F=A((1+i)^n-1)/i 公式描述：
F：终值（Future Value），或叫未来值，即期末本利和的价值。
P：现值（Present Value），或叫期初金额。
A ：年金（Annuity），或叫等额值。
i：利率或折现率
n：计息期数(公式中为（1+i）的次方数)
'''




def interest():
    initialvalue = eval(input("输入投入成本: "))
    winrate = eval(input("成功率: "))
    days = eval(input("交易天数: "))
    win = eval(input("盈利百分比: "))
    fail = eval(input("亏损百分比: "))

    for i in range(days):
        p = random.random()
        if p < winrate:
            initialvalue = initialvalue * (1 + win)
            print("第"+str(i)+"日交易成功,净值是： " + str(initialvalue))
        else:
            initialvalue = initialvalue * (1 - fail)
            print("第"+str(i)+"日交易失败,净值是： " + str(initialvalue))
    print("最终净值是: {:.2f} ".format(initialvalue))


# interest()


'''
random 库概述
常用的函数
基本随机数函数: seed(), random()

random.seed(10) 产生种子10对应的序列。 随机数种子能够产生特定的随机数, 可以不断的重复复现
random() ==> 生成一个[0.0 ,1) 的随机小数


扩展随机数函数:
randint(a,b) ==》 生成一个 a b 之间的整数
randrange(m,n[,k]) 生成一个 m n 之间，以K 为步长的随机整数
getrandbits(k) 生成一个 K 比特长的随机整数 random.getrandbits(16)  ==>37885
uniform(a,b) 生成一个a,b 之间的随机小数 random.uniform(10,100) ==> 13.298281
choice(seq) 从序列seq中随机选取一个元素
shuffle(seq) 对序列seq 中的元素随机排列， 返回打乱后的序列。

'''

#计算圆周率

def calPi(n):
    pi = 0
    for k in range(n):
        pi += 1/pow(16,k) * ( \
            4/(8*k+1) - 2/(8*k+4) - \
            1/(8*k+5) - 1/(8*k+6))
    print("圆周率值是: {}".format(pi))

calPi(2)