# 获取NameError显示的信息.
try:
    i += 1
except NameError:
    print("i is not definition.")
finally:
    print("Now! handling this error.")

# 获取ValueError and TypeError and NameError信息.
try:
    i += a
except (NameError, ValueError, TypeError):
    print("Name 'i' is not defined."
          "'a' not a type.")
finally:
    print("Now! handling this error.")

# 获取零值错误并打印其错误信息.
try:
    print(1/0)
except ZeroDivisionError as error:
    print("0 not as divisor: %s" % error)
finally:
    print("Now! handling this error.")


# 对任意错误进行捕捉.
try:
    a = 123
    a.append(456)
except Exception as error:
    print("This Error: %s" % error)
finally:
    print("Now! handling this error.")