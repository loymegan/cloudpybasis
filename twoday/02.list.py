# coding: utf-8
# author: bavdu
# email: bavduer@163.com
# date: 2019/06/01
# usage: study list.
# 列表、元组、字典、集合

# 列表定义.
list01 = ["hello", "world", "slice", "index"]

# 列表长度.
print(len(list01))

# 遍历列表.
for i in range(len(list01)):
    print(list01[i])

# 列表切片.
list02 = [1, 2, 3, 4, 5, 6, 7]
print(list02[1:3], type(list02[1:3]))
print(list02[-3:-1])

# 打印出元素的索引号.
print(list02.index(3))

# 列表添加元素<列表的长度是可以变化的>
list03 = [1, "hello", 2, "world", 3]
list03.append("kitty")
print(list03)

list04 = [3.14, True, False, "123", 123]
list03.extend(list04)
print(list03)

# 列表插入元素
list05 = [1, 2, 3, "hello", "world", 4, 5, 6]
list05.insert(1, "insert")
print(list05)

# 列表删除元素
list06 = [1, 2, 3, "hello", "world", 1, 1, 6]
print(list06.count(1))

cc = list06.count(1)
n = 0
while n < cc:
    list06.remove(1)
    n += 1
print(list06)

# list06.remove(1)
# list06.remove(1)
# list06.remove(1)

list06.pop()
print(list06)

list06.clear()
print(list06)

# 列表修改元素


# 列表生成式.

# 列表排序之冒泡排序.
# list_mao = [92, 43, 67, 23, 2, 11, 26, 79, 20, 41]
# for c in range(len(list_mao)):
#     for j in range(len(list_mao)-1):
#         if list_mao[j] > list_mao[c]:
#             list_mao[j], list_mao[c] = list_mao[c], list_mao[j]
# print(list_mao)


