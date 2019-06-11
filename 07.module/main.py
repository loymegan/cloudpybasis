from tools import readf
from tools import asum

text = []
for line in readf("./module.txt"):
    text.append(line.strip("\n"))
print(text)

sum01 = asum(23, 46)
print(sum01)