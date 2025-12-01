def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num -1)

x = factorial(6)
print(x)