import numpy as np
import pandas as nd

# a = np.array([20, 30, 40, 50])
# b = np.arange(4)
#
# c = a + b
# print(c)
# d = np.sqrt(b)
# print(d)
# e = d + c
# print(e)


# a = np.arange(12).reshape((3, 4))
# print(a)
# print(a.sum())
# print(a.sum(axis=0))
# print(a.sum(axis=1))
# print(a.cumsum(axis=1))


# # mnożenie macierzy
# a = np.arange(3)
# b = np.arange(3)
# print(np.dot(a, b))
# print(a.dot(b))
# c = np.arange(3)
# d = np.array([[0],[1],[2]])
# print(c.dot(d))
# e = np.array([[2, 5, 1],[3, 4, 5]])
# f = np.array([[3, 4],[1,6],[3, 3]])
# print(e.dot(f))



# a = np.arange(6).reshape((3, 2))
# print(a)
# for b in a:
#     for c in b:
#         print(c)
# for d in a.flat:
#     print(d)



# a = np.arange(12).reshape((3, 4))
# print(a)
# b = a.reshape((4, 3))
# print(b)
# c = b.ravel()
# print(c)
# d = b.T     #transpozycja
# print(d)

#       KONIEC BIBLIOTEKI NUMPY !!!



#       PANDAS

import pandas as pd

# s = pd.Series([1, 3, 5 ,5.5, 'a'])
# print(s)
# s = pd.Series([10, 12, 14, 8], index=['a', 'b', 'c','d'])
# print(s)
#
#
#
#
#
# data = {'Kraj': ['Belgia','Indie', 'Brazylia'],
#         'Stolica':['Bruksela', 'New Delhi', 'Brasilia'],
#         'Populacja':[111554, 55151, 55515881]}
# df =pd.DataFrame(data)
# print(df)
#
# daty = pd.date_range('20220507', periods=5)
# df2 = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD'))
# print(df2)
#
df3 = pd.read_csv('dane.csv', header=(0), sep=';', decimal='.')
print(df3)
#
# xlsx = pd.ExcelFile('imiona.xlsx')
# df4 = pd.read_excel(xlsx, header=0)
# print(df4)
#
# df3.to_csv('dane2.csv', index=False)
# df4.to_excel('imiona2.xlsx', sheet_name='dane')
# print(df4.head(10))
# print(df4.tail(10))
#
# print(df4.sample(5))
# print(df.sample(4, replace=True))


##                      BŁEDY !!!
                        # |
                        # V


s = pd.Series([1, 3, 5 ,5.5, 'a'])
print(s)
s = pd.Series([10, 12, 14, 8], index=['a', 'b', 'c','d'])
data = {'Kraj': ['Belgia','Indie', 'Brazylia'],
        'Stolica':['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja':[111554, 55151, 55515881]}
df =pd.DataFrame(data)
print(df)

daty = pd.date_range('20220507', periods=5)
df2 = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD'))

print(df[0:1])
print(df['Kraj'])
print(df.Kraj)

print(df.iloc[[0],[0]])
print(df.loc[[0],'Kraj'])
print(df.at[0, 'Kraj'])


