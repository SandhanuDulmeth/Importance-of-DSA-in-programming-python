# Q1: Write a basic insertion sort algorithm in Python.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]
    insertion_sort(data)
    print("Sorted array:", data)
```

# Q2: Modify insertion sort to sort a list of strings in alphabetical order.
```python
def insertion_sort_strings(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j].lower() > key.lower():
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
if __name__ == "__main__":
    words = ["banana", "Apple", "cherry", "date"]
    insertion_sort_strings(words)
    print("Sorted strings:", words)
```
# Q3: Modify insertion sort to sort the list in descending order.
```python
def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]
    insertion_sort_descending(data)
    print("Sorted in descending order:", data)
```

# Q4: Implement insertion sort using binary search to find the correct insertion index.

```python
def binary_search(arr, key, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= key:
            start = mid + 1
        else:
            end = mid
    return start

def insertion_sort_binary(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        insertion_index = binary_search(arr, key, 0, i)
        j = i
        while j > insertion_index:
            arr[j] = arr[j - 1]
            j -= 1
        arr[insertion_index] = key

# Example usage:
if __name__ == "__main__":
    data = [37, 23, 0, 17, 12, 72, 31]
    insertion_sort_binary(data)
    print("Sorted array using binary search:", data)
```

# Q5: Implement insertion sort to sort a list of dictionaries based on a specified key.
```python
def insertion_sort_dict(arr, sort_key):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j][sort_key] > current[sort_key]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

# Example usage:
if __name__ == "__main__":
    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 20},
        {"name": "Charlie", "age": 30}
    ]
    insertion_sort_dict(people, "age")
    print("People sorted by age:", people)
```