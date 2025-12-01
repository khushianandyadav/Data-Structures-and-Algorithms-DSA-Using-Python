def func(i, N):
    if i > N:
        return
    func(i+1, N)
    print(i)

func(1, 13)