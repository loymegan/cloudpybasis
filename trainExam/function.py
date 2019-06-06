def Println(number):
    if number <= 0:
        print("number <= 0")
    def inner(number):
        if number <= 1:
            return 1
        return number + inner(number - 1)
    return inner(number)


print(Println(3))