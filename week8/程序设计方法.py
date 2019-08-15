'''
体育竞技分析案例

输入： 球员的数值
输出： 胜率

体育竞技分析： 模拟N场比赛场景
模拟： 抽象比赛过程，预测胜负结果

需要输入比赛规则

框架及步骤

-步骤1： 打印程序的介绍性信息
步骤2：获得程序运行参数:  ProA, proB, n
步骤3：利用球员A和B的能力值， 模拟N局比赛
步骤4： 输出球员A 和B的获胜比赛的场次和概率
'''

'''
自顶向下 (设计)
解决复杂问题的有效方法
将一个复杂的问题 分解成 若干个小问题

自底向上(执行)

'''

'''
第一阶段
main() 分解成
printIntro()
getInputs()
simNGames()
printSummary()

'''
#第一阶段
from random import random

def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值(以0到1之间的小数表示)")

def getInputs():
    a = eval(input("请输入选手A的能力值(0-1): "))
    b = eval(input("请输入选手B的能力值: "))
    n = eval(input("模拟比赛的场次： "))
    return a,b,n

def printSummary(winsA,winsB):
    n = winsA + winsB
    print("竞技分析开始， 功模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛, 占比{:0.1%}".format(winsA, winsA/n))
    print("选手B获胜{}场比赛, 占比{:0.1%}".format(winsB, winsB/n))


# 第三阶段
def gameOver(a,b):
    return a==15 or b ==15

def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
        print("{},{}".format(scoreA, scoreB))
        return scoreA, scoreB

def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

main()