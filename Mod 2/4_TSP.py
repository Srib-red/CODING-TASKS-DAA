def TSP(dist_matrix, cities_list, src_city):
    min_dist = float('inf')
    best_path = []
    
    # Step 1
    cities = cities_list.copy()
    cities.remove(src_city)

    # Step 2
    for perms in get_permutations(cities):
        path = [src_city] + perms + [src_city]
        total_dist = 0

        for i in range(len(path) - 1):  # fixed range
            total_dist += dist_matrix[path[i]][path[i + 1]]  # fixed indexing

        if total_dist < min_dist:
            min_dist = total_dist
            best_path = path
    
    return best_path, min_dist


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
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    cities = [0, 1, 2, 3]
    src = 0
    
    best_path, min_dist = TSP(dist, cities, src)
    print("Best path:", best_path)
    print("Minimum distance:", min_dist)
