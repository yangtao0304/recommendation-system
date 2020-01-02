import pandas as pd
import matplotlib.pyplot as plt

def get_movies(file_path):
    movies = pd.read_csv(file_path)
    print('movieId的范围是：<{},{}>\n'.format(
        min(movies['movieId']), max(movies['movieId'])))
    print('数据总条数：\n{}\n'.format(movies.count()))

    moviesDict = dict()
    for line in movies['genres'].values:
        for one in line.split('|'):
            moviesDict[one] = moviesDict.get(one, 0)+1

    print('电影类型总数为：{}'.format(len(moviesDict)))
    print('电影类型分别是：{}'.format(moviesDict.keys()))
    print(moviesDict)

    newMD = sorted(moviesDict.items(), key=lambda k: k[1], reverse=True)

    labels = [newMD[i][0] for i in range(len(newMD))]
    values = [newMD[i][1] for i in range(len(newMD))]
    print(labels)
    # 与labels对应，数值越大，离中心区越远
    explode = [x*0.01 for x in range(len(newMD))]

    # 设置x，y轴比例
    plt.axes(aspect=1)
    # autopct表示百分比的格式，shadow表示阴影
    # labeldistance表示标签距离中心距离，pctdistance表示百分比数据距离中心距离
    plt.pie(x=values, labels=labels, explode=explode, autopct='%3.1f %%',
            shadow=False, startangle=0, labeldistance=1.1, pctdistance=0.8, center=(-1, 0))
    # bbox_to_anchor控制位置
    # ncol控制列数，默认为1
    plt.legend(loc=7, bbox_to_anchor=(1.3, 1.0), ncol=3,
            fancybox=True, shadow=True, fontsize=6)
    plt.show()

if __name__ == "__main__":
    get_movies('movies.csv')
