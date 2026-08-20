# Binary Search(1D Arrays)
# LeetCode 33 - Search in Rotated Sorted Array I

# nums = [1, 4, 5, 6, 8, 9, 10, 11, 15, 20]
# Rotate array 3 times
# nums = [11, 15, 20, 1, 4, 5, 6, 8, 9, 10]
# target = 15  target = 9  target = 13 
# -> 1         -> 8        -> -1

nums = [11, 15, 20, 1, 4, 5, 6, 8, 9, 10]
target = 8

def search(nums, target):
    n = len(nums)
    for i in range(0, n):
        if nums[i] == target:
            print(i)
    return -1

search(nums, target)

# TC -> O(N)
# SC -> O(1)
