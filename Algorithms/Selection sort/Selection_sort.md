# Q1: Write a Python implementation of Selection Sort.


```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage:
print(selection_sort([64, 25, 12, 22, 11]))
```

# Q2: Write a Python implementation of Selection Sort that sorts in descending order.
```python
def selection_sort_desc(arr):
    n = len(arr)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

# Example usage:
print(selection_sort_desc([64, 25, 12, 22, 11]))
```

# Q3: Write a Python implementation of Selection Sort that counts the number of comparisons.
```python
def selection_sort_with_comparisons(arr):
    n = len(arr)
    comparisons = 0
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr, comparisons

# Example usage:
sorted_arr, comp = selection_sort_with_comparisons([64, 25, 12, 22, 11])
print(sorted_arr, comp)
```

# Q4: Implement a recursive version of Selection Sort.

```python
def recursive_selection_sort(arr, start=0):
    n = len(arr)
    if start >= n - 1:
        return arr
    min_index = start
    for j in range(start + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[start], arr[min_index] = arr[min_index], arr[start]
    return recursive_selection_sort(arr, start + 1)

# Example usage:
print(recursive_selection_sort([64, 25, 12, 22, 11]))
```

# Q5: Implement a stable version of Selection Sort using Python.
```python
def stable_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        key = arr[min_index]
        # Instead of swapping, shift elements to right
        while min_index > i:
            arr[min_index] = arr[min_index - 1]
            min_index -= 1
        arr[i] = key
    return arr

# Example usage:
print(stable_selection_sort([64, 25, 12, 22, 11]))
```

# Q6: Implement Selection Sort to sort a list of dictionaries by a given key.
```python
def selection_sort_dict(arr, key):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j][key] < arr[min_index][key]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage:
data = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 20}
]
print(selection_sort_dict(data, "age"))
```





