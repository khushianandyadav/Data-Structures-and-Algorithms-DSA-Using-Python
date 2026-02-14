# LeetCode 1
# given an array and a target element
# return indexes of the two elements from array whose sum is target
# only use one element once
# only one solution exists


nums = [5, 9, 1, 2, 4, 15, 6, 3]

target = 13

n = len(nums)

for i in range(0, n-1):
    for j in range(i+1, n):
        if nums[i] + nums[j] == target:
            print([i, j])

'''
TC -> O(N(N+1)/2) similar to O(N**2)
SC -> O(1)
'''
