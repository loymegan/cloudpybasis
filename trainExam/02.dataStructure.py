# 数据结构: 列表(list)、元组(tuple)、字典(dict)、集合(set)

# 元组
tuple01 = (1, 3.14, "string", True)

tuple01_index = tuple01.index(3.14)
print(tuple01_index)

tuple01_count = tuple01.count(1)
print(tuple01_count)

# 集合
set01 = {1, 3.14, "string", False}
set02 = {2, 4.445, "hello", True}

set01.add(2)
print(set01)

set01.remove(False)
print(set01)

set01.pop()
print(set01)

set01.update([1, 2, 3, 4])
print(set01)

set01.discard(77)
print(set01)


# 列表
list01 = [1, 3.14, "string", False]

list01.insert(0, "kitty")
list01.extend([1, 2, 3, 4])
list01.append("hello world")
print(list01)

list01.remove(1)
list01.pop(-1)
print(list01)

list01.reverse()
print(list01)

list02 = list01.copy()
print(list02)

# 字典
dict01 = {"Cpu": 8, "Mem": 16, "Disk": 2000}
dict02 = {
    "Lenovo":
        {
            "Cpu": 32,
            "Mem": 256,
            "Disk": 20000
        },
    "DELL":
        {
            "Cpu": 28,
            "Mem": 512,
            "Disk": 30000
        }
}

print(dict02["DELL"]["Cpu"])






