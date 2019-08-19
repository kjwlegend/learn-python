#
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
# 通货膨胀率按 5 % 计算

deposit = 15
import random

def goldCalc(init, successRate, days):
    # 设置黄金振幅与翻倍关系
    goldflucation = {
        '5': '100%',
        '10': '150%',
        '12': '200%',
        '15': '300%',
        '20': '650%'
    }
    for i in range(days):
        if random.random():
            continue


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

goldCalc(200,5,5)