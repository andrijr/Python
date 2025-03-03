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