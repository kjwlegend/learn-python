# 第四章 程序的控制

#异常处理的相关方方法

# try:
#     num = eval(input("请输入一个整数"))
#     print(num**2)
# except NameError:
#     print("请输入一个整数,重新输入")
# else:
#     print("语句块3 -- 在不发生异常时执行")
# finally:
#     print("语句块4 - 无论什么情|况 最后都会执行")


# CalBMI 条件分支

height, weight = eval(input("请输入身高（米）/体重（KG），使用逗号隔开"))

bmi = weight / pow(height,2)
print("BMI 数值为：{:.2f}".format(bmi))
who, nat = "",""
if bmi < 18.5:
    who, nat = "偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    who, nat = "正常", "正常"
elif 24 <= bmi < 25:
    who, nat = "正常", "偏胖"
elif 25 <= bmi < 28:
    who, nat = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    who, nat = "偏胖", "肥胖"
print("bmi指标为: 国际{0:30^=}, 国内{1:5^=}".format(who,nat))


# 遍历循环
# for i in range(M,N,K)   M 起始， N 结尾整数, K 步长
# for c in "string"  ==> 把字符串里的每一个字符取出来
# for item in ls : ==>把列表里的每个拿出来作为循环 .  item in ['123',222,'test']
# for line in fi  -==》 对文件里的每一行作为遍历循环

# 无限循环
# while  {condition} :

# 循环控制内的保留字:  break 和 continue 一个保留字仅跳出一层循环
# break 跳出并结束当前循环，执行循环后的语句
# continue 结束当次循环，继续执行后续的循环语句
