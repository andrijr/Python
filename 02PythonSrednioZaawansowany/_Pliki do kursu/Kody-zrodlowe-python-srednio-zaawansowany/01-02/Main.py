import Virtual
import random

listOfMammals = []
for x in range(100):
    randomNumber = random.randint(0,1)
    if randomNumber == 0:
        listOfMammals.append(Virtual.Cat("Mruczek",4,"Dachowiec"))
    else:
        listOfMammals.append(Virtual.Dog("Azor",5,"Dalmatyńczyk"))

#giraffe = Virtual.Animal()

for x in range(100):
    listOfMammals[x].giveVoice()

#giraffe.giveVoice()