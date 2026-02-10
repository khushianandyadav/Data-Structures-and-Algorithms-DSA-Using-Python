'''
whatever n is add all elements from 0 to n...sum1
add all elements from the array...sum2
difference between sum1 and sum2 is the missing number.
formula to calculate missing numbers is (n(n+1))//2...double divide to get integer value
'''

nums = [9, 6, 8, 2, 3, 5, 7, 0, 1]
n = len(nums)

print(((n*(n+1))//2) - sum(nums))

'''
(n*(n+1))//2)...TC O(1), sum(nums)...TC O(N)

TC -> O(N)
SC -> O(1)
'''