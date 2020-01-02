import numpy as np
from sklearn import datasets


def pca(data, k):
    # 特征标准化（去中心化）
    print('origin data:', data)
    mean_vec = np.mean(data, axis=0)
    normalized_data = data-mean_vec
    print('after normalized:', normalized_data)

    # 协方差矩阵
    cov_matrix = np.cov(normalized_data.T)
    print('cov matrix:', cov_matrix)

    # 求特征值，特征向量
    f_value, f_vec = np.linalg.eig(cov_matrix)
    print('eig value:', f_value)
    print('eig vector:', f_vec)

    f_value_sort = np.argsort(f_value)
    f_value_top_k = f_value_sort[:-(k+1):-1]
    pca_basis = f_vec[:, f_value_top_k]
    print('pca basis:', pca_basis)
    # N*k*k*k'
    # 这里注意要使用normalized_data来乘
    result = np.matmul(normalized_data, pca_basis)
    return result, mean_vec, pca_basis


if __name__ == "__main__":
    import time
    data = np.array([[1, 2], [-2, -3.5], [3, 5], [-4, -7]])
    # data = datasets.load_iris()['data']
    t1 = time.time()
    print('origin data shape', data.shape)
    res, mean_vec, pca_basis = pca(data, k=1)
    print('after pca:', res)
    print('shape:', res.shape)

    reconstructed_data = np.matmul(res, pca_basis.T)+mean_vec
    print('重构数据：', reconstructed_data)

    t2 = time.time()
    from sklearn.decomposition import PCA
    pca = PCA(n_components=1)
    pca.fit(data)
    print('sklearn result:', pca.transform(data))
    t3 = time.time()

    print('time used: {} by our, {} by sklearn'.format(t2-t1, t3-t2))
