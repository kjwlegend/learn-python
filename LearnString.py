#WeekNamePrintV1

'''
weekStr = "星期一星期二星期三星期四星期五星期六星期日"
weekId = eval(input("请输入星期数字(1-7): "))
pos = (weekId - 1) * 3
print(weekStr[pos: pos+3])
'''

#WeekNamePrintV2

weekStr = "一二三四五六七"
weekId = eval(input("请输入星期数字(1-7): "))
print("星期"+weekStr[weekId - 1])

# 字符串常用函数
'''
len(x) 返回字符串的长度
str(x) 将值化为字符串
hex(x) or oct(x) 将数字转化为 十六进制或八进制
chr(u) u 为unicode编码形式， 返回对应的字符
ord(u)

'''

# 常用的字符串处理方法
'''
str.lower() 或者 str.upper()
str.split(sep=None) 由str 根据sep 分割
str.count(sub) 返回子串 sub 在 str 中出现的次数
str.replace(old, new)
str.center(width[,fillchar]) 字符串str 根据宽度 width居中， fillchar 可选 "python".center(20,"=") 结果为'===============python========='
str.strip(chars) 从 str中 去掉 chars
str.join(iter) 在 iter变量除最后元素外每个元素增加一个 str  ",".join("12345" ==> "1,2,3,4,5"
'''