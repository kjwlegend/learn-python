'''
学会三种主流数据的处理方法
'''

'''
集合类型
定义： 多个元素的无序组合
集合中的元素， 不可变
集合中的每个元素唯一，不会包含相同元素
集合用 {} 表示
元素之间用逗号分隔
生成集合用{} 或者 set()

集合操作：
并| 差| 交 | 补

6个操作符:
S|T
S-T
S & T
S ^ T

S <= T 或 S <T
S >= T 或 S>T

4个增强操作符：
S |= T  更新集合S， 包括在集合S 和T中的所有元素
S -= T  更新集合S， 包括在集合S但不在T种的元素
S &= T 更新集合S， 包括同事在集合和T中的元素
S ^= T  更新集合S， 包括集合S 和T 中的费相同元素
'''

A = {"p", "y", 123}
B = set("pypy123")

print(A-B)
print(B-A)
print(A|B)
print(A&B)
print(A^B)
print(A<B)
print(A>=B)

'''
集合处理方法
S.add(x)
S.discard(x)
S.remove(x)
S.clear()
S.pop()
S.copy()
len(S)
x in S
x not in S
set(x)
'''

