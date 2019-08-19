import random

# 当账户价值翻倍后进行出金， 提升原始资本为1/2 仓位
# 当账户价值大于2000时，提升原始资本仓位至 200 美金
# 当账户总价值大于10000时， 提升原始仓位为 1000美金
#
# 每个月的交易日为20天
# 账户操盘的成功率为 x ， 交易成功时账户根据盈亏比翻倍
# 交易失败时，进行50% 的本金进行保护，并重新从备用账户获取资金
# 交易账户的资金为备用账户1/4

# 需要知道要多少次操作和时间周期能够达到一定账户价值
#
#
#
# 账户价值大于10万美金后，进行分散投资。 超过10万美金的价值部分取 30% 进行其他风险资产投资。 风险资产年华收益为10% 直到其他风险资产价值总额达到100 万元
#
# 通货膨胀率每年按 3 % 计算

def goldPriceSimulation(days):
    goldPriceFluctionList = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    def getPrice(day,count):

        print("========第{0:}天========".format(day+1, count))
        randomNumber = random.random()
        print("随机值为：{:.2f}".format(randomNumber))

        # days 从1 开始，直到推算的日期
        goldPriceFluctionRate = (len(goldPriceFluctionList) / 20) * count

        priceLimit = round(goldPriceFluctionRate)  # 随着时间增长，价格波动增大的概率会余越大

        if randomNumber < 0.8:
            if priceLimit < 5:
                priceRange = goldPriceFluctionList[0:5]  # 当波动值不高时，黄金振幅为5-10美金
                print('test')

            elif priceLimit < len(goldPriceFluctionList):
                priceRange = goldPriceFluctionList[priceLimit:]
                print('test2')

            elif priceLimit >= len(goldPriceFluctionList):# 当振幅概率超出列表数量时，限制最大值为列表最大值
                print('test3')
                priceRange = goldPriceFluctionList[len(goldPriceFluctionList)-1:len(goldPriceFluctionList)]
            print("今日的价格波动范围是aa{}".format(priceRange))
        else:
            priceRange = goldPriceFluctionList # 有少许概率即使概率不高，振幅会不固定
            print("今日的价格波动范围是bb{}".format(priceRange))
        # 获取随机价格
        price = random.choice(priceRange)

        return price



    for day in range(days):
        # 黄金价格波动随着日期增长，振幅扩大的概率会巨大提升。
        # 当波动幅度超过14美金后，振幅的概率会重新从0 计算
        # 黄金每20天内必然会发生产生20美金以上的振幅
        # 每周有概率会产生一次12美金以上的振幅
        # 每两周有概率会产生15美金以上的振幅
        # 黄金每日的振幅随机，为5-9美金


        count = 1
        price =getPrice(day,count)
        if price < 14:

            print("第{0:}天的价格波动为{1:}美金\n行情累积天数:{2:}".format(day+1, price,count))
        else:
            count = 1
            print("第{0:}天的价格波动为{1:}美金, \n行情累积天数:{2:}\n价格范围计数器将重置".format(day+1, price,count))

        # if price > 14:
        #     day = i - day
        #     print("价格重置")
        #



goldPriceSimulation(25)


def goldCalc(init, successRate, days):
    # 规则说明
    #
    # 黄金日内波动    账户盈亏        振幅概率
    # 5           10%           0.4
    # 10          150%          0.3
    # 12          200%          0.15
    # 15          300%          0.1
    # 20          650%          0.05
    #

    #
    # 设置黄金振幅与翻倍关系
    goldPriceAndAccountValue = {
        '5': '100%',
        '10': '150%',
        '12': '200%',
        '15': '300%',
        '20': '650%'
    }




    init = init * successRate
    random.seed(2)

    # while init < 100000:
    print(random.Random)
    print(random.randint(0,1))
    print(random.randint(1,1001))


def riskAsset(init):
    return ""

def currencyInflation(rate):
    return ""


def main():
    return ""

