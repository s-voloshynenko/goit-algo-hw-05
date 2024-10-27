def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    iterations = 0
    mid = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        if arr[mid] == x:
            upper_bound = arr[mid]
            return (iterations, upper_bound)

        elif arr[mid] < x:
            low = mid + 1

        else:
            upper_bound = arr[mid]
            high = mid - 1

    if upper_bound is None and low < len(arr):
        upper_bound = arr[low]

    return (iterations, upper_bound)

arr = [0.5, 1.1, 2.5, 3.3, 4.5, 5.5, 10.5]
x = 4.3

print(binary_search(arr, x))
