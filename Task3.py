import random
import timeit


# СОРТУВАННЯ ВСТАВКАМИ
def insertion_sort(arr):
    a = arr.copy()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a


# СОРТУВАННЯ ЗЛИТТЯМ
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# TIMSORT
def timsort(arr):
    return sorted(arr)


def main():

    sizes = [100, 1000, 5000]

    for size in sizes:

        data = [random.randint(0, 10000) for _ in range(size)]

        print(f"\nРозмір масиву: {size}")

        insertion_time = timeit.timeit(
            lambda: insertion_sort(data),
            number=3
        )

        merge_time = timeit.timeit(
            lambda: merge_sort(data),
            number=3
        )

        timsort_time = timeit.timeit(
            lambda: timsort(data),
            number=3
        )

        print(f"Insertion Sort: {insertion_time:.6f} сек")
        print(f"Merge Sort:     {merge_time:.6f} сек")
        print(f"Timsort:        {timsort_time:.6f} сек")


if __name__ == "__main__":
    main()