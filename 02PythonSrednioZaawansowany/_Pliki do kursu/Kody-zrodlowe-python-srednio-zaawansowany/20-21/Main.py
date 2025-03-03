class Clock:
    def __init__(self,hours = 0,minutes = 0,seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def addTime(self,hours = 0,minutes = 0,seconds = 0):
        if seconds + self.seconds >= 60:
            self.minutes += ((seconds + self.seconds) // 60)
            self.seconds = (seconds + self.seconds) % seconds
        else:
            self.seconds += seconds

        if minutes + self.minutes >= 60:
            self.hours += ((minutes + self.minutes) // 60)
            self.minutes = (minutes + self.minutes) % minutes
        else:
            self.minutes += minutes

        if hours + self.hours >= 24:
            self.hours = ((hours + self.hours) // 24)
        else:
            self.hours += hours

    def __str__(self):
        return f"{self.hours}h {self.minutes}m {self.seconds}s"

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __add__(self, other):
        zegarek = Clock(self.hours,self.minutes,self.seconds)
        zegarek.addTime(other.hours, other.minutes, other.seconds)
        return zegarek

zegarek1 = Clock(10,11,12)
zegarek2 = Clock(10,11,12)

zegarek1.addTime(2,150,50)

print(zegarek1 == zegarek2)
print(zegarek1)

print(zegarek1 + zegarek2)

zegarek3 = zegarek1 + zegarek2
print("Zegarek3: " + str(zegarek3))

# operatory przeciążania
# >, >= , < , <=, ==, +, -, *, /, //, %, **, len, print, str, repr, itd.

