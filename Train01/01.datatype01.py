# 字符串、整型、浮点型、布尔值类型
#

# 整型数据
a = 24
b = 9

print(a % b)
print(a // b)

# 布尔值类型and、or、not
print(True and False)
print(True or False)

# 字符串类型
str01 = "hello world"
str02 = "this is my dog"

print(str01[2:5])
print(str01*20)
print(str01 + " " + str02)

number = str01.count('o')
print(number)

index = str01.index('o')
print(index)

str01_replace = str01.replace('o', '0', 2)
print(str01_replace)

str01_split = str01.split()
print(str01_split, type(str01_split))

del str01
