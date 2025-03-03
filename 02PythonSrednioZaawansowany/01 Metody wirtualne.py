import Animal_01_1
import  random

listOfMarmals = []
for x in range(0,100):
    randomNumber = random.randint(0,1)
    if randomNumber == 0:
        listOfMarmals.append(Animal_01_1.Cat("Mruczek", 4, "Dachowiec"))
    else:
        listOfMarmals.append(Animal_01_1.Dog("Azor", 5, "Dalmatynczek"))


# metoda giveVoice() jest metoda wirtualna
# metoda wirtualna to taka metoda bezwzgłedu czy mamy doczynienia z objektem klasy Cat czy klasy Dog można ją wykonać
listOfMarmals[1].giveVoice()

for x in range(100):
    listOfMarmals[x].giveVoice()


# giraffe = Animal_01_1.Animal("żyr", 5)
# giraffe.giveVoice()