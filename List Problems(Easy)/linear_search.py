'''
you are given an array and a target element. you have to return index of the target element. 
in case of  duplicates(target element exists more than one time in the array), return first
occurrence. in case target does not exist, return -1.
'''

nums = [5, 3, 1,9, 8, 6, 4, -10, -100]

target = 4

n = len(nums)
for i in range(0, n):
    if nums[i]==target:
        print(i)
        break
else:
    print(-1)

'''
TC -> O(n)
SC -> O(1)
'''