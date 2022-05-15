from random import randint


def QuickSort(arr: list[int], left: int, right: int) -> list[int]:

    def partition(arr: list[int], left: int, right: int) -> int:
        # in-place
        pi = randint(left, right)
        i = left - 1
        arr[pi], arr[right] = arr[right], arr[pi]  # swap to the right
        pivot = arr[right]

        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return pi

    if left < right:
        pi = partition(arr, left, right)
        QuickSort(arr, left, pi - 1)
        QuickSort(arr, pi + 1, right)

    return arr


if __name__ == '__main__':
    lst = [randint(1, 100) for i in range(10)]
    print(QuickSort(lst, 0, len(lst) - 1))
