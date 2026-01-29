nums = [3, 9, 5, 6, 7, 2]
k=2
n = len(nums)
rotations = k%n #This line ensures the code is efficient even if k is larger than the list length.Rotating a list of length n exactly n times results in the original list.For example, if k=8 and n=6, rotating 8 times is the same as rotating 2 times 8 % 6 = 2. In your case, 2% 6=2.
for _ in range(0, rotations):
    e = nums.pop() #pops the last element k times
    nums.insert(0, e) #inserts element in e(popped element) at the start.
print(nums)

'''
TC = O(r*n) #r is no. of rotations
SC = O(1)
'''
