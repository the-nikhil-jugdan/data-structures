arr = [1, 2, 3, 4, 5, 5]

length = len(arr)


def is_sorted(arr, length):
    if length == 1:
        return True
    else:
        if (arr[length - 2] > arr[length - 1]):
            return False
        else:
            return is_sorted(arr, length - 1)


print(is_sorted(arr, length))
