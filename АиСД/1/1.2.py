import numpy as np
import time
#импортируем тот файл функции которого вы хотите представить в виде графика
import matplotlib.pyplot as plt


class TestMain:

    n = 0

    def __time_it(self, type):

        sum = 0
        maximum = 0
        key = 51
        for i in range(50):
            test = np.random.randint(0, 100, self.n)
            start_time = time.time()
            self.__parser_dict(type)(test, key)
            runtime = time.time() - start_time
            if i == 0:
                minimum = runtime
            minimum = min(minimum, runtime)
            maximum = max(maximum, runtime)
            sum += runtime

        return minimum, sum/50, maximum

    def __parser_dict(self, type):
        dict = {
            1: linear_search,
            2: binary_search,
            3: interpolational_search
        }
        return dict[type]

    def __count_elements(self):
        if self.n < 1100000:
            while self.n < 100:
                self.n += 10
                return self.n
            while self.n < 1000:
                self.n += 100
                return self.n
            while self.n < 10000:
                self.n += 1000
                return self.n
            while self.n < 100000:
                self.n += 10000
                return self.n
            while self.n <= 1000000:
                self.n += 100000
                return self.n

    def plot(self, type, title):
        avg = []
        minimum = []
        maximum = []
        size = []
        for i in range(45):
            self.__count_elements()
            run = self.__time_it(type)
            minimum.append(run[0])
            avg.append(run[1])
            maximum.append(run[2])
            size.append(self.n)

        plt.plot(size, avg, 'g')
        plt.ylabel('Время')
        plt.xlabel('Длина массива')
        plt.title(title)
        plt.tight_layout()
        plt.plot(size, minimum, 'b')
        plt.plot(size, maximum, 'r')
        plt.grid()
        plt.show()
        plt.savefig(title)


a = TestMain()
a.plot(3, title='Интерполяционный поиск')