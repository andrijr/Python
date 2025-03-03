# kłasa abstrakcyjna to jest tak a klasa z której nie możemy lub nie chcemy tworzyć objektów



import Animal_02_1
import  random

listOfMarmals = []
for x in range(0,100):
    randomNumber = random.randint(0,1)
    if randomNumber == 0:
        listOfMarmals.append(Animal_02_1.Cat("Mruczek", 4, "Dachowiec"))
    else:
        listOfMarmals.append(Animal_02_1.Dog("Azor", 5, "Dalmatynczek"))


# metoda giveVoice() jest metoda wirtualna i bezwzgłedu czy mamy doczynienia z objektem klasy Cat czy klasy Dog można ją wykonać
listOfMarmals[1].giveVoice()

for x in range(100):
    listOfMarmals[x].giveVoice()


# giraffe = Animal_02_1.Animal() # żyrafy nie stworzymy dla animal bo klasa wykluczona
# giraffe.giveVoice()