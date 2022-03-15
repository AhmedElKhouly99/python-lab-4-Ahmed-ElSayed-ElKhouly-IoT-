
class Person:
    moods = ("happy", "tired", "Lazy")
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self, hours):
        if isinstance(hours, int):
            if hours < 7:
                self.mood = Person.moods[1]
                return True
            elif hours == 7:
                self.mood = Person.moods[0]
                return True
            elif hours > 7:
                self.mood = Person.moods[2]
                return True
        else:
            return False

    def eat(self, meals):
        if isinstance(meals, int):
            if meals == 1:
                self.healthRate = 50
                return True
            elif meals == 2:
                self.healthRate = 75
                return True
            elif meals == 3:
                self.healthRate = 100
                return True
        else:
            return False

    def buy(self, items):
        if isinstance(items, int) and (items*10) > self.money:
            self.money -= (10 * items)
            return True
        else:
            return False

    @property
    def healthRate(self):
        return self.__healthRate

    @healthRate.setter
    def healthRate(self, hlr):
        if isinstance(hlr, int) and hlr >= 0 and hlr <= 100:
            self.__healthRate = hlr
            return True
        else:
            return False