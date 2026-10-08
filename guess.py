# 猜数字小游戏（单文件完成）
# 导入 random 模块，用来生成随机数
import random

# 1.电脑随机生成一个 1~100 的整数，作为正确答案
answer = random.randint(1, 100)

# 2.count 记录玩家猜了多少次，初始为 0
count = 0

# 3.循环让玩家一直猜，猜中后用 break 跳出循环
while True:
    temp = input("请输入你猜的数字（1-100）：")

    # 如果输入的不是数字，提示后让玩家重新输入，避免程序报错
    if not temp.isdigit():
        print("输入无效，请输入一个整数！")
        continue

    guess = int(temp)    # input 得到的是字符串，用 int() 转成整数
    count = count + 1    # 每猜一次，次数加 1

    # 4.比较玩家猜的数字和答案
    if guess > answer:
        print("大了")
    elif guess < answer:
        print("小了")
    else:
        print("恭喜你，猜对了！")
        break            # 猜中，结束循环

# 5.循环结束，输出一共猜了几次
print("你一共猜了", count, "次")
