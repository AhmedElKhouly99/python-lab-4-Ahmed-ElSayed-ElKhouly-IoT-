
class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    def run(self, velocity, distance):
        self.velocity = velocity
        factor = 10
        remains = distance
        if distance >= 10:
            while factor <= distance and self.fuelRate > 0:
                remains -= factor
                self.fuelRate *= 0.9
                self.fuelRate = int(self.__fuelRate)
                factor += 10
        self.__stop(remains)


    def __stop(self, remainDis):
        self.velocity = 0
        notification = ""
        if remainDis > 0:
            notification = f"{remainDis} km from your destination."
        else:
            notification = "You have arrived successfully!!"
        print(notification)

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, vel):
        if isinstance(vel, int) and vel >= 0 and vel <= 200:
            self.__velocity = vel
        else:
            self.__velocity = 0

    @property
    def fuelRate(self):
        return self.__fuelRate

    @fuelRate.setter
    def fuelRate(self, flr):
        if isinstance(flr, int) or isinstance(flr, float) and flr >= 0 and flr <= 100:
            self.__fuelRate = flr
        else:
            self.__fuelRate = 0