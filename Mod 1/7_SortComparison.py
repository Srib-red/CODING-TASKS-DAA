import time
import tracemalloc
import random

def bubble_sort(arr):
    n = len(arr)
    ops = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            ops += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                ops += 1
    return ops


def insertion_sort(arr):
    n = len(arr)
    ops = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        ops += 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            ops += 1
        arr[j + 1] = key
    return ops


def selection_sort(arr):
    n = len(arr)
    ops = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            ops += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            ops += 1
    return ops


def quick_sort(arr):
    ops = [0]

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            ops[0] += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                ops[0] += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        ops[0] += 1
        return i + 1

    def quicksort(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort(low, pi - 1)
            quicksort(pi + 1, high)

    quicksort(0, len(arr) - 1)
    return ops[0]


def heap_sort(arr):
    ops = 0
    n = len(arr)

    def heapify(limit, i):
        nonlocal ops
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < limit:
            ops += 1
            if arr[left] > arr[largest]:
                largest = left
        if right < limit:
            ops += 1
            if arr[right] > arr[largest]:
                largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            ops += 1
            heapify(limit, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        ops += 1
        heapify(end, 0)

    return ops


def analyze_sorting_algorithms(n=1000):
    data = [random.randint(0, 10000) for _ in range(n)]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort,
        "Quick Sort": quick_sort,
        "Heap Sort": heap_sort
    }

    results = []

    for name, func in algorithms.items():
        test_data = data.copy()

        tracemalloc.start()
        start_time = time.time()

        ops = func(test_data)

        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        results.append({
            "Algorithm": name,
            "Time (s)": round(end_time - start_time, 6),
            "Operations": ops,
            "Memory (bytes)": peak
        })

    print("\nEmpirical Analysis Results:")
    print("{:<15} {:<12} {:<15} {:<15}".format("Algorithm", "Time (s)", "Operations", "Memory (bytes)"))
    print("-" * 60)

    for r in results:
        print("{:<15} {:<12} {:<15} {:<15}".format(
            r["Algorithm"], r["Time (s)"], r["Operations"], r["Memory (bytes)"]
        ))


if __name__ == "__main__":

    analyze_sorting_algorithms(n=500)
