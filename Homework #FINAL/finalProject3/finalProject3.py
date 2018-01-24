# Homework No. FINAL  Exercise No.3
# File Name:     finalProject3.py
# Programmer:    Kostyantyn Shumishyn
# Date:          December 14, 2017
#
# Problem Statement:
#
#
# Overall Plan:
# 1.

from Management import Management
from PartTime import PartTime
from Salary import Salary
from Hourly import Hourly


def Main():
    # Adds to an Employee List
    employeeList = []
    partTime = PartTime("Bob", "Barker", "1", 5)
    salary = Salary("Frank", "Neeson", "2", 4500)
    hourly = Hourly("Mike", "Smith", "3", 260, 18)
    employeeList.append(partTime)
    employeeList.append(salary)
    employeeList.append(hourly)

    # Creates a Management System
    miraCostaManagement = Management()

    # Adds list to it
    miraCostaManagement.AddEmployeeList(employeeList)

    # Writes Data to File
    miraCostaManagement.WriteToFile("MCCManifest.txt")

    # Prints Each Employee's Data
    for employee in miraCostaManagement.EmployeeList:
        print(employee.GetInfo() + "\n")


Main()
