import pandas as pd
import matplotlib.pyplot as plt

# 用来在matplotlib显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']


def get_ratings(file_path):
    rates = pd.read_csv(file_path)
    print('userId的范围：<{},{}>\n'.format(
        min(rates['userId']), max(rates['userId'])))
    print('movieId的范围：<{},{}>\n'.format(
        min(rates['movieId']), max(rates['movieId'])))
    print('rating的范围：<{},{}>\n'.format(
        min(rates['rating']), max(rates['rating'])))
    print('数据总条数为：\n{}\n'.format(rates.count()))
    print('数据的前5条记录为：\n{}\n'.format(rates.head(5)))

    df = rates['userId'].groupby(rates['userId'])
    print('用户评分记录最少条数为：{}'.format(df.count().min()))

    scores = rates['rating'].groupby(rates['rating']).count()
    for x, y in zip(scores.keys(), scores.values):
        plt.text(x, y+2, '%.0f' % y, ha='center', va='bottom', fontsize=12)
    plt.bar(scores.keys(), scores.values, width=0.3, tick_label=scores.keys())
    plt.xlabel('评分分数')
    plt.ylabel('对应人数')
    plt.title('评分分数对应人数统计')
    plt.show()


if __name__ == "__main__":
    get_ratings(file_path='ratings.csv')
