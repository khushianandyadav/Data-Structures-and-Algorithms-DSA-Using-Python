#LeetCode 268
#Find Missing Number in an Array

'''
Suppose nums = [1, 0, 3, 4] and no of elements n = 4
0 to 4 is 0, 1, 2, 3, 4. Out of these, 2 is missing in the array. So code should return 2.
n is not given in the question, only the array is given
'''

#for i in range(0, n=1)..loop runs till n


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

n = len(nums)
for i in range(0, n+1):    #TC->O(N)
    if i not in nums:      #TC->O(N)
        print(i)

'''
TC -> O(N**2)
SC -> O(1)

for better solution, there is the use of dictionary.
'''

