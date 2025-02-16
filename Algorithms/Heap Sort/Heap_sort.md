# Q1: Basic Heap Sort Implementation in Python
```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Example usage:
if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]
    heap_sort(arr)
    print("Q1 Output:", arr)
```

# Q2: Heap Sort Implementation with Ascending and Descending Order
```python
def heapify(arr, n, i, compare):
    extreme = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and compare(arr[left], arr[extreme]):
        extreme = left
    if right < n and compare(arr[right], arr[extreme]):
        extreme = right
    if extreme != i:
        arr[i], arr[extreme] = arr[extreme], arr[i]
        heapify(arr, n, extreme, compare)

def heap_sort(arr, order='asc'):
    n = len(arr)
    if order == 'asc':
        compare = lambda a, b: a > b  # Build max heap for ascending sort
    elif order == 'desc':
        compare = lambda a, b: a < b  # Build min heap for descending sort
    else:
        raise ValueError("order must be 'asc' or 'desc'")
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, compare)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, compare)

# Example usage:
if __name__ == "__main__":
    arr1 = [4, 10, 3, 5, 1]
    heap_sort(arr1, order='asc')
    print("Q2 Ascending:", arr1)
    arr2 = [4, 10, 3, 5, 1]
    heap_sort(arr2, order='desc')
    print("Q2 Descending:", arr2)
```

# Q3: Heap Sort for a List of Dictionaries by a Custom Key
```python
def heapify_dict(arr, n, i, key):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left][key] > arr[largest][key]:
        largest = left
    if right < n and arr[right][key] > arr[largest][key]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_dict(arr, n, largest, key)

def heap_sort_dict(arr, key):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify_dict(arr, n, i, key)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_dict(arr, i, 0, key)

# Example usage:
if __name__ == "__main__":
    arr = [
        {'name': 'Alice', 'score': 85},
        {'name': 'Bob', 'score': 95},
        {'name': 'Charlie', 'score': 75}
    ]
    heap_sort_dict(arr, key='score')
    print("Q3 Output:", arr)
```

# Q4: Heap Sort Implementation that Counts Comparisons
```python
comparison_count = 0

def heapify_count(arr, n, i):
    global comparison_count
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n:
        comparison_count += 1
        if arr[left] > arr[largest]:
            largest = left
    if right < n:
        comparison_count += 1
        if arr[right] > arr[largest]:
            largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_count(arr, n, largest)

def heap_sort_count(arr):
    global comparison_count
    comparison_count = 0
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify_count(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_count(arr, i, 0)
    return comparison_count

# Example usage:
if __name__ == "__main__":
    arr = [4, 10, 3, 5, 1]
    comps = heap_sort_count(arr)
    print("Q4 Sorted array:", arr)
    print("Q4 Total comparisons:", comps)
```