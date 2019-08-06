# 递归示例
# 递归本身是一个函数， 递归需要调用自身
# 函数 + 分支语句 及时递归

def fact(n):
    if n == 0 :
        return 1
    else:
        return n * fact(n-1)


#字符串反转
# 将字符串s 反转后输出

def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:])+s[0]

# 斐波那契数列

def f(n):
    if n ==1 or n ==2: #函数加分支结构
        return 1
    else: #递归链条
        return f(n-1) + f(n-2) #递归基例

# 汉诺塔问题

count = 0
def hanoi(n,src,dst,mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1,src,dst))
        count +=1
    else :
        hanoi(n-1,src, mid, dst)
        print("{}:{}:->{}".format(n,src,dst))
        count += 1
        hanoi(n-1,mid,dst,src)
hanoi(3,"a","b","c")
print(count)