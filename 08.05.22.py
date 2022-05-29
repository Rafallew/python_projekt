#4 wykresy
#2 wektory
#na danych
# 5 zad na wyświetlenie dodatkowe
# z jakiej bibioteki bedzie podane
#ustawienia do wykres etykiety 1,5h github +dokumentacja
# cały projekt
# biblioteki instal;beda podane jakie









import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def zadanie1():

        s = pd.Series([1, 3, 5 ,5.5, 'a'])
        #print(s)
        s = pd.Series([10, 12, 14, 8], index=['a', 'b', 'c','d'])
        print(s)

                #pierwsza tabela
        data = {'Kraj': ['Belgia','Indie', 'Brazylia'],
                'Stolica':['Bruksela', 'New Delhi', 'Brasilia'],
                'Populacja':[111542525, 52250000, 35055881]}
        df =pd.DataFrame(data)
        #print(df)

        print(s['a'])
        print(s[s > 10])
        print(s[(s < 13) & (s > 8)])

        # na dwa sposoby można na podstawie warunku wykluczyć wartość w tabeli
        print(s.where(s >10, 'warunek niespełniony'))
        s.where(s >10, 'warunek niespełniony', inplace=True)
        print(s)
                # jeżeli nie spełnia warunku cały wiersz zostaje usunięty
        print(df['Kraj'])
        print(df[df['Populacja']> 1200000])

              #DIODANIE ELEMENTU DO SERI DANYCH
                        # do 's' przypisujemy 14 do indexu 'e'
        print("dodanie nowego elementu")
        s['e']=14
        print(s)
        #wiersz         w każedj kolumnie pokaże "nowy el."
        df.loc[3] = 'nowy element'
        print(df)
        #wiersz
        df.loc[4] = ['Polska', 'Warszawa', 358111]
        print(df)

#       USUWANIE ELEMENTU na dwa sposoby
        print("usuwanie elementu")
        new = df.drop([3])
        print(new)
        df.drop([3], inplace=True)
        print(df)
        # DODANIE KOLUMNY
        print("dodanie kolumny")
        df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa','Europa']
        print(df)

        # SORTOWANIE WZGLĘDEM KRAJU
        print("sortowanie względem kraju")
        df.sort_values(by='Kraj', inplace=True)
        print(df)

        #WYPISZ TYLKO: W KOLUMNE "KONTYNENT" EUROPE
        grupa = df.groupby(by='Kontynent')
        print(grupa.get_group('Europa'))


        grupa = df.groupby('Kontynent').agg({'Populacja':['sum']})
        print(grupa)



#               WYKRES SŁUPKOWY
# kide=('line' : wykres liniowy (domyślnie),
        # 'bar': pionowy wykres słupkowy,
        # 'barh': poziomy wykres słupkowy
        # 'kde' : Wykres szacowania gęstości jądra

        # grupa.plot(kind='bar', xlabel='Kontynent',
        #            ylabel='Populacja w mld', rot=0,
        #            title='Populacja na kontynentach')
        # plt.show()
        #
        #           WYKRES II SPOSÓB zapisz wykres jako

        wykres = grupa.plot.bar()
        wykres.set_xlabel('Kontynent')
        wykres.set_ylabel('Populacja w mld')
        wykres.tick_params(axis='x', labelrotation=0)
        wykres.set_title('Populacja na kontynentach')
        #   ZAPISUJEMY WYKRES
        plt.savefig('plot2.png')
        plt.show()

def zadanie2():
        #

        s = pd.Series([1, 3, 5 ,5.5, 'a'])
        print(s)
        s = pd.Series([10, 12, 14, 8], index=['a', 'b', 'c','d'])
        print(s)





        data = {'Kraj': ['Belgia','Indie', 'Brazylia'],
                'Stolica':['Bruksela', 'New Delhi', 'Brasilia'],
                'Populacja':[1115542525, 551525251, 55515881]}
        # tabela
        df =pd.DataFrame(data)
        print(df)


if __name__ == '__main__':
        # zadanie1()
        zadanie2()