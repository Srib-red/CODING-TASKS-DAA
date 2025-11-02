def get_permutations(arr):
    n = len(arr)

    if n == 0:
        return [[]]
    
    perms = get_permutations(arr[1:])
    result = []

    for p in perms:
        for i in range(len(p) + 1):
            p_copy = p.copy()
            p_copy.insert(i, arr[0])
            result.append(p_copy)

    return result


if __name__ == '__main__':
    arr1 = []
    n = int(input("Enter the size of list: "))
    for i in range(n):
        arr1.append(int(input(f"Enter element at index [{i}]: ")))

    print("Original list:", arr1)
    perms = get_permutations(arr1)
    print(f"All permutations: {perms}")
    
