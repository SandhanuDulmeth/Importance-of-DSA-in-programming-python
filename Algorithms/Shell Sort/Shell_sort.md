# Q1: Write a Python function to implement Shell Sort using a basic gap sequence (n//2, n//4, ... , 1).
```python
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

arr = [23, 12, 1, 8, 34, 54, 2, 3]
print(shell_sort(arr))
```

# Q2: Modify the Shell Sort algorithm to use the Knuth sequence (1, 4, 13, 40, ...).
```python
def knuth_sequence(n):
    gap = 1
    gaps = []
    while gap < n:
        gaps.append(gap)
        gap = 3 * gap + 1
    return gaps[::-1]

def shell_sort_knuth(arr):
    n = len(arr)
    gaps = knuth_sequence(n)
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    return arr

arr = [23, 12, 1, 8, 34, 54, 2, 3]
print(shell_sort_knuth(arr))
```

# Q3: Implement Shell Sort in Python without modifying the original array (return a sorted copy).
```python
def shell_sort_copy(arr):
    sorted_arr = arr[:]
    n = len(sorted_arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = sorted_arr[i]
            j = i
            while j >= gap and sorted_arr[j - gap] > temp:
                sorted_arr[j] = sorted_arr[j - gap]
                j -= gap
            sorted_arr[j] = temp
        gap //= 2
    return sorted_arr

arr = [23, 12, 1, 8, 34, 54, 2, 3]
sorted_arr = shell_sort_copy(arr)
print("Original:", arr)
print("Sorted:", sorted_arr)
```

# Q4: Implement Shell Sort and count the number of swaps performed.
```python
def shell_sort_count_swaps(arr):
    n = len(arr)
    gap = n // 2
    swap_count = 0

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                swap_count += 1
            arr[j] = temp
        gap //= 2

    return arr, swap_count

arr = [23, 12, 1, 8, 34, 54, 2, 3]
sorted_arr, swaps = shell_sort_count_swaps(arr)
print("Sorted Array:", sorted_arr)
print("Number of Swaps:", swaps)
```

# Q5: Implement Shell Sort to sort a list of strings in alphabetical order.

```python
def shell_sort_strings(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

arr = ["banana", "apple", "grape", "cherry", "mango"]
print(shell_sort_strings(arr))
```


# Q6: Implement Shell Sort with a dynamically chosen gap sequence using Sedgewick’s sequence.
```python
def sedgewick_sequence(n):
    seq = []
    k = 0
    while True:
        sedgewick = 9 * (4**k - 2**k) + 1 if k % 2 == 0 else 2**(k+2) * (2**(k+2) - 3) + 1
        if sedgewick >= n:
            break
        seq.append(sedgewick)
        k += 1
    return seq[::-1]

def shell_sort_sedgewick(arr):
    n = len(arr)
    gaps = sedgewick_sequence(n)
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    return arr

arr = [23, 12, 1, 8, 34, 54, 2, 3]
print(shell_sort_sedgewick(arr))
```

# Q7: Implement Shell Sort in Python to sort a list of tuples based on the second element.
```python
def shell_sort_tuples(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap][1] > temp[1]:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

arr = [(1, 5), (2, 3), (3, 8), (4, 1)]
print(shell_sort_tuples(arr))
```

# Q8: Implement Shell Sort for a large list and measure execution time using time module.
```python
import time
import random

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

arr = [random.randint(0, 100000) for _ in range(10000)]
start = time.time()
shell_sort(arr)
end = time.time()
print("Execution Time:", end - start)
```

# Q9: Implement Shell Sort recursively.
```python
def shell_sort_recursive(arr, gap):
    if gap == 0:
        return arr
    for i in range(gap, len(arr)):
        temp = arr[i]
        j = i
        while j >= gap and arr[j - gap] > temp:
            arr[j] = arr[j - gap]
            j -= gap
        arr[j] = temp
    return shell_sort_recursive(arr, gap // 2)

arr = [23, 12, 1, 8, 34, 54, 2, 3]
print(shell_sort_recursive(arr, len(arr) // 2))
```

# Q10: Implement Shell Sort to handle floating-point numbers.
```python
def shell_sort_floats(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

arr = [3.2, 1.5, 4.8, 2.1, 0.9]
print(shell_sort_floats(arr))
```