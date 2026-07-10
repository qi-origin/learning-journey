import requests
#GET请求获取数据
response=requests.get("https://v1.hitokoto.cn/")
data=response.json()
print(data["hitokoto"])
print(f"来自：{data['from']}")
# ---- 带参数的 GET 请求 ----
response = requests.get("https://api.ipify.org?format=json")
print(f"你的公网 IP 是：{response.json()['ip']}")
# ---- 查看响应详情 ----
url = "https://v1.hitokoto.cn/"
response = requests.get(url)
print(f"状态码：{response.status_code}")
print(f"响应头：{response.headers['Content-Type']}")
print(f"原始文本：{response.text[:100]}...")  # 前 100 个字符
print(f"JSON 数据：{response.json()}")
# ---- POST 请求：提交数据 ----

# 免费测试 API：JSONPlaceholder
data_to_send = {
    "title": "我的第一篇帖子",
    "body": "这是内容",
    "userId": 1
}
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data_to_send
)
print(f"POST 状态码：{response.status_code}")
print(response.json())
# ---- 错误处理 ----
try:
    response = requests.get("https://httpstat.us/404")
    response.raise_for_status()  # 状态码不是 200 就抛异常
except requests.exceptions.RequestException as e:
    print(f"请求失败：{e}")

