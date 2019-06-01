# coding: utf-8
# author: bavdu
# email: bavduer@163.com
# date: 2019/06/01


# var01 = "#!hello world!#"
# print(var01)

# var02, var03, var04 = "hello", "world", "kitty"
# print(var02, var03)
# print(var02, var04)

# var05 = var06 = var07 = var08 = 18

# var09, var10 = "100", "hello"
# print(var09, var10)
# var09, var10 = var10, var09
# print(var09, var10)


# for i in range(100):
#     print(i)

# n = 0
# while n < 100:
#     print(n)
#     n += 1

# age = 18
# if age < 20:
#     print("your young")
# else:
#     print("your old")

# 求1-100里面所有的偶数.
n = 1
while n < 101:
    if n % 2 == 0:
        print(n)
    n += 1

for i in range(1, 101):
    if i % 2 == 0:
        print(i)


# 求既能被2整除又能被3整除的数字, 范围是:1--100
for i in range(1, 101):
    if i % 2 == 0:
        if i % 3 == 0:
            print(i)

for i in range(1, 101):
    if i % 2 == 0 and i % 3 == 0:
        print(i)












