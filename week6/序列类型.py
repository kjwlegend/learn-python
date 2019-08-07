#序列类型

'''
包含
字符串类型
元组类型
列表类型

序列通用操作符 6 个
x in s
x not in s
s + t 连接两个序列
s*n  或 n*s 将s 复制n次
s[i]
s[i:j] 或 s[i:j:k] 切片， 返回序列s 中第 i 到 j 以步长 k 的元素子序列

通用函数
len(s)
min(s)
max(s)
s.index(x) 或 s.index(x,i,j)
s.count(x)
'''

'''
元组类型
元组是序列类型的一种扩展
tuple()
一旦被创建就不能被修改
使用小括号()  或 tuple() 创建， 元素用逗号分隔
def func():
    return 1,2     #  1,2 就是元组 (1,2)
    
元组集成了序列类型的全部通用操作

'''

'''
列表是序列类型的一种扩展， 但是创建后可以被修改
list()
列表的操作类型和方法
ls[i] = x 替换列表ls第i 元素为x
ls[i:j:k] = lt 用列表lt 替换ls 切片后所对应元素字列表
del ls[i] 删除列表ls 中第 i 元素
del ls[i:j:k] 删除列表ls 中第i到j 以k 为步长的元素
ls =+ lt 更新列表ls 将列表lt 元素增加到列表ls 中
ls *= n 更新列表ls, 其元素重复 n 次

列表操作函数
ls.append(x) 在列表ls 最后增加一个元素x
ls.clear() 删除ls中的所有元素
ls.copy() 生成一个新列表， 复制ls 中所有元素
ls.insert(i,x) 在列表ls的第 i 位置增加元素x
ls.pop(i) 将列表ls 中第i 位置元素取出并删除该元素
ls.reverse() 反转列表顺序
ls.remove(x) 将列表ls 中出现的第一个元素x 删除
'''
