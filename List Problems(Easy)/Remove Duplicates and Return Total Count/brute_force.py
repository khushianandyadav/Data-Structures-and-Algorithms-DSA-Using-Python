'''
***********************************************************************************************
Remove Duplicates from Sorted Array(IN PLACE) and also Return Total Count of Unique Elements
************************************************************************************************
leetcode problem says unique elements from the array should come to the start and it doesn't
matter what you fill the remaining spaces with.
dictionary's add, update, etc functions have SC -> O(1) (on an average) 
'''

nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]

n = len(nums)
freq_map = {}

for i in range(0, n):
    freq_map[nums[i]] = 0

j = 0
for k in freq_map:
    nums[j] = k
    j += 1

print(nums)
print(j)

'''
TC -> O(2N) similar to O(N)
SC -> O(N)

for optimal we will try to make SC -> O(1) and TC(precise) ->  O(N) ...ie such that it will
be solved in single pass
'''
