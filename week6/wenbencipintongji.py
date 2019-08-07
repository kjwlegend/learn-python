# jieba 库 是python中十分流行的中文分词第三方库
# jieba.lcut(s)
import jieba

jieba.lcut("中国是一个伟大的国家")

# 案例一 哈姆雷特 HAMLET
#分析哈姆雷特中的词频统计
#
# def getText():
#     txt = open("hamlet.txt","r").read()
#     txt = txt.lower()
#     for ch in "~!@#$%^&*()_+-=[]\{}|;':,./<>?":
#         txt = txt.replace(ch, " ")
#     return txt
#
# hamletTxt = getText()
# words = hamletTxt.split()
# counts = {}
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# items = list(counts.items())
# items.sort(key=lambda x:x[1], reverse=True)
# for i in range(50):
#     word, count = items[i]
#     print("{0:<10}{1:>5}".format(word,count))
#

# 案例2 三国演义人物出场统计
# 词频统计不是人物出场统计
# 需要面向问题，增加排除词库

txt = open("threekindoms.txt","r",encoding="utf-8").read()
words = jieba.lcut(txt)
excludes = {"将军", "却说", "荆州", "二人", "不可","不能","如此","商议", "如何", "左右", "军马", "引兵","次日","大喜"}
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word =="诸葛亮" or word =="孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word =="孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
