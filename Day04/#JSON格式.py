#JSON格式
import json
#python 字典 转换成JSON字符串
data1 = {
         "name":"张三",
         "age":18,
         "skills":"python,Git",
         "has_laptop":True
}
json_str=json.dumps(data,ensure_ascii=False,intend=2)
print(json_str)
#输出格式化的JSON,ensure_ascii=False——中文正常显示
#JSON字符串转python字典
import json
json_str={
    "name":"张三",
    "age":18,
    "skills":"python/Git",
    "has_latpot":true

}
data2=json.loads(json_str)
print(data2["name"])
#python字典转换成JSON文件
data1 = {
         "name":"张三",
         "age":18,
         "skills":"python,Git",
         "has_laptop":True
}
with open("data1.json","w",encoding="uft-8") as f:
     json.dump(data1,f,ensure_ascii=False,intend=4)

#从json文件中读取
data1 = {
         "name":"张三",
         "age":18,
         "skills":"python,Git",
         "has_laptop":True
}
with open("data1.json","r",encoding="uft-8") as f:
     data3=json.load(f)
print(data3["name"])
print(data3["age"])
#dumps = dump string（转成字符串）
#loads = load string（从字符串加载）
#dump = 写文件
#load = 读文件
#ensure_ascii=False = 中文正常显示，不加变成 \uXXXX
#indent=2 = 格式化，好看
