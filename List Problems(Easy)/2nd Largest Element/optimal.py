nums = [-55, -56, -13, -12, 11, -67, -3, -1]
n = len(nums)
largest = float("-inf")
s_largest = float("-inf")

for i in range(0, n):
    if nums[i] > largest:
        s_largest = largest
        largest = nums[i]
    elif nums[i] > s_largest and nums[i] != largest:
        s_largest = nums[i]
print(s_largest)

'''
TC -> O(N)
SC -> O(1)

'''