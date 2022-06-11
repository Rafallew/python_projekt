# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.arange(-5, 6, 1)
# y = x**3 + 2*(x**2)
#
# plt.plot(x, y)
# plt.xlim((-5, 5))
# plt.xlabel('x')
# plt.ylabel('x^3+2x^2')
# plt.title('Wykres funkcji x^3+2x^2')
# plt.show()
# #
# zad2
#
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('flags.csv', header=0, sep=';')

df1 = df[(df['Zone'] == 'NE') | (df['Zone'] == 'NW')]

grouped = df1.groupby('Landmass').agg({'Area': ['sum']})

grouped.plot(kind='pie', subplots=True)#, autopct='%.2f %%', fontsize=14)
plt.title('Podział powierzchni kontynentów')
plt.legend()
plt.show()
#
# import matplotlib.pyplot as plt
# import pandas as pd
#
# df = pd.read_csv('flags.csv', header=0, sep=';')
#
# grouped = df.groupby('Zone').size()
# print(grouped)
#
# grouped.plot.bar()
# plt.title('Ilość krajów w poszczegółnych strefach')
# plt.xlabel('Strefa')
# plt.ylabel('Ilość')
# plt.subplots_adjust(bottom=0.18)
# plt.show()
