prices = [7, 2, 1, 5, 6, 4, 8]

n = len(prices)
max_profit = 0
for i in range(0, n):
    for j in range(i+1, n):
        if prices[j] > prices[i]:
            p = prices[j] - prices[i]
            max_profit = max(max_profit, p)
print(max_profit)

#TC -> O(n(N+2)/2) similar to O(N**2)
#SC -> O(1)
