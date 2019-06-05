# 1.写出列表、元组、字典的生成式
list01 = [x for x in range(10)]
tuple01 = (y for y in range(10))
dict01 = {keys: None for keys in list01}

# 2.把如下的内容进行反转
#     原字符串: this is my house
#     转换后的: house my is this
sentence = "this is my house"
word = sentence.split()
revers = ""
i = len(word) - 1
while i >= 0:
    revers += word[i] + " "
    i -= 1
print(revers)

# 3.实现一个搜索引擎, 当搜索到"苍老师"、"波多野结衣"、"小泽玛利亚"等特殊字符时
# 对所搜内容进行隐藏.
search = input('''
        -| Google Search |-
        Please Input: ''')
if "苍" in search:
    w = search.replace("苍", "*")
    print(w)
elif "波多野结衣" in search:
    w = search.replace("波多野结衣", "*****")
    print(w)
elif "小泽玛利亚" in search:
    w = search.replace("小泽玛利亚", "*****")
    print(w)
else:
    print(search)


# 4. 把字典中的内容输出到文件中
information = {
    "China":
        {
            "People": 1300000000,
            "Area": 9600000
        },
    "Korea":
        {
            "People": 20000000,
            "Area": 20000
        }
}
with open("./information", "w") as file:
    info = str(information)
    file.write(info)




