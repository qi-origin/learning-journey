#day03_main.py
from contacts_functions import (
    CONTACTS, add_contact, list_contacts, 
    search_contact, delete_contact
)
while True:
    print("\n===== 通讯录 =====")
    print("1. 添加")
    print("2. 查看")
    print("3. 搜索")
    print("4. 删除")
    print("5. 退出")
    
    choice = input("选择：")
    if choice == "1":
        name = input("姓名：")
        phone = input("电话：")
        print(add_contact(name, phone))
    elif choice == "2":
        print(list_contacts())
    elif choice == "3":
        name = input("搜索姓名：")
        result = search_contact(name)
        if result:
            print(f"{result['name']} - {result['phone']}")
        else:
            print("未找到")
    elif choice == "4":
        name = input("删除姓名：")
        print(delete_contact(name))
    elif choice == "5":
        break
