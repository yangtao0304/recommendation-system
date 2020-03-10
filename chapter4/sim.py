import numpy as np


def euclidean_dist(a, b):
    return np.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


print('a,b二维欧式距离：', euclidean_dist([1, 1], [2, 2]))


def manhattan_dist(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


print('a,b的二维曼哈顿距离：', manhattan_dist([1, 1], [2, 2]))


def chebyshev_dist(a, b):
    return max(abs(a[0]-b[0]), abs(a[1]-b[1]))


print('a,b的二维切比雪夫距离：', chebyshev_dist([1, 2], [3, 4]))


def cosine_dist(a, b):
    return (a[0]*b[0]+a[1]*b[1])/(np.sqrt(a[0]**2+a[1]**2)*np.sqrt(b[0]**2+b[1]**2))


print('a,b的二维余弦距离：', cosine_dist([1, 1], [2, 2]))


def jaccard_coef(a, b):
    set_a = set(a)
    set_b = set(b)
    return len(set_a & set_b)/len(set_a | set_b)


print('a,b的杰卡德相似系数：', jaccard_coef((1, 2, 3, 5, 8), (2, 3, 4)))


def jaccard_dist(a, b):
    set_a = set(a)
    set_b = set(b)
    return (len(set_a | set_b)-len(set_a & set_b))/len(set_a | set_b)


print('a,b的杰卡德距离：', jaccard_dist((1, 2, 3, 5, 8), (2, 3, 4)))
