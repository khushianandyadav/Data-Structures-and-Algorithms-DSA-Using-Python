# Leetcode 35
# Binary Search(Easy) - Search Insert Position

nums = [1, 3, 4, 5, 8, 9, 14, 15, 19, 20, 21]
target = 7
n = len(nums)

lb = n
low = 0
high = n - 1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] >= target:
        lb = mid
        high = mid - 1
    else:
        low = mid + 1
print(lb)

# TC -> O(log2 n)
# SC -> O(1)