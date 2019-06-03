# author: bavdu
# email: bavduer@163.com
# date: 2019/06/03
# usage: study file with func.


# file = open("./op.info", "w")
# file.writelines()
# file.close()

with open("./test.txt", "a") as file:
    file.writelines("\nAAAAA")


with open("./test.txt", "r") as file:
    for line in file.readlines():
        print(line.lower())



