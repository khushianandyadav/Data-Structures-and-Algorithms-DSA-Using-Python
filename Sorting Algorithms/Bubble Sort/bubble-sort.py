nums = [5, 8, 1, 6, 9, 2, 4]

n = len(nums)
for i in range(n-2, -1, -1):
    for j in range(0, i+1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums)


# TC -> O((N(N+1))/2) almost -> O(N**2)
# SC -> O(1)
