# 列表、元组、字典、集合
#

list01 = [1, 2, 3, 4, 5]
tuple01 = (1, 2, 3, 4, 5)
dict01 = {"key01": "values01", "key02": "values02"}
set01 = {1, 1, 1, 1, 1}
# 集合中没有重复的元素, 若在声明时有多个重复的元素只显示一个

list01.append(6)
list01.insert(0, 0)
list01.extend([7, 8, 9])
list01 += [10, 11, 12]
print(list01)

list01.remove(0)
list01.pop(0)
# list01.clear()
print(list01)

list01.sort()
print(list01)

list01 = [1, 6, 2, 3, 5, 4, 0]
list01.reverse()
print(list01)

list01[0] = 10
print(list01)


keys = dict01.keys()
print(keys, type(keys))

for i in keys:
    print(i)



with open("./info.txt", "w", encoding="utf8") as file:
    file.write("information")

with open("./info.txt", "r", encoding="utf8") as file:
    text = file.read()
    print(text)






















