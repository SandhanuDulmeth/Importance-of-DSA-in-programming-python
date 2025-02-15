# Q1: Write a basic merge sort in Python.
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test Q1:
arr1 = [38, 27, 43, 3, 9, 82, 10]
print("Q1 Sorted:", merge_sort(arr1))
```

# Q2: Write a merge sort in Python that sorts a list in descending order.
```python
def merge_sort_desc(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_desc(arr[:mid])
    right = merge_sort_desc(arr[mid:])
    return merge_desc(left, right)

def merge_desc(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test Q2:
arr2 = [38, 27, 43, 3, 9, 82, 10]
print("Q2 Sorted Descending:", merge_sort_desc(arr2))
```

# Q3: Write an iterative (bottom-up) merge sort in Python.
```python
def merge_sort_iterative(arr):
    width = 1
    n = len(arr)
    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i:i+width]
            right = arr[i+width:i+2*width]
            arr[i:i+2*width] = merge(left, right)
        width *= 2
    return arr

# Reusing merge() from Q1.
# Test Q3:
arr3 = [38, 27, 43, 3, 9, 82, 10]
print("Q3 Iterative Sorted:", merge_sort_iterative(arr3.copy()))
```

# Q4: Write an in-place merge sort in Python.
```python
def merge_in_place(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]
    i = j = 0
    k = start
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def merge_sort_in_place(arr, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort_in_place(arr, start, mid)
        merge_sort_in_place(arr, mid, end)
        merge_in_place(arr, start, mid, end)

# Test Q4:
arr4 = [38, 27, 43, 3, 9, 82, 10]
merge_sort_in_place(arr4, 0, len(arr4))
print("Q4 In-Place Sorted:", arr4)
```

# Q5: Write a parallel merge sort in Python using multiprocessing.
```python
import multiprocessing as mp

def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # Use serial merge sort for small arrays to reduce overhead.
    if len(arr) < 5000:
        return merge_sort(arr)
    mid = len(arr) // 2
    with mp.Pool(2) as pool:
        left, right = pool.map(parallel_merge_sort, [arr[:mid], arr[mid:]])
    return merge(left, right)

# Reusing merge() and merge_sort() from Q1.
# Test Q5:
if __name__ == '__main__':
    arr5 = [38, 27, 43, 3, 9, 82, 10] * 1000  # enlarge for parallel benefit
    sorted_arr5 = parallel_merge_sort(arr5)
    print("Q5 Parallel Sorted (first 10 elements):", sorted_arr5[:10])
```