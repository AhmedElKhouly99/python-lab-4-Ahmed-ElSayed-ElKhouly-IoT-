from person import *
from car import *
import re

class Employee(Person):
    def __init__(self, name, money, mood, healthRate, id , car, email, salary, distanceToWork):
        super(Employee, self).__init__(name, money, mood, healthRate)
        self.id = id
        # self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
        self.c = car

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, sal):
        if isinstance(sal, int) and sal >= 1000:
            self.__salary = sal
        else:
            self.__salary = 1000

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            self.__email = email
            return True
        else:
            return False

    def work(self, hours):
        if isinstance(hours, int):
            if hours < 8:
                self.mood = Person.moods[2]
                return True
            elif hours == 8:
                self.mood = Person.moods[0]
                return True
            elif hours > 8:
                self.mood = Person.moods[1]
                return True
        else:
            return False

    def drive(self, velocity, distance):
        if isinstance(distance, int):
            self.c.run(velocity, distance)
            return True
        else:
            return False
        

    def refuel(self, gasAmount = 100):
        self.c.fuelRate += gasAmount

    def send_mail(self, to="myFriend@gmail.com", subject="new mail", msg="This is an email template.", receiver_name="My friend"):
        try:
            with open("mail.txt","w") as mail:
                text = f'''
                    From: {self.email}
                    To: {to}\n
                    Hi, {receiver_name}\n
                    {msg}\n
                    thanks\n
                    ==================== Email Subject =======================\n
                    {subject}
                '''
                mail.write(text)
        except Exception as e:
            print(e)

# c = Car("bmw", 50, 50)
# e = Employee("ahmed", 30000, "happy", 90, 1, c, "ahmed@gmail.com", 30000, 100)
# e.refuel(20)
# e.drive(50, 95)
# e.send_mail()
# print(e)