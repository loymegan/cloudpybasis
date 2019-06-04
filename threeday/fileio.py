# author: bavdu
# email: bavduer@163.com
# date: 2019/06/04
# usage: file output info


with open("information", "r+") as file:
    info = []
    table = {
        "China":
            {
                "url": None,
                "MobilePhone": None,
                "PassWord": None
            }
    }

    for line in file.readlines():
        info.extend(line.split(","))
        for element in info:
            if element[0:3] == "url":
                table["China"].update({"url": element[4:]})
            elif element[0:11] == "mobilephone":
                table["China"].update({"MobilePhone": element[12:]})
            elif element[0:3] == "pwd":
                table["China"].update({"PassWord": element[4:]})

    print(table)

