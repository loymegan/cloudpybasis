# 遍历列表for
list01 = [i for i in range(10)]
list02 = []
for i in list01:
    if i == 0:
        continue
    elif i % 2 == 0:
        list02.append(i)
print(list02)


# 遍历元组while
list01 = [i for i in range(10)]
list03 = []
n = 0
while n < len(list01):
    if list01[n] == 0:
        n += 1
        continue
    elif list01[n] % 2 == 1:
        list03.append(list01[n])
    n += 1
print(list03)

tuple01 = tuple(list03)
print(tuple01)

list04 = list(tuple01)
print(list04)

set01 = set(list03)
print(set01)

dict01 = {keys: None for keys in list03}
print(dict01)




