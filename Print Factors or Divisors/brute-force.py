n = 900
num = n
result = []
for i in range(1, num + 1):
    if num % i == 0:
        result.append(i)
print(result)

# TC -> O(N)
# SC -> O(k) ___ k would be the total no. of factors
