nums = [3, 4, 5, 6, 8, 9, 10, 7, 1]

n = len(nums)
for i in range(1, n):
    key = nums[i]
    j = i-1

    while j>=0 and nums[j] > key:
        nums[j+1] = nums[j]
        j -= 1
    nums[j + 1] = key 

print(nums)

#TC -> O((N(N+1)/2)) almost-> O(N**2)
#SC -> O(1)
'''


## 🔢 Initial Array

```
nums = [3, 4, 5, 6, 8, 9, 10, 7, 1]
```

Index positions:

```
 0  1  2  3  4  5   6   7  8
```

---

## 🔁 Outer Loop Starts

```python
for i in range(1, n):
```

We start from index **1** because index `0` is already considered sorted.

---

## ▶️ Iteration 1: i = 1

```python
key = nums[1] = 4
j = 0
```

Compare:

* `nums[0] = 3 > 4` ❌ → false

No shifting needed.

Array remains:

```
[3, 4, 5, 6, 8, 9, 10, 7, 1]
```

---

## ▶️ Iteration 2: i = 2

```python
key = 5
j = 1
```

Compare:

* `nums[1] = 4 > 5` ❌

No shift.

```
[3, 4, 5, 6, 8, 9, 10, 7, 1]
```

---

## ▶️ Iteration 3: i = 3

```python
key = 6
j = 2
```

Compare:

* `nums[2] = 5 > 6` ❌

No shift.

```
[3, 4, 5, 6, 8, 9, 10, 7, 1]
```

---

## ▶️ Iteration 4: i = 4

```python
key = 8
j = 3
```

Compare:

* `nums[3] = 6 > 8` ❌

No shift.

```
[3, 4, 5, 6, 8, 9, 10, 7, 1]
```

---

## ▶️ Iteration 5: i = 5

```python
key = 9
j = 4
```

Compare:

* `nums[4] = 8 > 9` ❌

No shift.

```
[3, 4, 5, 6, 8, 9, 10, 7, 1]
```

---

## ▶️ Iteration 6: i = 6

```python
key = 10
j = 5
```

Compare:

* `nums[5] = 9 > 10` ❌

No shift.

```
[3, 4, 5, 6, 8, 9, 10, 7, 1]
```

---

## ▶️ Iteration 7: i = 7

```python
key = 7
j = 6
```

### Shifting starts:

* `nums[6] = 10 > 7` ✅ → shift

```
[3, 4, 5, 6, 8, 9, 10, 10, 1]
```

* `nums[5] = 9 > 7` ✅

```
[3, 4, 5, 6, 8, 9, 9, 10, 1]
```

* `nums[4] = 8 > 7` ✅

```
[3, 4, 5, 6, 8, 8, 9, 10, 1]
```

* `nums[3] = 6 > 7` ❌ → stop

Insert key:

```python
nums[4] = 7
```

Array becomes:

```
[3, 4, 5, 6, 7, 8, 9, 10, 1]
```

---

## ▶️ Iteration 8: i = 8

```python
key = 1
j = 7
```

### Shifting (worst case):

* 10 > 1 → shift
* 9 > 1 → shift
* 8 > 1 → shift
* 7 > 1 → shift
* 6 > 1 → shift
* 5 > 1 → shift
* 4 > 1 → shift
* 3 > 1 → shift

Final insert:

```python
nums[0] = 1
```

Array becomes:

```
[1, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

## ✅ Final Output

```python
[1, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

## 🧠 Why this is Insertion Sort

* Left part is **always sorted**
* Each new element is **inserted into its correct position**
* Similar to how you sort cards in your hand 🃏


'''