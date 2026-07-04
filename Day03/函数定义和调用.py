#函数
#基本函数
def greet(name):
    """这是一个问候函数"""#这是文档字符串用来说明函数的作用
    return f"你好,{name}"  


#调用函数
result=greet("小明")
print(result)


#多个参数
def add(a,b):
    return a+b
print(add(3,5))#结果为8


#默认参数
def greet_tltle(name,title="同学"):
    return f"你好，{name}{title}"
print(greet_title("小明"))
print(greet_title("雷军","企业家"))#默认值可以被修改，如果不修改默认值，就自动提供默认值


#无返回值的函数
def print_menu():
    print("1. 添加")
    print("2. 删除")
    print("3. 退出")

print_menu()#无返回值的函数运行结果都是None

#检验自己：写一个函数 max_of_three(a, b, c)，返回三个数中最大的那个。
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# 调用函数并传入具体参数
result = max_of_three(10, 20, 30)
print(result)  





    
    
    