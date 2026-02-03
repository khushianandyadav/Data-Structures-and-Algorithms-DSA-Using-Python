#Leetcode 283

#order of the rest of the elements should remain maintained.changes should be made in place. you can take the help of other variables but at the end changes should be reflected in place.

nums = [3, 1, 0, 4, 22, 0, 8, 7, 0, 1, 0, 0, 2, 4, 5]
n = len(nums)
temp = []

for i in range(0, n):
    if nums[i] != 0:
        temp.append(nums[i])
nz = len(temp)

for i in range(0,nz):
    nums[i] = temp[i]
for i in range(nz, n):
    nums[i] = 0

print(nums)

'''
TC -> O(N+N) -> O(2N) similar -> O(N)
SC -> o(N) ... worst case if there are no 0s and temp contains same no. of elements as nums


in optimal, try to make SC O(1) and single iteration
'''
