from math import sqrt
n = 9856
num = n
result = []
for i in range(1, int(sqrt(num))+1):
    if num % i == 0:
        result.append(i)

        if num // i != i:
            result.append(num // i)
result.sort()
print(result)


# TC -> O(sqrt(N)) + O(Nlog(N))
# SC -> O(k)