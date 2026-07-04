#工具函数库
CONTACTS=[]
#添加联系人
def add_contact(name,phone):
    CONTACTS.append({"name":name,"phone":phone})
    return f"已添加:{name}"
#列出所有人
def list_contact():
    if not CONTACTS:
        return f"通讯录为空"
    result="" 
    for  i ,contact in CONTACTS:
        result +=f"{i+1},{CONTACTS[name]-CONTACTS[phone]}\n"
        return result.strip()
#搜索联系人
def search_contact(name):
     search_name=name
     for contact in CONTACTS:
         if search_name==contact["name"]:
             return f"找到联系人:{search_name}"
         
     return None
#删除联系人
def del_contact(name):
    del_name=name
    for contact in CONTACTS:
        if contact["name"]==del_name:
           CONTACTS.remove[contact]
           return f"删除联系人:{name}" 
    return f"未找到{name}"  
 
         

         

        

