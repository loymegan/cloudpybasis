# author: bavdu
# email: bavduer@163.com
# date: 2019/06/04
# usage: file output info


# 第一道题: 把文件中的信息输出到下面的字典中
information = {
    "China":
        {
            "URL": None,
            "UserName": None,
            "PassWord": None
        },
    "Sydney":
        {
            "URL": None,
            "UserName": None,
            "PassWord": None
        },
    "NewYork":
        {
            "URL": None,
            "UserName": None,
            "PassWord": None
        }
}

with open("information", "r+") as file:
    for line in file.readlines():
        tlist = line.split(",")
        if tlist[0][0:5] == "China":
            information["China"]["URL"] = tlist[0][11:]
            information["China"]["UserName"] = tlist[1][9:]
            information["China"]["PassWord"] = tlist[2][9:]
        elif tlist[0][0:6] == "Sydney":
            information["Sydney"]["URL"] = tlist[0][11:]
            information["Sydney"]["UserName"] = tlist[1][9:]
            information["Sydney"]["PassWord"] = tlist[2][9:]
        elif tlist[0][0:7] == "NewYork":
            information["NewYork"]["URL"] = tlist[0][11:]
            information["NewYork"]["UserName"] = tlist[1][9:]
            information["NewYork"]["PassWord"] = tlist[2][9:]
print(information)



info = []
info.append(
    {'192.168.1.11':
         {
            'cpu': ['Intel(R) Core(TM) i5-5350U CPU @ 1.80GHz', 4, 1],
            'memory': ['16', '4', '2'],
            'disk': ['1T', '2T']
         }
    })

info.append({
    '192.168.1.12': {
         'cpu': ['Intel(R) Core(TM) i5-5350U CPU @ 1.80GHz', 4, 1],
         'memory': ['16', '4', '2'],
         'disk': ['1T', '2T']
    }
})

print(info[0]["192.168.1.11"]["disk"][0])



username = input("Please input your name: ")
password = input("Please input your passwd: ")

if username == "yangge" or username == "shark":
    if password == "123":
        print("load successfully.")
    else:
        print("password not true.")
else:
    print("No such user.")
















