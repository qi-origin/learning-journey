#常见的异常类型D
#ValueError-值错误
try:
     num=int("abc")
except ValueError:
     print(f"值错误,无法把字符串转变为整数型")
#FileNotFoundError
try:
     with open("不存在的文件.txt")as f:
          content=f.read()
except FileNotFoundError:
      print(f"文件不存在")
# KeyError: 字典键不存在
data = {"name": "张三"}
try:
    phone = data["phone"]
except KeyError:
    print("phone 字段不存在")
#捕获多处异常
try:
     result=10/0
except ZeroDivisionError:
     print(f"不能除以0")
except Exception as e:
     print(f"其他错误:{e}")
       # ---- 通用防护 ----
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "错误：不能除以零"
    except TypeError:
        return "错误：请输入数字"

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # 错误：不能除以零
print(safe_divide("a", 2))  # 错误：请输入数字