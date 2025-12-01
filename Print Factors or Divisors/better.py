n = 6000
num = n
result = []
for i in range(1, num//2):
    if num % i == 0:
        result.append(i)
result.append(num)
print(result)

# TC -> O(N/2) almost = O(N)
# SC -> O(k)