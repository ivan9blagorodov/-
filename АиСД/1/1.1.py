def linear_search(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i
        else:
            return -1


def binary_search(array, key):
    minimum = 0
    maximum = len(array) - 1
    search = 0
    while minimum <= maximum:
        avg = (maximum + minimum) // 2
        if key < array[avg]:
            maximum = avg - 1
        elif key > array[avg]:
            minimum = avg + 1
        else:
            search = avg
            break
    while search > 0 and array[search - 1] == key:
        search -= 1
    if array[search] == key:
        return search
    else:
        return -1


def interpolational_search(array, key):
    minimum = 0
    maximum = len(array) - 1
    search = 0
    while array[minimum] < key < array[maximum]:
        dist = int(minimum + (maximum - minimum) * (key - array[minimum]) / (array[maximum] - array[minimum]))
        if array[dist] == key:
            search = dist
            break
        elif array[dist] > key:
            maximum = dist - 1
        else:
            minimum = dist + 1
    if array[minimum] == key:
        search = minimum
    elif array[maximum] == key:
        search = maximum
    while search > 0 and array[search - 1] == key:
        search -= 1
    if array[search] == key:
        return search
    else:
        return -1