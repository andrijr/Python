# i = 10
# if i == 3:
#     print("i równa się 3")
# else:
#     print("i nie równa się 3")

# while i > 4:
#     i -= 1
#     print("Wszedłem do pętli while")
#     if i==7:
#         break
# else:
#     print("Instrukcja else")
#
# print("Instrukcje za pętlą while")

# import random
#
# zgadywana = random.randint(1,1000)
#
# odpowiedz = int(input("Wylosowałem liczbę z przedziału 1-1000, zgadnij ją, a jeżeli chcesz wyjść wpisz liczbę z poza przedziału 1-1000: "))
#
# while 1 <= odpowiedz <= 1000:
#     if odpowiedz > zgadywana:
#         print("Wylosowałem mniejszą liczbę")
#     elif odpowiedz < zgadywana:
#         print("Wylosowałem większą liczbę")
#     else:
#         print("Zgadłeś liczbę. Była to",zgadywana)
#         break
#     odpowiedz = int(input("Zgadnij inną: "))
#
# else:
#     print("Wyszedłeś z gry przed odgadnięciem, wylosowaną liczbą była:",zgadywana)
#
# print("Dziękuję!")

for i in range(10):
    print(i)
    if i % 5 == 0 and i != 0:
        break
else:
    print("Wyszedłeś z pętli")
print("Dalsze instrukcje")