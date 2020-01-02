import pandas as pd

file_path = 'BX-Users.csv'

users = pd.read_table(file_path, sep=';', header=0, encoding='ISO-8859-1')
print('前5条数据为：\n{}\n'.format(users.head()))
print('总的数据条数为：\n{}\n'.format(users.count()))
print('年龄区间：<{},{}>'.format(users['Age'].min(), users['Age'].max()))

'''
总的数据条数为：
User-ID     278858
Location    278858
Age         168096

年龄区间：<0.0,244.0>
'''

# Age列，对于NULL，pandas处理为NaN
# 最大、最小年龄有误

# 这里可以采用1.符合事实范围的随机数；2.平均数填充
