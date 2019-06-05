# 数据类型: 整型(int)、浮点型(float)、布尔值类型(bool)、字符串类型(str=string)
int01 = 23
print(int01, type(int01))

# 求余数(%): 20对3取余
print(20 % 3)

# 求取整(//): 20对2取整
print(20 // 3)

# [1, 3, 5, 7, 9, 11, 13, 15]
# ? + ? + ? = 30
# 15 + 9.7 + 5.3 = 30

float01 = 4.445
print(float01, type(float01))

bool01 = True
bool02 = False
print(bool01, bool02, type(bool01), type(bool02))

str01 = 'Hello World'
str02 = "hello kitty"
str03 = '''
    hello:
        this is my house.
'''
# str04 = input("please Input: ")

str01_split = str01.split()
print(str01_split, type(str01_split))

str01_upper = str01.upper()
print(str01_upper)

str01_lower = str01.lower()
print(str01_lower)

str01_len = len(str01)
print(str01_len)

str_sum = str01 + " " + str02
print(str_sum)
print(len(str_sum))

print(str01)
str01_replace = str01.replace("H", "G")
print(str01_replace)