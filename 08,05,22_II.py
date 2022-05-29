import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def zadanie1():

    df3 = pd.read_csv('dane.csv', header=(0), sep=';', decimal='.')
    print(df3)

    grupa =df3.groupby('Imię i nazwisko').agg({'Wartość zamówienia': ['sum']})
    print(grupa)
    grupa.plot(kind='pie', subplots=True,
               autopct='%.2f %%',
               fontsize=20,
               colors=['red','green'])

    plt.legend(loc='upper left')
    plt.show()
if __name__ == '__main__':
         zadanie1()
        #zadanie2()