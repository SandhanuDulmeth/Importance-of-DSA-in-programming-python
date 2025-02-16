# Q1. (Beginner) Write a simple QuickSort implementation in Python using the Lomuto partition scheme.

```python
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage:
data = [10, 7, 8, 9, 1, 5]
quicksort(data, 0, len(data) - 1)
print(data)
```

# Q2. (Beginner) Write a non in‐place QuickSort in Python using list comprehensions that returns a new sorted list.
```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort(left) + equal + quicksort(right)

# Example usage:
print(quicksort([10, 7, 8, 9, 1, 5]))
```

# Q3. (Intermediate) Modify your QuickSort implementation to use a randomized pivot selection.
```python
import random

def quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage:
data = [10, 7, 8, 9, 1, 5]
quicksort(data, 0, len(data) - 1)
print(data)
```

# Q4. (Intermediate) Write a Python QuickSort that counts the number of comparisons made during sorting.
```python
def quicksort(arr, low, high, counter):
    if low < high:
        pi = partition(arr, low, high, counter)
        quicksort(arr, low, pi - 1, counter)
        quicksort(arr, pi + 1, high, counter)
    return counter

def partition(arr, low, high, counter):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        counter[0] += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage:
data = [10, 7, 8, 9, 1, 5]
comp_counter = [0]
quicksort(data, 0, len(data) - 1, comp_counter)
print(data)
print("Comparisons:", comp_counter[0])
```

# Q5. (Advanced) Implement 3-way QuickSort in Python to efficiently handle arrays with many duplicate elements.
```python
def quicksort3way(arr, low, high):
    if low >= high:
        return
    lt, i, gt = low, low, high
    pivot = arr[low]
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    quicksort3way(arr, low, lt - 1)
    quicksort3way(arr, gt + 1, high)

# Example usage:
data = [4, 5, 3, 4, 2, 4, 1, 4]
quicksort3way(data, 0, len(data) - 1)
print(data)
```

# Q6. (Advanced) Implement QuickSort with tail recursion elimination in Python to optimize recursion depth.
```python
def quicksort_tail(arr, low, high):
    while low < high:
        pi = partition(arr, low, high)
        if pi - low < high - pi:
            quicksort_tail(arr, low, pi - 1)
            low = pi + 1
        else:
            quicksort_tail(arr, pi + 1, high)
            high = pi - 1

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage:
data = [10, 7, 8, 9, 1, 5]
quicksort_tail(data, 0, len(data) - 1)
print(data)
```

# Q7. (Hard) Implement QuickSort in Python using the Hoare partition scheme.
```python
def quicksort_hoare(arr, low, high):
    if low < high:
        p = hoare_partition(arr, low, high)
        quicksort_hoare(arr, low, p)
        quicksort_hoare(arr, p + 1, high)

def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

# Example usage:
data = [10, 7, 8, 9, 1, 5]
quicksort_hoare(data, 0, len(data) - 1)
print(data)
```