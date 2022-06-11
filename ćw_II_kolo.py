import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#zadanie 1

# x = np.arange(-5, 5, 0.1) #wyświetla wykres od-5, do5, krok0,1
# plt.plot(x, x**3+2*x**2) #wykres funkcji
# plt.xlabel('x') #label-etykieta(opisanie osi)
# plt.ylabel('y')
#
# # plt.legend(loc='upper right')  # gorny rog(legenda)
# plt.axis([-5, 5, -5, 5]) # oś przedział
#
# plt.title('Wykres funkcji f(x) = x^3 + 2x^2') #tytuł wykresu
# plt.show() #wyświetl


# zadanie 2
#
df = pd.read_csv('flags.csv', header=0, sep=';', decimal='.')
print(df)

#a)

df.sort_values(by='Zone', inplace=True)
grupa = df.groupby('Zone')
print(grupa.get_group('N'))


#zadanie 3

# df = pd.read_csv('flags.csv', header=(0), sep=';', decimal='.')
# print(df)
#
#
#
# grupa =df.groupby('Zone').agg({'Zone':['sum']})
# print(grupa)


# grupa = df.plot.bar()
# grupa.set_xlabel('Zone')
# grupa.set_ylabel('Population')


plt.show()