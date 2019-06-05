# author: bavdu
# email: bavduer@163.com
# date: 2019/06/04
# usage: study set.


# 声明一个集合
set01 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set02 = {"string", "int", "float", "bool"}
set03 = {3.14, 4.445, 9.3, 290.00}
set04 = {True, False}

# 在集合中增加元素
set01.add(10)
print(set01)

set01.update([11, 22, 33, 44])
print(set01)

list01 = [1, 2, 3, 4, 5]
set01.update(list01)
print(set01)


# 在集合中删除元素
set01.pop()
print(set01)

set01.remove(22)
print(set01)

set01.discard(77)
print(set01)


# 集合是不支持索引的.
for i in set01:
    print(i)

# 集合的生成式.
set05 = {i for i in range(10) if i % 2 == 0}
print(set05)

# 集合交并集.
set06 = {1, 2, 3, 5, 8, 0}
set07 = {4, 3, 2, 1}

print("set06与set07取交集: ", set06 & set07)
print("set06与set07取并集: ", set06 | set07)






