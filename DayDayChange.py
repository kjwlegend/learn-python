# day power

# 天天向上1： 变量， 每天提升
# dayfactor = 0.005
#
# dayup = pow(1+dayfactor, 365)
# daydown = pow(1-dayfactor, 365)
#
# print("向上{:.2f}, 向下 {:.2f}".format(dayup, daydown))

#  天天向上2： 工作日、非工作日
# dayup = 1.0
# dayfactor = 0.01
# for i in range(365):
#     if i % 7 in [6, 0]:
#         dayup = dayup*(1-dayfactor)
#     else:
#         dayup = dayup*(1+dayfactor)
# print("向上{:.2f}".format(dayup))
#

# 天天向上3 ：比较两个人

def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup*(1 - 0.01)
        else:
            dayup = dayup*(1 + df)
    return dayup
dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日的参数是: {:.3f}".format(dayfactor))