import time
import numpy as np
import matplotlib.pyplot as plt


def fibonaccian_search(array, key):
    fib_nm2 = 0
    fib_nm1 = 1
    fib_n = fib_nm2 + fib_nm1
    while fib_n < len(array):
        fib_nm2 = fib_nm1
        fib_nm1 = fib_n
        fib_n = fib_nm2 + fib_nm1
    offset = -1
    while fib_n > 1:
        i = min(offset + fib_nm2, len(array) - 1)
        if array[i] < key:
            fib_n = fib_nm1
            fib_nm1 = fib_nm2
            fib_nm2 = fib_n - fib_nm1
            offset = i
        elif array[i] > key:
            fib_n = fib_nm2
            fib_nm1 = fib_nm1 - fib_nm2
            fib_nm2 = fib_n - fib_nm1
        else:
            return i
    if fib_nm1 and array[offset] == key:
        return offset
    return -1


n = 1000
dx = 100000
key = 435
result = []
search_time = []
while n < 1.0e+6 + 1000:
    array = np.arange(n, dtype=int)
    a = fibonaccian_search(array, key)
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