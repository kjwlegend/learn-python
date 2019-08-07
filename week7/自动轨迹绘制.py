# 步骤1：定义数据文件格式（接口）
# 步骤2： 编写程序 根据文件接口
# 步骤3：绘制

import turtle as t

t.title('自动轨迹绘制')
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)

# 解析数据文件

datals = []
f = open("draw.txt")
for line in f:
    line = line.replace("\n","")
    datals.append(list(map(eval,line.split(","))))

f.close()
print(datals)

#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
