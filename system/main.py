from system import *
def main():
    c = Car("Fiat128", 50, 50)
    e = Employee("Samy", 20000, "happy", 90, 1, c, "samy@gmail.com", 20000, 100)
    emps = [e]
    iti = Office("ITI", emps)
    c1 = Car("BMW", 50, 50)
    e1 = Employee("Ahmed", 30000, "happy", 90, 2, c, "ahmed@gmail.com", 20000, 100)
    e1.refuel(20)
    e1.drive(50, 95)
    e1.send_mail()
    iti.hire(e1)
    allEmps = iti.get_all_employees()
    print(allEmps)


main()