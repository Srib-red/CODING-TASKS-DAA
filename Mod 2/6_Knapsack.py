def knapsack(values, weigths, item_list, max_capacity):
    n = len(weigths)
    max_value = 0
    best_combination = []

    for combs in find_all_combinations(item_list, [], 0):
        temp_weight = 0
        temp_value = 0

        for item in combs:
            index = item_list.index(item)
            temp_value += values[index]
            temp_weight += weights[index]

        if max_value<temp_value and temp_weight <= max_capacity:
            max_value = temp_value
            best_combination = combs.copy()

    return best_combination, max_value

def find_all_combinations(arr,ans,i):
    
    if(i == len(arr)):
        return [ans.copy()] 
    
    result = []

    ans.append(arr[i])
    result += find_all_combinations(arr,ans,i+1)

    ans.pop()
    result += find_all_combinations(arr,ans,i+1)

    return result

if __name__ == "__main__":
    items_list = ['I1', 'I2', 'I3', 'I4', 'I5', 'I6']
    weights = [2, 3, 4, 5, 9, 7]
    values  = [3, 4, 8, 8, 10, 6]
    capacity = 15

    best_items, best_value = knapsack(values, weights, items_list, capacity)
    print("Best combination of items:", best_items)
    print("Maximum value:", best_value)