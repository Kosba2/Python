# Homework No. FINAL  Exercise No.3
# File Name:     Management.py
# Programmer:    Kostyantyn Shumishyn
# Date:          December 14, 2017
#
# Problem Statement: Management Class

from Employee import Employee
from PartTime import PartTime
from Salary import Salary
from Hourly import Hourly


class Management:

    def __init__(self):
        self.employeeList = []

    @property
    def EmployeeList(self):
        return self.employeeList

    def AddEmployee(self, employee):
        self.EmployeeList.append(employee)

    def AddEmployeeList(self, employees):
        for employee in employees:
            self.EmployeeList.append(employee)

    def RemoveEmployee(self, employee):
        self.EmployeeList.remove(employee)

    def WriteToFile(self, fileName):
        with open(fileName, 'w') as f:
            for employee in self.EmployeeList:
                f.write(employee.GetInfo())
                f.write("\n\n")

    # Reads in a Database Text File and returns Employee list
    def ReadFromFile(self, fileName):
        # Creates an empty Employee list
        employeeList = []
        keepReading = True

        while keepReading:
            # Reads in File
            with open(fileName, 'r') as file:
                # Reads in Name line
                nameLine = file.readline()

                # Splits Line: "Text: FirstName LastName"
                nameList = nameLine.split()
                firstName = nameList[1]
                lastName = nameList[2]

                # Reads in ID Line
                idLine = file.readline()

                # Splits Line: "Text: ID"
                idList = idLine.split()
                eID = idList[1]

                # Variation Step
                variationLine = file.read()
                variableList = variationLine.split()
                emp = variableList[0]

                # Part Time
                if emp is "Number":
                    numberClasses = variableList[2]
                    tempPartTime = PartTime(firstName, lastName, eID, numberClasses)
                    employeeList.append(tempPartTime)

                # Salary
                elif emp is "Salary":
                    salary = variableList[1]
                    tempSalary = Salary(firstName, lastName, eID, salary)
                    employeeList.append(tempSalary)

                # Hourly
                elif emp is "Hours":
                    hoursWorked = variableList[2]
                    hoursRateLine = file.readline()
                    hoursRateList = hoursRateLine.split()
                    hoursRate = hoursRateList[2]
                    tempHourly = Hourly(firstName, lastName, eID, hoursWorked, hoursRate)
                    employeeList.append(tempHourly)

        # Returns the Employee List
        return employeeList
