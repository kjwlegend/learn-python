import wordcloud
import jieba
from scipy.misc import imread
#wordcloud 库常规方法
# w.generate(txt) 向对象中加载文本txt
# w.to_file(filename) 将词云输出为图像文件
'''
步骤1：配置对象参数
步骤2： 加载词云文本
步骤3： 输出词云文件


对象参数
min_font_size     ==> w=wordcloud.WordCloud(min_font_size=10)
max_font_size
font_step   ===>  w = wordcloud.WordCloud(font_step=2)
font_path ===> w = wordcloud.WordCloud(font_path="msyh.ttc")
max_words   最大单词数量
stop_words  排除哪些词 stop_words={"ab","cc"}
mask ==> 给词云增加遮罩，指定词云形状
from scipy.misc import imread
mk=imread("pic.png")
w.wordcloud.WordCloud(mask=mk)

background_color ==> 指定背景颜色
'''
mask = imread("pika.jpg")
f = open("../week6/threekindoms.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)

w = wordcloud.WordCloud(
    font_path = "msyh.ttc",
    width = 1000,
    height = 700,
    background_color = "white",
    mask = mask
    # min_font_size=5,
    # max_font_size=86
)

w.generate(txt)
w.to_file("pywordcloud.png")