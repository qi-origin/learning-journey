#命令行天气查询工具
import requests
city=input("请输入城市名：")
url=f"https://wttr.in/{city}?format=json"
response = requests.get(url)
data=response.json()
#提取当前天气
current=datadata["current_condition"][0]
temp=current["temp_C"]
humidity = current["humidity"]
desc = current["weatherDesc"][0]["value"]
print(f"\n{city} 当前天气：")
print(f"温度：{temp}°C")
print(f"湿度：{humidity}%")
print(f"天气：{desc}")