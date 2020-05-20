import time
import numpy as np
import matplotlib.pyplot as plt


def linear_search(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i


n = 1000
dx = 100000
key = 435
result = []
search_time = []
while n <= 1.0e+6 + 1000:
    array = np.arange(n, dtype=int)
    a = linear_search(array, key)
    b = time.process_time()
    n += dx
    result.append(len(array))
    search_time.append(b)

plt.plot(result, search_time, 'g')
plt.ylabel('Time')
plt.xlabel('Array length')
plt.title('Linear search')
plt.tight_layout()
plt.grid()
print(result)
print(search_time)