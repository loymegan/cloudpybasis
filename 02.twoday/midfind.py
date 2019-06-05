# author: bavdu
# email: bavduer@163.com
# date: 2019/06/03
# usage: study midfind.



list01 = [45, 38, 21, 75, 90]
list02 = [45, 38, 21, 75, 90]
for i in range(len(list01)):
    for j in range(len(list01)):
        if list01[i] < list01[j]:
            list01[i], list01[j] = list01[j], list01[i]
print(list01)

search = int(input("please Input: "))
zindex = 0
yindex = len(list01) - 1
while yindex - zindex >= 0:
    mid = (zindex + yindex) // 2
    if list01[mid] > search:
        yindex = mid - 1
    elif list01[mid] == search:
        print(list02.index(search))
        break
    elif list01[mid] < search:
        zindex = mid + 1