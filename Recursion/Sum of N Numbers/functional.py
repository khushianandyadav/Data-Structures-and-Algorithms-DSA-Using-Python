def func(N):
    if N == 1:
        return 1
    return N + func(N - 1)

x = func(15)
print(x)