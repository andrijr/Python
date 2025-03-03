import string
print("generowanie list")
l1 = list(string.ascii_uppercase)
print(l1)
l2 = [*range(1,11)]
print(l2)



# d1 = dict.fromkeys(string.ascii_lowercase, 0)
# print(d1)
#
# d2 = {'XX':0}
# d1 |= d2
# print(d1)

print("dodanie do listy listy")
l1 = [1,2,3]
l2 = [11,22,33]
l1 += l2
print(l1)

print("dodanie do listy tekstu")
l1 = [1,2,3]
l2 = [11,22,33]
l1[len(l2)+1:] = 'tekst'
print(l1)


print("łączenie 1")
l1 = [1,2,3]
l2 = [11,22,33]
for i in l2:
    l1.append(i)
print(l1)

l1 = [1,2,3]
[l1.append(i) for i in l2 ]
print(l1)

print("łączenie 2")
l1 = [1,2,3]
l2 = [11,22,33]
l1.extend(l2)
print(l1)

print("łączenie 3")
l1 = [1,2,3]
l2 = [11,22,33]
l3 = [*l1, *l2]
print(l3)

print("łączenie 4")
l3 = []
l3 = l1 + l2
print(l3)

print("łączenie 5")
l1 = [1,2,3]
l2 = [11,22,33]
l3 = []
l3 =  [x for n in (l1, l2) for x in n]
print(l3)
l3 = []
l3 = [i for i in l1]
print(l3)
l3 = []
l3 = [n for n in (l1, l2)]
print(l3)
l3 = []
l3 = [i for n in (l1, l2) for i in n]
print(l3)


