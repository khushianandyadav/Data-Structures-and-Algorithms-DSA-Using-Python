nums = [33, 67, 89, -81, 777, 123]

largest = nums[0]
n = len(nums)
for i in range(0, n):
    if nums[i] > largest:
        largest = nums[i]
print(largest)
