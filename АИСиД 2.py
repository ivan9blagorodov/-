import time
import numpy as np
import matplotlib.pyplot as plt


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
    if array[search] == key:
        search = array[search]
        return search
    else:
        return -1


n = 1000
dx = 100000
key = 435
result = []
search_time = []
while n <= 1.0e+6 + 1000:
    array = np.arange(n, dtype=int)
    a = binary_search(array, key)
    b = time.process_time()
    n += dx
    result.append(len(array))
    search_time.append(b)

plt.plot(result, search_time, 'g')
plt.ylabel('Time')
plt.xlabel('Array length')
plt.title('Binary search')
plt.tight_layout()
plt.grid()
print(result)
print(search_time)