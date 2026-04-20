nums = [[5, 10, 3], [8, 7, 1], [9, 6, 2]]

rows = len(nums) 
cols = len(nums[0])
for i in range(0, rows):
    for j in range(0, cols):
        if i == j:
            print(nums[i][j], end = " ")
        else:
            print("*", end = " ")

    print()