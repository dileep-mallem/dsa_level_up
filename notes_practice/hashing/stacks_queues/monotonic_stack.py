def next_greater(arr):
    n      = len(arr)
    result = [-1] * n     # default: no greater element
    stack  = []           # stores INDICES (monotonic decreasing by value)

    for i in range(n):
        # While stack has indices whose values are < current value
        # → current element is their "next greater"
        while stack and arr[stack[-1]] < arr[i]:
            idx          = stack.pop()
            result[idx]  = arr[i]

        stack.append(i)    # push current index

    return result

arr = [2, 1, 5, 3, 4]
print(next_greater(arr))    # [5, 5, -1, 4, -1]

arr2 = [4, 5, 2, 10, 8]
print(next_greater(arr2))   # [5, 10, 10, -1, -1]


 # For each element, find the previous smaller element to its LEFT
def prev_smaller(arr):
    result = [-1] * len(arr)
    stack  = []     # monotonic increasing stack (values)

    for i, num in enumerate(arr):
        while stack and stack[-1] >= num:
            stack.pop()
        if stack:
            result[i] = stack[-1]   # top is now the previous smaller
        stack.append(num)

    return result

arr = [4, 5, 2, 10, 8]
print(prev_smaller(arr))   # [-1, 4, -1, 2, 2]