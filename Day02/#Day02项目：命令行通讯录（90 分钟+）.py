#今日项目：命令行通讯录（90 分钟+）
#功能要求：

#显示菜单（1.添加 2.查看全部 3.搜索 4.删除 5.退出）
#添加联系人：输入姓名、电话
#查看全部联系人
#按姓名搜索联系人
#删除联系人
#循环运行直到用户选择退出
contacts = []
while True:
    print("\n===== 通讯录 =====")
    print("1.添加联系人")
    print("2.查看全部联系人")
    print("3.搜索联系人")
    print("4.删除联系人")
    print("5.退出通讯录")
    choice = int(input("请选择你的操作："))
    if choice == 1:
        name = input("姓名：")
        phone = input("电话：")
        contacts.append({"name": name, "phone": phone})
        print(f"已添加 {name}")
    elif choice == 2:
        if contacts == []:
            print("通讯录中没有联系人")
        else:
            for i, contact in enumerate(contacts):
                print(f"{i + 1}. {contact['name']}: {contact['phone']}")
    elif choice == 3:
        search_name = input("请输入您要搜索的联系人：")
        found = False
        for contact in contacts:
            if search_name == contact["name"]:
                print(f"找到了 {contact['name']}: {contact['phone']}")
                found = True
                break
        if not found:
            print("未找到")
    elif choice == 4:
        del_name = input("请输入你要删除的联系人：")
        found = False
        for contact in contacts[:]:
            if del_name == contact["name"]:
                contacts.remove(contact)
                print(f"已删除 {del_name}")
                found = True
                break
        if not found:
            print("找不到您要删除的联系人")
    elif choice == 5:
        print("退出通讯录")
        break
    else:
        print("输入错误,请输入1 - 5之间的数字")