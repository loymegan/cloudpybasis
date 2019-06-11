from sub import tools


n = tools.recursive(10)
print(n)

t01 = tools.openfile("./module.txt")
t02 = []
for element in t01:
    t02.append(element.strip("\n"))
print(t02)


file01 = tools.Doc("Git.md", "30M", 644, "file", "/Users/chaoliu/Documents/Other")
file01.getSize()

