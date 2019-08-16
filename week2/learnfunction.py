'''
局部变量： 函数内部使用的变量
全局变量： 在函数外面定义的变量。
规则1： 局部变量和全局变量是不同变量
局部变量 在函数计算后就会被释放。 但是可以使用global 保留字进行声明

规则2： 局部变量为组合数据类型且未创建， 等同于全局变量。
判断方法是是否有创建同名的变量。
'''

# 非可选参数+可选参数

def fact(n, *b):
    s = 1
    for i in range(1 , n+1):
        s *= i
    for item in b:
        s *= item
    return s

# 给参数定义位置 将第一个输入的参数设为M值
def fact2(n, m=1):
    s = 1
    for i in range(1 , n+1):
        s *= i

    return s//m

#函数的返回值 return. 案例返回3个值
def fact3(n, m=1):
    s = 1
    for i in range(1 , n+1):
        s *= i
    return s//m, n , m   #元组类型

print(fact(10,3))
print(fact2(10,5))
print(fact2(m=5,n=10))
print(fact3(10,5))


# lambda 函数： 能够返回函数名为结果
# 是一种匿名函数， 没有名字的函数
# 使用 lambda 保留自定义， 函数名是返回结果

# <函数名> = lambda <参数> :<表达式>

f = lambda x,y : x + y
f(10,15)
print(f(10,15))
print(g())