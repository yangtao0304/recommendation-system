# 基于信息熵的离散化 是 有监督学习的算法

import numpy as np
import math


class DiscreteByEntropy:
    def __init__(self, group, threshold):
        self.max_group = group
        self.min_threshold = threshold
        self.result = dict()

    def load_data(self):
        data = np.array([[56, 1], [87, 1], [129, 0], [23, 0], [342, 1],
                         [641, 1], [63, 0], [2746, 1], [2323, 0], [453, 1],
                         [10, 1], [9, 0], [88, 1], [222, 0], [97, 0],
                         [2398, 1], [592, 1], [561, 1], [764, 0], [121, 1]])
        return data

    def cal_entropy(self, data):
        num_data = len(data)
        label_counts = {}
        for feature in data:
            label = feature[-1]
            label_counts[label] = label_counts.get(label, 0)+1
        shannon_entropy = 0
        for key in label_counts:
            prob = label_counts[key]/num_data
            shannon_entropy -= prob*math.log2(prob)
        return shannon_entropy

    def split(self, data):
        min_entropy = float('inf')
        index = -1
        last_e1, last_e2 = -1, -1
        sorted_data = sorted(data, key=lambda x: x[0])

        s1 = dict()
        s2 = dict()

        for i in range(len(data)):
            split_data1, split_data2 = sorted_data[:i+1], sorted_data[i+1:]
            e1, e2 = (self.cal_entropy(split_data1),
                      self.cal_entropy(split_data2))
            # 计算信息熵
            entropy = e1*len(split_data1)/len(data) + \
                e2*len(split_data2)/len(data)
            if entropy < min_entropy:
                min_entropy = entropy
                index = i
                last_e1 = e1
                last_e2 = e2

        s1['entropy'] = last_e1
        s1['data'] = sorted_data[:index+1]
        s2['entropy'] = last_e2
        s2['data'] = sorted_data[index+1:]
        return s1, s2, entropy

    def train(self, data):
        need_split_key = [0]

        self.result[0] = {}
        self.result[0]['entropy'] = self.cal_entropy(data)
        self.result[0]['data'] = data
        group = 1

        for key in need_split_key:
            s1, s2, entropy = self.split(self.result[key]['data'])
            if group == self.max_group:
                break
            if entropy > self.min_threshold:
                self.result[key] = s1
                new_key = max(self.result.keys())+1
                self.result[new_key] = s2
                need_split_key.extend([key])
                need_split_key.extend([new_key])
                group += 1

            else:
                continue


if __name__ == "__main__":
    dbe = DiscreteByEntropy(group=6, threshold=0.5)
    data = dbe.load_data()
    print('整个数据集的香农熵为：', dbe.cal_entropy(data))
    s1, s2, min_entropy = dbe.split(data)
    dbe.train(data)

    print('result is ')
    import pprint
    pprint.pprint(dbe.result)
