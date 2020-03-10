import numpy as np
from collections import defaultdict


class KNN:
    def __init__(self, k):
        self.k = k

    def create_data(self):
        features = np.array([[180, 76], [158, 43], [176, 78], [161, 49]])
        labels = ['男', '女', '男', '女']
        return features, labels

    def normalize(self, data):
        d_max = np.max(data, axis=0)
        d_min = np.min(data, axis=0)
        new_data = (data-d_min)/(d_max-d_min)
        return new_data, d_max, d_min

    def classify(self, one, data, labels):
        diff = data-one
        square = (diff**2).sum(axis=1)
        dist = square**0.5
        sort_idx = np.argsort(dist)

        # 统计k近邻labels
        d = defaultdict(int)
        for idx in sort_idx[:self.k]:
            d[labels[idx]] += 1
        sorted_d = sorted(d.items(), key=lambda k: k[1], reverse=True)
        # print(sorted_d)
        return sorted_d[0][0]


if __name__ == "__main__":
    knn = KNN(3)
    features, labels = knn.create_data()
    new_data, d_max, d_min = knn.normalize(features)
    one = np.array([[176, 76]])
    new_one = (one-d_min)/(d_max-d_min)
    result = knn.classify(new_one, new_data, labels)
    print('数据{}的预测性别为：{}'.format(one, result))
