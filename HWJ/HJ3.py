def partition(arr, l, r):
    i, j = l, r

    while i < j:
        while i < j and arr[j] >= arr[l]:
            j -= 1
        while i < j and arr[i] <= arr[l]:
            i += 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[i] = arr[i], arr[l]

    return i


def quick_sort(arr, l, r):
    if l >= r:
        return
    i = partition(arr, l, r)
    quick_sort(arr, l, i - 1)
    quick_sort(arr, i + 1, r)


if __name__ == '__main__':
    num = int(input())
    res = []

    for _ in range(num):
        i = int(input())
        if i not in res:
            res.append(i)

    quick_sort(res, 0, len(res) - 1)

    for item in res:
        print(item)
