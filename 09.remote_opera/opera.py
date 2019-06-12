# python中的错误处理try-except-finally

# FileNotFoundError
# with open("./info.json", "r", encoding="utf8") as file:
#     file.read()

# NameError
# print(a)

# ZeroDivisionError
# print(1/0)
import sys
import os

try:
    with open('./info.json', 'r', encoding='utf8') as file:
        text = file.read()
        print(text)
except Exception as error:  # Exception是python中所有错误类型的基类.
    # print("This program run ERROR: {}".format(error))
    os.system('bash ziyu.sh')
finally:
    print("error already output")
    # if os.system('') == 0:
    #     email
    # else:
    #     logging

print("go on...")
sys.exit(23)
