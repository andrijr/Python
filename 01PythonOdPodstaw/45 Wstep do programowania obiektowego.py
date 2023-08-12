# klasa zbór informaccji o objekcie
# fukcja w klasei to są metodami
# funkcje które nie są w klasach są funkcjami
# self w metodzie oznacza że ta metoda wie że jest częśćią objęktu do którego jest klasa.
# Najważniejszą ceśćią jest ktoś lub coś czyli objekt a nie to co ktoś wykonuję czyli fukcja czy metoda


class Dog:
    def giveVoice(self):
        print("haw haw")

szarik = Dog()
azor = Dog()

azor.giveVoice()
szarik.giveVoice()
