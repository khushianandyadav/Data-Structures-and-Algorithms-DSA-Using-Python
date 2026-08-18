# Binary Search(1D Arrays)
# Count Occurrences of a number in a sorted array with duplicates

nums = [1, 2, 3, 3, 3, 3, 3, 5, 6, 8, 9, 9, 10]
target = 3
n = len(nums)
first =  -1
last = -1
for i in range(0, n):
    if nums[i] == target:
        if first == -1:
            first = i
        last = i
if first == -1:
    print(0)
print(last-first+1)

# TC -> O(N)
# SC -> O(1)
