
# string字符串操作
# var01 = "string"
# print(var01, type(var01))
#
# var02 = "a b c d e f g"
# for i in range(len(var02)):
#     print(var02[i])
#
# print(var02[2:5])
#
# var03 = var02.upper()
# print(var03)
#
# var04 = var02.replace("c", "G")
# print(var04)
#
# var05 = var02.strip("a")
# print(var05)
#
# var06 = var02.split(" ")
# print(var06, type(var06))


# list列表
# list01 = [1, 3.14, "string", False]
#
# for i in list01:
#     print(i)
#
# print(list01[1:3])
#
# # append, insert, extend
# list01.append(23)
# print(list01)
#
# list01.insert(2, "hello")
# print(list01)
#
# list02 = [1, 2, 3]
# list01.extend(list02)
# print(list01)
#
#
# # remove, pop, clear
# list01.remove("string")
# print(list01)
#
# list01.pop(2)
# print(list01)
#
# # list01.clear()
# # print(list01)
#
#
# # index, count
# index = list01.index(3.14, 0, 3)
# print(index)
#
# count = list01.count(1)
# print(count)
#
# list03 = [28, 34, 12, 1, 0, 45]
# list03.sort()
# print(list03)


# tuple元组
tuple01 = (1, 2, 3, 4, 5, 1)

# count, index
print(tuple01.count(1))
print(tuple01.index(5))

# for, while对元组进行遍历.
for element in tuple01:
    print(element)

n = 0
while n < len(tuple01):
    print(tuple01[n])
    n += 1


# file文件读写.
with open("./test.txt", "r") as file:
    txt = file.readlines()
    print(txt)






































