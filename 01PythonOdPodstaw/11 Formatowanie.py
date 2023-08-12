# %-formatting
# str.format()

print('%(lang)s has %(number)03d quote types.' % {'lang': "Python", "number": 2})
print('%s has %03d quote types.' % ("Python", 2))
print('%s has %d quote types.' % ("Python", 2))

print("1 po angielsku: %s \n2 po angielsku: %s" % ('one', 'two'))
print("1 po angielsku: {} \n2 po angielsku: {}".format('one', 'two'))

print("Cyfra %d poprzedza %d" % (7, 8))
print("Cyfra {} poprzedza {}".format(7, 8))
print("Cyfra %d poprzedza %.2f" % (7.568, 8.569))
print("Cyfra {:6} poprzedza {:.2f}".format(7.569, 8.569))


print("Rekord świata na 100m to %f ustanowił go %s" % (9.58, 'Usain Bolt'))
print("Rekord świata na 100m to {} ustanowił go {}".format(9.58, 'Usain Bolt'))

# pokazujemy do ile znaków zaokrąglić
print("Rekord świata na 100m to %.2f ustanowił go %s" % (9.5877, 'Usain Bolt'))
print("Rekord świata na 100m to {:.2f} ustanowił go {}".format(9.5877, 'Usain Bolt'))


szer = 42
print("-" * szer)
print("|  Czas  |     Zawodnik     |    Data    |")
print("*" * szer)
print("| %6.3f | %16s | %10s |" % (9.58, "Usain Bolt", "16.08.2009"))
print("| %6.3f | %16s | %10s |" % (9.69, "Tyson Gay", "20.09.2009"))
print("| %6.3f | %16s | %10s |" % (9.69, "Yohan Blake", "23.09.2012"))
print("| %6.3f | %16s | %10s |" % (9.74, "Asafa Powell", "2.09.2008"))
print("-" * szer)


szer = 42
print("-" * szer)
print("|  Czas  |     Zawodnik     |    Data    |")
print("*" * szer)
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.58, "Usain Bolt", "16.08.2009"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.69, "Tyson Gay", "20.09.2009"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.69, "Yohan Blake", "23.09.2012"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.74, "Asafa Powell", "2.09.2008"))
print("-" * szer)


print("{} ma {}".format("Ala", "kota"))
print("{1} ma {0}".format("Ala", "kota"))
print("{0:10s} ma {1:10s}".format("Ala", "kota"))

print( "Moja %s o wadze %dg ma ok. %d kcal i %.1f węglowodanów" % ("czekolada", 100, 545, 58.5))
print("Moja {} o wadze {}g ma ok. {} kcal i {:.1f} węglowodanów".format("czekolada", 100, 545, 58.5))