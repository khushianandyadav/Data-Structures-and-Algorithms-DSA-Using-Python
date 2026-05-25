# LeetCode 48

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

n = len(matrix)
result = [[0 for _ in range(n)] for _ in range(n)]
for i in range(0, n):
    for j in range(0, n):
        result[j][(n-1)-i] = matrix[i][j]
for row in result:        
    print(row)
