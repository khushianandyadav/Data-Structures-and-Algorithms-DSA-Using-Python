s = "ANBCDDCBNA"

n = len(s)
left = 0
right = n-1
while left < right:
    if s[left] != s[right]:
        print(False)
    left += 1
    right -= 1
print(True)

# TC -> O(N/2) -> 1/2 * N almost -> N
# SC -> O(1)
