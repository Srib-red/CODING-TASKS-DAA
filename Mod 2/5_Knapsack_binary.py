def knapsack(values, weigths, item_list, max_capacity):
    n = len(weigths)
    max_value = 0
    best_combination = []

    for i in range(2**n):
         binary_string = bin(i)[2:].zfill(n)

         temp_value = 0
         temp_weight = 0
         selected_items = []

         for j in range(n):
           if binary_string[j] == '1':
               temp_value += values[j]
               temp_weight += weigths[j]
               selected_items.append(item_list[j])
           if max_value < temp_value and temp_weight <= max_capacity:
               max_value = temp_value
               best_combination = selected_items.copy()

    return best_combination, max_value

if __name__ == "__main__":
    items = ['I1', 'I2', 'I3', 'I4', 'I5', 'I6']
    weights = [2, 3, 4, 5, 9, 7]
    values  = [3, 4, 8, 8, 10, 6]
    capacity = 15

    best_items, best_value = knapsack(values, weights, items, capacity)
    print("Best combination of items:", best_items)
    print("Maximum value:", best_value)
    
    


          