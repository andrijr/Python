from Cat import Cat

kot1 = Cat(3,"bury","dachowiec","Mruczek")
kot2 = Cat(2,"niebieski","brytyjski","Sylwester")
kot3 = Cat(3,"bury","dachowiec","Mruczek")

print(kot1)
kot1.printInformationAboutCat()
print(kot2)
kot2.printInformationAboutCat()
print(kot3)
kot3.printInformationAboutCat()

kot4 = kot1
kot4.setName("Psotek")
kot4.printInformationAboutCat()
kot1.printInformationAboutCat()