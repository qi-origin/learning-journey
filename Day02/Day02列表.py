#创建列表
students=["张三","李四","王五"]
print(students)


#索引(从0开始)
print(students[0])
print(students[-1])#(-1表示从最后一个元素开始索引)


#切片
print(students[0:2])#从索引0开始到索引2结束（不包括索引2），只有0和1位置上的元素


#添加元素
students.append("赵六")#在列表最后位置添加  
students.insert(1,"孙七")#在列表索引1的位置添加
print(students)


#删除元素
students.remove("李四")
students.pop(0)#删除索引0处的元素


#修改元素
students[0]="周八"


#查找
print(len(students))#获取列表长度
print("王五"in students)#判断元素是否在列表中,回答true或false
print(students.index("王五"))#index()获取元素在列表中的索引位置


#遍历
for student in students:
    print(student)


#带着索引的遍历
for i ,student in enumerate(students):
    print(f"{i}:{student}")


#检验自己：不查资料，写一个程序——创建一个空列表，让用户循环输入 5 个名字，然后打印列表的长度和内容。
names=[]
for i in range(5):
    names.append(input())
print(len(names))
print(names)