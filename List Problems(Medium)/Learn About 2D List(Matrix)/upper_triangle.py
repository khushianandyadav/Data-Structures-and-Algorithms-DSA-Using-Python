nums = [[5, 10, 8], [7, 6, 3], [2, 1, 9]]

row = len(nums)
cols = len(nums[0])
for i in range(0, row):
    for j in range(0, cols):
        if j >= i:
            print(nums[i][j], end = " ")
        else:
            print("*", end = " ")
    print()
    
        