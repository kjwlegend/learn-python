import  time

'''
时间获取: 
time() 获取当前时间戳
ctime() 获取当前时间并且以易读方式展现
gmtime() 获取当前时间，是计算机可处理的格式


时间格式化：将时间以合理的方式展示 类似支付穿格式化
strftime(tpl,ts)

tpl是格式化模板字符串，用来定义输出效果, ts是计算机内部时间类型变量
t = time.gmtime()
格式化模板有： 

%Y
%B
%b
%a
%H
%I
.......
time.strftime("%Y-%m-%d %H:%M:%S", t)   >>>>  '2018-01-26 12:55:20'


strptime(str,tpl)  ==>将一个字符串变成时间

程序计时:

测量时间:  perf_counter()

start = perf_counter()
end = perf_counter()
end - start


sleep(s)

def wait():
    time.sleep(3.3)
wait()
'''

t = time.gmtime()
time.strftime("%Y-%m", t)
timeStr = '2018-01-26 12:55:20'


# 文本进度条多行刷新

scale = 10
print("------执行开始------")
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale -i)
    c = (i/scale) * 100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("------执行结束------")


# 文本进度条单行动态刷新
for i in range(101):
    print("\r{:3}%".format(i), end="")
    time.sleep(0.1)


#文本进度条完整效果

scale = 50
print("执行开始".center(scale//2,"-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale -i)
    c = (i/scale)*100
    dur = time.perf_counter() -start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur), end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2, '-'))


# 根据不同的函数 变化展示进度条

'''
Linear -- 如实展示 == f(x) = x
Early Pause -- Speeds up == f(x) = x + (1-sin(x*pi*2+pi/2)/-8
Late Pause -- Slows down == f(x) = x + (1-sin(x*pi*2+pi/2)/8
'''