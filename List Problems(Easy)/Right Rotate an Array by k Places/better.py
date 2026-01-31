#Better Solution - Using Slicing

nums = [3, 9, 5, 6, 1, 4, 2, 8]
k = 6
n=len(nums)
k = k%n

nums[:] = nums[n-k:] + nums[:n-k]

print(nums)

'''
TC -> O(N)
SC -> O(1)
'''