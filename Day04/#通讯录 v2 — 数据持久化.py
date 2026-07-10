#通讯录 v2 — 数据持久化
import json
import os
DATA_FILE="contacts.json"
def load_contacts():
    if os.path.exists(DATA_FILE):
        with open("contacts.json","r",encoding="uft-8") as f:
             return json.load(f)
    else :
        return []
def save_contacts(contacts):
    with open("contacts.json","w",encoding="uft-8") as f:
        json.dump(contacts,f,ensure_ascii=False,intend=4)
 
 
contacts=load_contacts
print(f"已经保存了{len(contacts)}个联系人")
while True:
    print("\n===== 通讯录 =====")
    print("1. 添加  2. 查看  3. 搜索  4. 删除  5. 退出")
    choice=input("添加")
    if choice=="1":
        name=input("姓名")
        phone=input("电话号")
        contacts.append({"name":name,"phone":phone})
        save_contacts(contacts)
        print(f"已添加并保存：{name}")
    elif choice=="2":
        if not contacts:
            print("通讯录为空")
        else:
            for i, contact in enumerate(contacts):
                print(f"{i+1},{i}{name}:{phone}")
    elif choice=="3":
        name=input("搜索:")
        found=[c for c in contacts if c["name"]==name]
        #等价写法：
        #found=[]
        #for c in contacts: 
        #    if name==c["name"]:
        #       found.append(c)
        if found:
            print(f"{found[0]['name']} - {found[0]['phone']}")
        else:
            print("未找到")
    elif choice=="4":
        name=input("删除：")
        before=len(contacts)
        contacts=[c for c in contacts if c["name"]!=name]
        if len(contacts)<before:
            print(f"已经删除{name}")
        else:
            print(f"未找到{name}")
    
    elif choice == "5":
        break