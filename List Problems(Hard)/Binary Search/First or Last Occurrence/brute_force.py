# Binary Search(1D Array) - LeetCode 34
# Find the first or last occurrence of a given number in a sorted array.

nums = [1, 2, 3, 3, 3, 3, 3, 5, 6, 7, 8, 9, 9, 10]
target = 3
n = len(nums)
first = -1
last = -1
for i in range(0, n):
    if nums[i] == target:
        if first == -1:
            first = i
        last = i
print([first, last])

