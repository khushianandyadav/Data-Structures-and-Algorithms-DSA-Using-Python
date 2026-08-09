nums = [2, 4, 6, 7, 9, 11, 18, 19]
n= len(nums)
low = 0
high = n - 1

def binarySearch(nums, low, high):
    target = 7
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binarySearch(nums, mid + 1, high)
    else:
        return binarySearch(nums, low, mid - 1)
    

print(binarySearch(nums,low, high))