# Homework No. FINAL  Exercise No.3
# File Name:     Salary.py
# Programmer:    Kostyantyn Shumishyn
# Date:          December 14, 2017
#
# Problem Statement: Employee Child Class

from Employee import Employee


class Salary(Employee):

    def __init__(self, firstName, lastName, employeeID, salary):
        Employee.__init__(self, firstName, lastName, employeeID)
        self.salary = salary

    @property
    def FirstName(self):
        return self.firstName

    @property
    def LastName(self):
        return self.lastName

    @property
    def EmployeeID(self):
        return self.employeeID

    @property
    def Salary(self):
        return self.salary

    def GetPay(self):
        return self.salary

    def GetInfo(self):
        return str("Name: " + self.FirstName + " " + self.LastName + "\nID: " + self.EmployeeID +
                   "\nSalary: " + str(self.Salary) + "\nPay: $" + str(self.GetPay()))
