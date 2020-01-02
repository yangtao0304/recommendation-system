import numpy as np
import math


class DataNorm:
    def __init__(self):
        self.arr = [1, 2, 3, 4, 5, 6, 7, 8, 99]
        self.x_max = max(self.arr)
        self.x_min = min(self.arr)
        self.x_mean = np.mean(self.arr)
        self.x_std = np.std(self.arr)

    def min_max(self):
        arr_ = list()
        for x in self.arr:
            # round(x,4) 保留4位小数
            arr_.append(round((x-self.x_min)/(self.x_max-self.x_min), 4))
        print('经过min_max标准化后的数据为：\n{}'.format(arr_))

    def z_score(self):
        arr_ = list()
        for x in self.arr:
            arr_.append(round((x-self.x_mean)/self.x_std, 4))
        print('经过z_score标准化后的数据为：\n{}'.format(arr_))

    def decimal_scaling(self):
        arr_ = []
        j = int(np.ceil(math.log(self.x_max, 10)))
        for x in self.arr:
            arr_.append(round(x/math.pow(10, j), 4))
        print('经过decimal scaling标准化后的数据为：\n{}'.format(arr_))

    def mean(self):
        arr_ = []
        for x in self.arr:
            arr_.append(round((x-self.x_mean)/(self.x_max-self.x_min), 4))
        print('经过mean标准化后的数据为：\n{}'.format(arr_))

    def vector(self):
        arr_ = []
        for x in self.arr:
            arr_.append(round(x/sum(self.arr), 4))
        print('经过vector标准化后的数据为：\n{}'.format(arr_))

    def exponential(self):
        arr_1 = []
        for x in self.arr:
            arr_1.append(round(math.log10(x)/math.log10(self.x_max), 4))
        print('经过log10标准化后的数据为：\n{}'.format(arr_1))

        arr_2 = []
        sum_e = sum([math.exp(one) for one in self.arr])
        for x in self.arr:
            arr_2.append(round(math.exp(x)/sum_e, 4))
        print('经过softmax标准化后的数据为：\n{}'.format(arr_2))

        arr_3 = []
        for x in self.arr:
            arr_3.append(round(1/(1+math.exp(-x)), 4))
        print('经过sigmoid标准化后的数据为：\n{}'.format(arr_3))


if __name__ == "__main__":
    dn = DataNorm()
    dn.min_max()
    dn.z_score()
    dn.decimal_scaling()
    dn.mean()
    dn.vector()
    dn.exponential()
