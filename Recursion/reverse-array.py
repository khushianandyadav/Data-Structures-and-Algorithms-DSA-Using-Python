arr = [2, 3, 4, 1, 7, 6, 3, 8, 9, 5]

def func(nums, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    func(arr, left + 1, right - 1)


def reverseArray(nums, l, r):
    func(nums, l, r)
    return nums

print(reverseArray(arr, 0, len(arr) - 1))
