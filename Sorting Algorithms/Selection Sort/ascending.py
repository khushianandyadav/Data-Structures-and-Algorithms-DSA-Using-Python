nums = [5, 7, 8, 4, 1, 6, 9, 2]

def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        mini_ind = i
        for j in range(i+1, n):
            if nums[j] < nums[mini_ind]:
                mini_ind = j
        nums[i], nums[mini_ind] = nums[mini_ind], nums[i]

selection_sort(nums)
print(nums)


# TC -> O(N((N+1)/2)) almost -> O(N**2)
# SC -> O(1)

