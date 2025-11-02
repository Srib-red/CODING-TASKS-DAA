def find_all_combinations(arr,ans,i):
    
    if(i == len(arr)):
        return [ans.copy()] 
    
    result = []

    ans.append(arr[i])
    result += find_all_combinations(arr,ans,i+1)

    ans.pop()
    result += find_all_combinations(arr,ans,i+1)

    return result

if __name__ == '__main__':
    arr1 = []
    n = int(input("Enter the size of list: "))
    for i in range(n):
        arr1.append(int(input(f"Enter element at index [{i}]: ")))

    combs = find_all_combinations(arr1,[],0)
    print(f"All combinations: {combs}")


