count = 0

def func():
    global count
    if count == 6:
        return
    count += 1
    func()
    print("Anirudh")

func()