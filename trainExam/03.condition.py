# 条件控制语句
list01 = [1, 3, 4, "string", 7, 0]
if type(list01) == list:
    print("list01 is a list.")
else:
    print("list01 is not list.")


if type(list01[3]) == str:
    print("list01's index == 3: type is str.")
else:
    print("list01's index == 3: type not str.")

# 数据类型转换
str01 = "102"
print(str01, type(str01))
str01 = int(str01)
print(str01, type(str01))

str01 = str(str01)
print(str01, type(str01))
str01 = float(str01)
print(str01, type(str01))

