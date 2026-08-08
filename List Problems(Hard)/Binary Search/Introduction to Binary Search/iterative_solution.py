#Used for Searching Sorted Lists
#If target does not exist, return -1

nums = [2,4,6,7,9,11,18,19]
target = 9

def binarySearch(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binarySearch(nums, target))

#TC -> O(log base 2 (N)) ... where N is the number of elements in the list
#SC -> O(1)
