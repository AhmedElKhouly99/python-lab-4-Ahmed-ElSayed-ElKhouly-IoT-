from employee import *

class Office:
    employeesNum = 0
    def __init__(self, name, employees):
        self.name = name
        self.employees = list(employees)


    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for e in self.employees:
            if e.id == empId:
                return e


    def hire(self, emp):
        self.employees.append(emp)
        Office.employeesNum += 1

    def fire(self, empId):
        for e in self.employees:
            if e.id == empId:
                self.employees.remove(e)
                Office.employeesNum -= 1

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        if isinstance(targetHour, (int, float)) and isinstance(moveHour, (int, float)) and isinstance(distance, (int, float)) and isinstance(velocity, (int, float)):
            time = distance/velocity
            moveHour += time
            if targetHour >= moveHour:
                print("Not late")
            else:
                print("Employee is late")


    def deduct(self, empId, deduction):
        for e in self.employees:
            if e.id == empId:
                e.salary -= deduction

    def reward(self, empId, reward):
        for e in self.employees:
            if e.id == empId:
                e.salary += reward

    @classmethod
    def change_emps_num (cls,num):
        if isinstance(num, int) and num >= 0:
            Office.employeesNum = num
            return True
        else:
            return False