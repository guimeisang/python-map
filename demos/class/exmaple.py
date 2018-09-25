# coding=utf-8

class Employee: 
    empCount = 0;

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1

    def displayCount(self):
        print "total employee %d" % Employee.empCount

    def displayEmployee(self):
        print "name: ", self.name, ", Salary: ", self.salary

emp1 = Employee("zara", 2000)
emp2 = Employee("hihi", 2000)
emp3 = Employee("oooo", 2000)
emp1.displayCount();
emp1.displayEmployee();