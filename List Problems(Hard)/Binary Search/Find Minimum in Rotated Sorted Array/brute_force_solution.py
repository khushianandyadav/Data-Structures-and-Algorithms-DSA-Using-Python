# Binary Search(1D Arrays) LeetCode 153
# Find Minimum in Rotated Sorted Array

# nums = [4, 5, 6, 7, 0, 1, 2]
# -> 0 __ minimum

nums = [4, 5, 6, 7, 0, 1, 2]
n = len(nums)
mini = float("inf")
for i in range(0, n):
    mini = min(mini, nums[i])
print(mini)

# TC -> O(N)
# SC -> O(1)
