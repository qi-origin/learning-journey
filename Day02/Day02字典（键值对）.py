#创建字典（键值对）

#创建字典用{}
student={
    "name":"张三",
    "age":"18",
    "major":"计算机科学"
}


#访问字典
print(student["name"])
print(student.get("age"))


#添加修改
student["phonenumber"]="100000000"#不存在phonenumber这个键的话，就是添加这个新键
student["age"]="20"#存在则修改


#删除
del student["name"]
major=student.pop("major")


#遍历
for key , value in student.items():
      print(f"{key}:{value}")


# 只遍历键
for key in student.keys():
    print(key)


# 只遍历值
for value in student.values():
    print(value)

# 检验自己：创建一个字典表示一本书（书名、作者、价格），然后打印出来
book={
     "bookname":"活着",
     "writer":"余华",
     "price":45
}
for key,value in book.items():
     print(f"{key}:{value}")


#集合set
# 集合：无序、不重复
tags = {"python", "编程", "python", "学习"}
print(tags)  # 输出：{'python', '编程', '学习'}（去重了）

tags.add("AI")       # 添加
tags.remove("python") # 删除
print("AI" in tags)  # 判断是否存在