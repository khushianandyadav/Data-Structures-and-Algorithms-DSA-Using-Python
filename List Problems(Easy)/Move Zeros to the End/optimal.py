nums = [44, 1, 0, 8, 0, 0, 443, 1,2 , 7, 0, 8, 4, 0, 5, 0, 11]

if len(nums) == 1:
    print(nums)

i = 0

while i<len(nums):
    if nums[i] == 0:
        break
    i += 1

if i == len(nums):
    print(nums)

j = i + 1

while j < len(nums):
    if nums[j] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
    j += 1


print(nums)