
from math import *

n = 24963529
def countDigits(num):
    return int(log10(num)+1)

print(countDigits(n))


# TC -> O(log10(N))
# SC -> O(1)