# Homework No. FINAL  Exercise No.3
# File Name:     Hourly.py
# Programmer:    Kostyantyn Shumishyn
# Date:          December 14, 2017
#
# Problem Statement: Employee Child Class

from Employee import Employee


class Hourly(Employee):

    def __init__(self, firstName, lastName, employeeID, hoursWorked, hourlyRate):
        Employee.__init__(self, firstName, lastName, employeeID)
        self.hoursWorked = hoursWorked
        self.hourlyRate = hourlyRate

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
    def HoursWorked(self):
        return self.hoursWorked

    @property
    def HourlyRate(self):
        return self.hourlyRate

    def GetPay(self):
        return self.hoursWorked * self.hourlyRate

    def GetInfo(self):
        return str("Name: " + self.FirstName + " " + self.LastName + "\nID: " + self.EmployeeID +
                   "\nHours Worked: " + str(self.HoursWorked) + "\nHourly Rate: " + str(self.HourlyRate) +
                   "\nPay: $" + str(self.GetPay()))
