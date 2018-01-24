# Homework No. FINAL  Exercise No.3
# File Name:     PartTime.py
# Programmer:    Kostyantyn Shumishyn
# Date:          December 14, 2017
#
# Problem Statement: Employee Child Class

from Employee import Employee


class PartTime(Employee):

    def __init__(self, firstName, lastName, employeeID, numberClasses):
        Employee.__init__(self, firstName, lastName, employeeID)
        self.numberClasses = numberClasses

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
    def NumberClasses(self):
        return self.numberClasses

    def GetPay(self):
        return self.numberClasses * 1000

    def GetInfo(self):
        return str("Name: " + self.FirstName + " " + self.LastName + "\nID: " + self.EmployeeID +
                   "\nNumber Classes: " + str(self.NumberClasses) + "\nPay: $" + str(self.GetPay()))
