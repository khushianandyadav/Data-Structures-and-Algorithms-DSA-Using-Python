n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10, 11, 112, 9]
m = [10, 111, 1, 9, 5, 67, 2, 16, 88]
hash_map = dict()
for i in range(0, len(n)):
    hash_map[n[i]] = hash_map.get(n[i], 0) + 1
for x in m:
    print(x, hash_map.get(x, 0))