s = "MALAYALAM"
n = len(s)
def func(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return func(s, left + 1, right - 1)

x = func(s, 0, n-1)
print(x)

# TC -> O(N/2) almost -> O(N)
# SC -> O(N/2) ___ Stack Space