nums = [5, 7, 8, 4, 1, 6, 9, 2]

def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        maxi_ind = i
        for j in range(i+1, n):
            if nums[j] > nums[maxi_ind]:
                maxi_ind = j
        nums[i], nums[maxi_ind] = nums[maxi_ind], nums[i]

selection_sort(nums)
print(nums)
