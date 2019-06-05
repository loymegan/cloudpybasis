# author: bavdu
# email: bavduer@163.com
# date: 2019/05/31
# usage: study variables.


# define python's variables.
var01 = "hello world"
print(var01)

var02, var03, var04 = 1, "hello", "world"
print(var02, var03, var04)

var05 = var06 = 18
print(var05, var06)

# variables's values change.
var07, var08 = "hello", "world"
print(var07, var08)
var07, var08 = var08, var07
print(var07, var08)


# variables's data type.
var10, var11, var12, var13 = 18, 3.14, "string", False
print(type(var10), type(var11), type(var12), type(var13))

# int type.
var14 = -1
print(type(var14))

# str type.
var15 = '15'
print(type(var15))

var16 = "this's my dog."
print(type(var16))

# bool type.
print(True and False)
print(True or False)
print(not True)



