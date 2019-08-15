#如何读取二维数据

fo = open(fname)
ls = []
for line in fo:
    line = line.replace('\n','')
    ls.append(line.split(","))
fo.close()

#写二维数据

ls = [[],[],[]] #二维列表
f = open(fname,'w')
for item in ls:
    #给每一行增加逗号和回车
    f.write(','.join(item) + '\n')
f.close()


# 如何注意遍历二维数据中的所有元素，

ls = [
      [1,2],
      [3,4],
      [5,6]
    ]
for row in ls:
    for column in row:
        print(column)
