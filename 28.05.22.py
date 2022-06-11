#
#2 dane z pliku ramka pandas
#3 ramka na podstawie zad2
#4 pogrupowanie kołowo lub kolumnowo
#co oddziela wartości w wierszach

# liniowy kolumnowy kołowy

# interpreter 3.8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Na wykresie wyswietl wykres liniowy funkcji f(x)=1/x dla xE[1,20].
# Dodaj etykietę do linii wykresu i wyświetl legędę. Dodaj odpowiednie
# etykiety do osi wykresu('x','f(x)')oraz ustaw
# zakres osi na (0,1)oraz (1, ,długość wektora x)
def zadanie1 ():
    x = np.arange(1, 21, 1)
    plt.plot(x, 1/x, label='f(x) = 1/x')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axis([0, 20, 0, 1])
    plt.legend()
    plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')
    plt.show()

#Zmodyfikuj wykres z zadania 1 tak, żeby styl wykresu
# wyglądał tak jak na poniższym zrzucie ekranu.
def zadanie2():
    x = np.arange(1, 21, 1)
    plt.plot(x, 1/x, 'g>:', label='f(x) = 1/x' )
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axis([0, 20, 0, 1])
    plt.legend()
    plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')
    plt.show()

#Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x)
#dla xE[0,30] z krokiem 0,1. Dodaj etykiety i legende do wykresu.
def zadanie3():
    x = np.arange(0, 30, 0.1)
    plt.plot(x, np.sin(x), 'b', label='sin(x)')
    plt.plot(x, np.cos(x), 'r', label='cos(x)')
    plt.xlabel('x')
    plt.ylabel('sin(x) cos(x)')
    plt.legend(loc='upper right')#gorny rog(legenda)
    plt.title('Wykres sin(x), cos(x)')
    plt.show()

def zadanie4():
    df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
    print(df)
    # przygotowanie wektora kolorów
    colors = np.random.randint(0, 50, len(df.index))
    # przygotowanie wektora z rozmiarami 'kropek'
    scale = np.abs(df['sepal length'] - df['sepal width'])

    plt.scatter(df['sepal length'], df['sepal width'], c=colors, s=scale)
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')
    plt.show()


def zadanie5():
    xlsx = pd.ExcelFile('imiona.xlsx') #..(cofam sie)\\lab 5 i 6\\(otwieram folter o nazwie lab 5 i 6
    df = pd.read_excel(xlsx, header=0)
    print(df)
    plt.subplot(1, 3, 1)
    grouped = df.groupby('Plec')
    etykiety = list(grouped.groups.keys())
    wartosci = list(grouped.agg('Liczba').sum())
    plt.bar(x=etykiety, height=wartosci, color=['green', 'red'])
    plt.xlabel('Płeć')
    plt.ylabel('Liczba narodzonych dzieci')
    # wykres 2
    plt.subplot(1, 3, 2)
    x = df['Rok'].unique()
    kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba':['sum']}).values
    mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba':['sum']}).values
    plt.plot(x, kobiety, label="Kobiety")
    plt.plot(x, mezczyzni, label="Mężczyźni")
    plt.xlabel('Rok')
    #
    # # wykres 3
    plt.subplot(1, 3, 3)
    x = df['Rok'].unique()
    y = df.groupby('Rok').agg('Liczba').sum()
    plt.bar(x, y)
    plt.xlabel('Rok')
    # wyświetlamy cały wykres
    plt.subplots_adjust(wspace=0.85)
    plt.show()


#korzystając z pliku zamówienia.csv (pandans) policz sumy zamówień dla każdego sprzedawcy
# i wyświetl wykres kolowy z procentowym udziałem każdego sprzedawcy w ogólnej sumie zamówień .
#Poszukaj w Internecie jak dodać cień do takiego wykresu i jak działa atrybut 'explode'
#tego wykresu. Przetestuj ten atrybut na wykresie.
def zadanie6():
    df = pd.read_csv('zamowienia.csv', sep=';')
    policzone = df.groupby('Sprzedawca')['Utarg'].sum()
    print(policzone)
    # explode
    explode = [0.0 for n in range(len(policzone.index))]
    # określamy które kawałki i o ile wysunąć, tu losujemy jeden
    explode[np.random.randint(0, len(policzone.index))] = 0.2
    wedges, texts, autotext = plt.pie(x=policzone, labels=policzone.index,
                                      autopct=lambda pct: "{:.2f}%".format(pct), textprops=dict(color='black'), explode=explode, shadow=True)
    plt.title("Procentowy udział kwot zamówień sprzedawców")
    plt.show()
if __name__ == '__main__':
    # zadanie1()
    # zadanie2()
    zadanie3()
    ## zadanie4()
    # zadanie5()
    # zadanie6()