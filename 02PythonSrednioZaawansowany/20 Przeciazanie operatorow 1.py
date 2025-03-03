# nie wszystkie języki programowania posiadają przeciążanie operatorów na dzień dzisiejszy java nie posiada

# print(5 * 5)
# print("ab" * 5)

class Clock:
    def __init__(self,hours = 0,minutes = 0,seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def addTime(self,hours = 0,minutes = 0,seconds = 0):
        if self.seconds + seconds >= 60:
            self.seconds = (self.seconds + seconds) % 60
            self.minutes += (self.seconds + seconds) // 60
        else:
            self.seconds = self.seconds + seconds
        if self.minutes + minutes  >= 60:
            self.minutes = (self.minutes + minutes)%60
            self.hours += (self.minutes + minutes)//60
        else:
            self.minutes = self.minutes + minutes
        self.hours = self.hours + hours



    def __str__(self):
        return f"{self.hours}h {self.minutes}m {self.seconds}s"

    # funkcja porównywania
    def __eq__(self, other):
        return  self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    # nadpisanie metody add
    def __add__(self, other):
        zegarek = Clock(self.hours ,self.minutes ,self.seconds)
        zegarek.addTime(other.hours, other.minutes, other.seconds)
        return zegarek

zegarek1 = Clock(10,11,12)
zegarek2 = Clock(11,11,12)
zegarek3 = Clock(11,11,12)


print(zegarek1 == zegarek2)
print(zegarek1.__eq__(zegarek2))
print(zegarek2 == zegarek3)
print("---")
print(zegarek1)
zegarek1.addTime(1,1,1)
print(zegarek1)
zegarek1.addTime(10,10,68)
print(zegarek1)
zegarek1.addTime(0,61,68)
print(zegarek1)
print(zegarek1 + zegarek2)
zegarek4 = zegarek1+zegarek2+zegarek3+zegarek2+zegarek2
print(zegarek4)
