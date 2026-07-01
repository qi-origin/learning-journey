#变量和打印
name="邰稚霄"
age=19
print(f"我的名字是{name},今年{age}岁.")


#数字运算
a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%b)


#自我检验——用代码计算圆的面积
pai=3.14
r=5.0
area=pai*(r**2)
print(f"半径为{r}的圆的面积为{area}")


#input函数用法
#input() 函数可以让用户输入数据，输入的数据类型为字符串类型
user_name=input("请输入你的名字：")
print(f"你好,{user_name}!")


#input返回的是字符串类型，要转成数字必须要用int（）或float（）
age_str=input("请输入你的年龄：")
age=int(age_str)
print(f"你的年龄为{age}岁")
print(f"你明年的年龄为{age+1}岁")


#检验自己：写一个程序，让用户输入两个数字，程序输出它们的和
num1_str=input("请输入一个数字:")
num1=float(num1_str)
num2_str=input("请输入另一个数字：")
num2=float(num2_str)
print(f"这两个数字的和为：{num1 + num2}")


# if/else/elif语句
score=int(input("请输入你的分数:"))
if scor>=90:
    print("优秀")
elif score>=80:
    print("良好")
elif score>=60:
    print("及格")
else :
    print("不及格")


#检验自己：写一个"是否是闰年"的判断程序
#闰年的判断规则：
#1.年份能被4整除但不能被100整除的为闰年
#2.年份能被400整除的为闰年
year=int(input("请输入年份为："))
if (year%4==0 and year%100!=0) or(year%400==0):
    print(f"{year}为闰年")
else:
    print(f"{year}不是闰年")


#for循环
for i in range(5):
    print(f"第i次循环")


#遍历列表
fruits=["苹果","香蕉","橘子"]
for fruit in fruits:
    print(f"我喜欢吃的水果是：{fruit}")


#while循环
count=0
while count<5:
    print(f"第{count}次循环")
    count+=1


#break语句和continue语句
for i in range(10):
    if i==4:
        continue
    if i==7:
        break
    print(i)


#检验自己：用 for 循环打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}",end="\t")
    print()  # 换行
#random模块
#要使用random模块来生成随机数，必须要先引用这个模块，使用 import random 语句来导入这个模块
# 调用这个模块的函数来生成随机数，格式为：random.函数名()
#函数名包括：random（）——表示生成   一个0.0到1.0之间的随机小数
#randint（a,b）——表示生成一个a到b之间的随机整数
#randrange（a,b）——表示生成一个a到b之间的随机整数，左闭右开区间
#from ...import ... 语句可以导入模块中的指定函数，使用时不需要加模块名
#eg:from random import randint     random_int = randint(1, 10)     print(random_int)




#项目一：猜数字游戏
#游戏规则：

#程序随机生成一个 1-100 之间的整数
#用户猜数字
#程序提示"大了"或"小了"
#猜中后显示"恭喜，你猜了 X 次"
#   拆解提示
#用 random.randint(1, 100) 生成目标数字
#用一个变量 guess_count = 0 记录猜的次数
#用 while True: 做无限循环
#每次循环：让用户输入数字 → 计数 +1 → 判断大小
#猜对了就 break


import random
num_to_guess=random.randint(1,100)
guess_count=0
num=int(input("请输入你猜的数字："))
while True:
      guess_count+=1
      if num<num_to_guess:
          print("小了")
      elif num>num_to_guess:
          print("大了")
      else:
          print(f"恭喜，你猜了 {guess_count} 次")
          break        