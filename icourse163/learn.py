# lesson 1 Cel to Fahrihat

# TempStr = input("请输入带有符号的温度值：")
# if TempStr[-1] in ['f', 'F']:
#     C = (eval(TempStr[0:-1]) - 32) /1.8
#     print("转换后的温度是{:.2f}".format(C))
# elif TempStr[-1] in ['C', 'c']:
#     F = 1.8*eval(TempStr[0:-1]) + 32
# else:
#     print("输入格式错误")
#
#
# '''
# {:.2f} 表示float number 浮点数
# {}    .format(C)    会将变量C 放入到{} 中
# '''
#
# number = int(input())
# if number == 0:
#     print("Hello World")
# elif number > 0:
#     print("He\nll\no \nWo\nrl\nd")
# else:
#     print("H\ne\nl\nl\no\n \nW\no\nr\nl\nd")

string = input()
# op_num = 0
# op = ['+', '-', '*', '/']
# for i, s in enumerate(string):
#     if s in op and i != 0:
#         op_num = i
#         if string[0] == '-':
#             num1 = -float((string[1:i]).strip())
#         elif string[0:2] == '0x':
#             num1 = int(eval((string[:i]).strip()))
#         else:
#             num1 = float((string[0:i]).strip())
#         num2 = float((string[i + 1:]).strip())
#
#         if s == op[0]:
#             print('{:.2f}'.format(num1 + num2))
#         elif s == op[1]:
#             print('{:.2f}'.format(num1 - num2))
#         elif s == op[2]:
#             print('{:.2f}'.format(num1 * num2))
#         else:
#             print('{:.2f}'.format(num1 / num2))
print("{:.2f}".format(eval(string)))

