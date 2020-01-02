import os
import random
import json
import math
from collections import defaultdict


class FirstRec:
    '''
    基于用户的协同过滤推荐
    '''

    def __init__(self, file_path, seed, k, n_items):
        self.file_path = file_path
        self.users_1000 = self._select_1000_users()
        self.seed = seed
        self.k = k
        self.n_items = n_items
        self.train, self.test = self._load_and_split_data()

    def _select_1000_users(self):
        print('随机选取1000个用户！')

        if os.path.exists('data/train.json') and os.path.exists('data/test.json'):
            return list()
        else:
            users = set()
            for file in os.listdir(self.file_path):
                if file.startswith('combined_data_1'):
                    one_path = '{}/{}'.format(self.file_path, file)
                    print('{}'.format(one_path))
                    with open(one_path, 'r') as fp:
                        for line in fp.readlines():
                            if line.strip().endswith(':'):
                                continue
                            userID, _, _ = line.split(',')
                            users.add(userID)
            users_1000 = random.sample(users, 1000)
            print(users_1000)
            return set(users_1000)

    def _load_and_split_data(self):
        train = defaultdict(dict)
        test = defaultdict(dict)
        if os.path.exists('data/train.json') and os.path.exists('data/test.json'):
            print('从文件中加载训练集和测试集')
            train = json.load(open('data/train.json'))
            test = json.load(open('data/test.json'))
            print('从文件中加载数据完成')
        else:
            random.seed(self.seed)
            for file in os.listdir(self.file_path):
                if file.startswith('combined_data_1'):
                    one_path = '{}/{}'.format(self.file_path, file)
                    print('{}'.format(one_path))
                    with open(one_path, 'r') as fp:
                        for line in fp.readlines():
                            if line.strip().endswith(':'):
                                movieID = line.split(':')[0]
                                continue
                            userID, rate, _ = line.split(',')
                            if userID in self.users_1000:
                                if random.randint(1, 50) == 1:
                                    test[userID][movieID] = int(rate)
                                else:
                                    train[userID][movieID] = int(rate)
            print('加载数据到 data/train.json 和 data/test.json')
            if not os.path.exists('data'):
                os.makedirs('data')
            json.dump(train, open('data/train.json', 'w'))
            json.dump(test, open('data/test.json', 'w'))
            print('加载数据完成')
        return train, test

    def pearson(self, rating1, rating2):
        sum_xy = 0
        sum_x = 0
        sum_y = 0
        sum_x2 = 0
        sum_y2 = 0
        num = 0

        for key in rating1.keys():
            if key in rating2.keys():
                num += 1
                x = rating1[key]
                y = rating2[key]
                sum_xy += x*y
                sum_x += x
                sum_y += y
                sum_x2 += math.pow(x, 2)
                sum_y2 += math.pow(y, 2)
        if num == 0:
            return 0

        denominator = math.sqrt(
            sum_x2 - math.pow(sum_x, 2)/num) * math.sqrt(sum_y2 - math.pow(sum_y, 2)/num)

        if denominator == 0:
            return 0
        return (sum_xy-sum_x*sum_y/num) / denominator

    def recommend(self, userID):
        neighborUsers = dict()
        for user in self.train.keys():
            if user != userID:
                distance = self.pearson(self.train[userID], self.train[user])
                neighborUsers[user] = distance
        # 字典排序
        newNU = sorted(neighborUsers.items(), key=lambda k: k[1], reverse=True)

        movies = dict()
        for (sim_user, sim) in newNU[:self.k]:
            for movieID in self.train[sim_user].keys():
                movies[movieID] = movies.get(
                    movieID, 0)+sim*self.train[sim_user][movieID]
        newMovies = sorted(movies.items(), key=lambda k: k[1], reverse=True)
        return newMovies

    def evaluate(self, num=30):
        '''
        随机抽取num个用户计算准确率
        '''
        print('开始计算准确率')
        precisions = list()
        random.seed(self.seed)
        for userID in random.sample(self.test.keys(), num):
            hit = 0
            result = self.recommend(userID)[:self.n_items]
            for (item, rate) in result:
                if item in self.test[userID]:
                    hit += 1
            precisions.append(hit/self.n_items)
        return sum(precisions)/len(precisions)


if __name__ == "__main__":
    file_path = 'netflix-prize-data'
    seed = 2020
    k = 15
    n_items = 20
    f_rec = FirstRec(file_path, seed, k, n_items)

    r = f_rec.pearson(f_rec.train['2385774'], f_rec.train['1327672'])
    print('2385774 和 1327672 的皮尔逊相关系数为：{}'.format(r))

    result = f_rec.recommend('1327672')
    print('为用户ID为：1327672的用户推荐的电影为：{}'.format(result))

    print('算法的推荐准确率为：{}'.format(f_rec.evaluate()))
