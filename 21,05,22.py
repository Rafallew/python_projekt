import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
from PIL import Image


def zadanie1():
    print('Zadanie 1')

    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro:")
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'bo')
    plt.ylabel('tutaj y')

    plt.axis([0, 6, 0, 20])

    plt.show()


def zadanie2():
    x = np.arange(0, 5.2, 0.2)
    plt.plot(x, x, 'r-', x, x ** 2, 'bs', x, x ** 3, 'g^')

    plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])

    plt.ylabel('y')
    plt.xlabel('x')

    plt.plot(x, x, 'r--', label='liniowa')
    plt.plot(x, x ** 2, 'bs', label='kwadratowa')
    plt.plot(x, x ** 3, 'g^', label='szescienna')

    plt.legend(loc='upper left')
    plt.title('Wykres 3 linii')
    plt.savefig('plot2.png')

    plt.show()

    im1 = Image.open('plot2.png')
    im1 = im1.convert('RGB')
    im1.save('plot2.jpg')


def zadanie3():
    x = np.arange(1, 20)
    y = 1/x
    plt.plot(x, y, 'r-')

    plt.legend(labels=['liniowa'])

    plt.ylabel('y')
    plt.xlabel('x')



    plt.legend(loc='upper left')

    plt.show()


    x = np.arange(1, 20)
    y = 1/x
    plt.plot(x, y, 'r-')

    plt.legend(labels=['liniowa'])

    plt.ylabel('y')
    plt.xlabel('x')



    plt.legend(loc='upper left')

    plt.show()

def zadanie4():
    x = np.arange(0, 10, 0.1)
    y = np.sin(x)
    plt.plot(x, y, color='green', label='linia 1')

    plt.legend(loc='upper left')


    plt.show()


def zadanie5():
    x1 = np.arange(0, 2.02, 0.02)
    x2 = np.arange(0, 2.02, 0.02)

    y1 = np.sin(2*np.pi *x1)
    y2 = np.cos(2 * np.pi * x1)

    plt.subplot(2, 1, 1)
    pl.plot(x1, y1)
    plt.xlabel('x')
    plt.title('Wykres sin(x)')

    plt.subplot(2, 1, 2)
    plt.plot(x2, y2, 'r-')
    plt.ylabel('cos(x)')
    plt.xlabel('x')
    plt.title('Wykres cos(x)')
    plt.subplots_adjust(hspace=0.5)

    plt.show()



def zadanie6():
    x1 = np.arange(0, 2.02, 0.02)
    x2 = np.arange(0, 2.02, 0.02)

    y1 = np.sin(2*np.pi *x1)
    y2 = np.cos(2 * np.pi * x1)



    fig, axs =plt.subplots(3, 2)
    print(type(fig))
    print(type(axs))
   # plt.show()

    axs[0, 0].plot(x1, y1)
    axs[0, 0].set_xlabel('x')
    axs[0, 0].set_ylabel('sin(x)')
    axs[0, 0].set_title('wykres sin(x)')

    axs[1, 1].plot(x2, y2)
    axs[1, 1].set_xlabel('x')
    axs[1, 1].set_ylabel('cos(x)')
    axs[1, 1].set_title('wykres cos(x)')

    axs[2, 0].plot(x2, y2)
    axs[2, 0].set_xlabel('x')
    axs[2, 0].set_ylabel('cos(x)')
    axs[2, 0].set_title('wykres cos(x)')

    fig.delaxes(axs[0, 1])
    fig.delaxes(axs[1, 0])
    fig.delaxes(axs[2, 1])



    plt.show()


def zadanie7():
    x1 = np.arange(0, 2.02, 0.02)
    x2 = np.arange(0, 2.02, 0.02)

    y1 = np.sin(2*np.pi *x1)
    y2 = np.cos(2 * np.pi * x1)

    dane = {'a': np.arange(50),
            'c':np.random.randint(0, 51, 50),
            'd': np.random.randn(50)}
    dane['b'] = dane['a'] + 10 * np.random.randn(50)
    dane['d'] = np.abs(dane['d']) * 100

    plt.scatter(data=dane, x='a', y='b', c='c', cmap='plasma', s='d')
    print(dane['c'])
    plt.show()


def zadanie8():
    x1 = np.arange(0, 2.02, 0.02)
    x2 = np.arange(0, 2.02, 0.02)

    y1 = np.sin(2*np.pi *x1)
    y2 = np.cos(2 * np.pi * x1)

    dane = {
        'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delphi', 'Brasilia', 'Warszawa'],
        'Populacja': [11190846, 1303171035, 207847528, 38645467],
        'Kontynent': ['Europa', 'Azja', 'Ameryka', 'Europa']
    }
    df = pd.DataFrame(dane)
    print(df)
    grupa =df.groupby('Kontynent')
    etykiety =list(grupa.groups.keys())
    wartosci = list(grupa.agg('Populacja').sum())

    plt.bar(x=etykiety, height=wartosci, color=['red', 'green', 'blue'])
    plt.xlabel('Kontynenty')
    plt.ylabel('Populacja na kontynecie')
    plt.show()



# def zadanie9():
#     x =





if __name__ == '__main__':
    # zadanie1()
     # zadanie2()
    # zadanie3()
    zadanie4()
    # zadanie5()
    # zadanie6()
    # zadanie7()
    # zadanie8()
    # zadanie9()