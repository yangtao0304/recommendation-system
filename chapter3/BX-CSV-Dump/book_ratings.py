import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']


def get_ratings(file_path):
    # 图书的ISBN中可能包含字符，所以在使用pandas读取文件时，需要指定编码
    ratings = pd.read_table(file_path, header=0,
                            sep=';', encoding='ISO-8859-1')
    print('前5条数据：\n{}\n'.format(ratings.head(5)))
    print('总的数据条数：\n{}\n'.format(ratings.count()))
    print('用户对图书的评分范围：<{},{}>\n'.format(
        min(ratings['Book-Rating']), ratings['Book-Rating'].max()))
    rateSer = ratings['Book-Rating'].groupby(ratings['Book-Rating']).count()
    plt.bar(rateSer.keys(), rateSer.values, tick_label=rateSer.keys())
    for x, y in zip(rateSer.keys(), rateSer.values):
        plt.text(x, y+1, '%.0f' % y, ha='center', va='bottom', fontsize=9)
    plt.xlabel('用户评分')
    plt.ylabel('评分对应的人数')
    plt.title('每种评分下对应的人数统计图')
    plt.show()


if __name__ == "__main__":
    get_ratings(file_path='BX-Book-Ratings.csv')
