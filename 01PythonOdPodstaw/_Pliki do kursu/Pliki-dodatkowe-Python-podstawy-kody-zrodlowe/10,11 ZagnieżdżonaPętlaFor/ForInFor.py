# for x in range(0,3):
#     print("Tutaj wewnętrzna pętla for:")
#     for y in range(0,4):
#         print(x,y)

# for x in range(1,11):
#     for y in range(1,11):
#         print(x*y, end="  ")
#     print("")

#Napisz program, który wyświetli wszystkie możliwe kombinacje czterocyfrowej kłódki, gdzie pierwsza cyfra jest parzysta, druga nieparzysta
#trzecia podzielna przez 5, a czwarta podzielna przez 3

for x in range(0,10,2):
    for y in range(1,10,2):
        for z in range(0,10,5):
            for t in range(0,10,3):
                print(x,y,z,t)

#1. Napisz program przypominający zapominalskiemu Jasiowi możliwe kody do jego kłódki. Jasio pamięta jedynie, że:
#Kłódka jest pięciocyfrowa
#Żadna cyfra nie jest większa niż 6
#Nie było w kodzie 0
#Pierwsza, trzecia i piąta cyfra to albo 0 albo 5
#Druga i czwarta były nieparzyste

#2. Znaleźć w jaki sposób poprawić nasz program z tabliczką mnożenia by odpowiednio się formatował.