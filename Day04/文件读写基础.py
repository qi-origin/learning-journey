#写入文件
with open("text.txt","w",encoding=utf-8) as f:
    f.write("打印第一行\n")
    f.write("打印第二行\n")
    f.write("打印第三行")


#读取文件
with open ("text.txt","r",encoding=uft-8) as f:
     content=f.read()#r是一次性读取全部的文件对象的内容
     print(content)


#逐行读取
with open("text.txt","r",encoding=uft-8) as f:
    for line in f:
        print(line.strip())#strip用来去除换行符


#读取所有行到一个列表
with open("text.txt","r",encoding=uft-8) as f:
     lines=f.readlines
     print(lines)
    

# 追加模式（不覆盖原内容）
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("这是追加的一行\n")

#"w" 模式会清空原文件，"a" 模式追加
#encoding="utf-8" 必须要，否则中文乱码
#with 语句会自动关闭文件，不用手动 f.close()

