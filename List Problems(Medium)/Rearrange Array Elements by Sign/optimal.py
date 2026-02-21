nums = [3, -12, -17, 15, -14, 12, 9, -6]

n = len(nums)
result = [0] * n
posIndex, negIndex = 0, 1
for i in range(0, n):
    if nums[i] >= 0:
        result[posIndex] = nums[i]
        posIndex += 2
    else:
        result[negIndex] = nums[i]
        negIndex += 2

print(result)

#TC -> O(N)
#SC -> O(1) bc u are using array elements
#else SC -> O(N)