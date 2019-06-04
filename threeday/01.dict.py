# author: bavdu
# email: bavduer@163.com
# date: 2019/06/04
# usage: study dict.


dict01 = {"key01": "string", "key02": "values"}

dict02 = {
    "dashixiong":
        {
            "grade": 98,
            "sex": "Man",
            "YMD": 20180604
         },
    "ershixiong":
        {
            "grade": 100,
            "sex": "Woman",
            "YMD": 20190604
        }
}

dict03 = {
    "cloud1903":
        {
            "People": ["dashixiong", "ershixiong", "Pge"],
            "YMD": (20180604, 20190604, 20200604),
            "Grade": True
        }
}

# 求字典dict01的长度
print(len(dict01))

# 在字典dict01中增加键值对.
dict01["key03"] = "add"
print(dict01)

dict01.setdefault("key04", "setdeault")
print(dict01)

dict01.setdefault("key05", "many01")
print(dict01)

# 删除dict01中的键值对.
del dict01["key04"]
print(dict01)

dict01.pop("key01")
print(dict01)

dict01.popitem()
dict01.popitem()
print(dict01)


# 修改dict01中的值.
dict01["key02"] = 99.999
print(dict01)

dict01.update({"key02": "update"})
print(dict01)
dict_test = {"key02": "updates", "key03": "opera"}
dict01.update(dict_test)
print(dict01)

dict01.update({"key04": "updates"})
print(dict01)


# 字典dict01遍历查询
# print(dict01.get("key04"))
# print(dict01.keys())
# print(dict01.values())
# print(dict01.items())


# 对dict01中所有的key进行遍历,使用for循环.
for key in dict01.keys():
    print(key)

# 对dict01中所有的值进行遍历,使用for循环.
for values in dict01.values():
    print(values)

# 遍历dict01中的键值对.
for kv in dict01.items():
    print(kv, type(kv))


# 遍历dict01字典中所有的值
for key in dict01:
    print(key, dict01[key])


# 字典生成式01
list01 = ["key01", "key02", "key03", "key04", "key05"]
dict04 = {}.fromkeys(list01)
print(dict04)

# 字典生成式02
dict05 = {keys: None for keys in list01}

# 字典生成式03
dict06 = {keys: 100 for keys in range(11) if keys % 3 != 0}