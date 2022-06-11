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
# df = pd.read_csv('flags.csv', header=0, sep=';', decimal='.')
# print(df)
# #wyświetla niepowtarzające sie wartości z kolumny Zone
# print(df['Zone'].unique())
# #a)
#
# #kraje znajdujace sie w polnocnej czesci ziemi.
# Polnocna_czesci=(df['Zone'].isin(["NE", "NW"]))
# print(Polnocna_czesci)
#
# #grupowanie w landmass  i ssumowanie w area   sum area (np. africa 27728
#
# sumaArea = (df.groupby("Landmass").agg({'Area':['sum']}))
# print(sumaArea)
# sumaArea.plot
# y = np.array(sumaArea)
# plt.pie(y)

# plt.pie(x=sumaArea, labels=)

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


# plt.show()



