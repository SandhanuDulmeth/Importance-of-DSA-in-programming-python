# Q1: Write a basic bubble sort implementation in Python.
```python
def bubble_sort_basic(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Example test for Q1:
print("Q1 Answer:", bubble_sort_basic([64, 34, 25, 12, 22, 11, 90]))
```

# Q2: Write an optimized bubble sort that stops early if no swaps occur.
```python
def bubble_sort_optimized(arr):
    n = len(arr)
    while True:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        n -= 1  # Last element is now in correct position.
        if not swapped:
            break
    return arr

# Example test for Q2:
print("Q2 Answer:", bubble_sort_optimized([64, 34, 25, 12, 22, 11, 90]))
```
# Q3: Write a recursive bubble sort implementation in Python.
```python
def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 1:
        return arr
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return bubble_sort_recursive(arr, n - 1)

# Example test for Q3:
print("Q3 Answer:", bubble_sort_recursive([64, 34, 25, 12, 22, 11, 90]))
```


# Q4: Write a bubble sort that outputs the list after each swap (step-by-step output).
```python
def bubble_sort_steps(arr):
    n = len(arr)
    steps = []
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append(arr.copy())
    return steps

# Example test for Q4:
print("Q4 Answer (step-by-step):")
for step in bubble_sort_steps([64, 34, 25, 12, 22, 11, 90]):
    print(step)
```

# Q5: Write a bubble sort that counts the number of swaps.
```python
def bubble_sort_count_swaps(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
    return arr, swap_count

# Example test for Q5:
sorted_arr, swaps = bubble_sort_count_swaps([64, 34, 25, 12, 22, 11, 90])
print("Q5 Answer:", sorted_arr)
print("Total swaps:", swaps)
```







