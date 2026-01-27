nums = [5, -2, 3, 9, 0, 6, 10, 7]
n = len(nums)
#nums = [nums[-1]] + nums[0:n-1]
#nums[:] = [nums[-1]] + nums[0:n-1]
nums[:] = [nums[n-1]] + nums[0:n-1]

print(nums)
'''
all three syntaxes work
TC -> O(1) + O(n-1) -> O(n)

'''
