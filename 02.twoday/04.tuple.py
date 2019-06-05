# author: bavdu
# email: bavduer@163.com
# date: 2019/06/03
# usage: study tuple.


# list01 = [1, 2, "string", True]
# tuple01 = (1, 2, "string", True)
# for i in range(len(tuple01)):
#     print(tuple01[i])

# list_size = list01.__sizeof__()
# tuple_size = tuple01.__sizeof__()
# print(list_size, tuple_size)
#
# list01.append("app")
# tuple02 = tuple01 + ("app", )
# list_size = list01.__sizeof__()
# tuple_size = tuple02.__sizeof__()
# print(list_size, tuple_size)

# 声明元组
tuple01 = (1, 1, 3, 4, 6, 9, 10, 12, 1)

# 查看某个元素的索引值
print(tuple01.index(4))

# 查看元组中某个字符的个数
print(tuple01.count(1))




