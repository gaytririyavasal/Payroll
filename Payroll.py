# File: Payroll.py
# Student: Gaytri Riya Vasal
# UT EID: grv377
# Course Name: CS303E
# 
# Date Created: 9/13/2021
# Date Last Modified: 9/17/2021
# Description of Program: This program analyzes financial information and delivers a payroll statement.

print()

def main():
    employeename = input("Enter employee's name: ")
    hoursworked = float(input("Enter number of hours worked in a week: "))
    payrate = float(input("Enter hourly pay rate: "))
    federaltaxrate = float(input("Enter federal tax withholding rate: "))
    statetaxrate = float(input("Enter state tax withholding rate: "))
    grosspay = hoursworked * payrate
    federalwithholding = grosspay * federaltaxrate
    statewitholding = grosspay * statetaxrate
    totaldeduction = federalwithholding + statewitholding
    netpay = grosspay - totaldeduction

    print()

    print("Employee Name:", employeename)
    print("Hours Worked:", format(hoursworked, ".1f"))
    print("Pay Rate: $", format(payrate, ".2f"), sep="")
    print("Gross Pay: $", format(grosspay, ".2f"), sep="")
    print("Deductions:")
    print("  Federal Witholding (", format(federaltaxrate, ".1%"), "): $", format(federalwithholding, ".2f"), sep="")
    print("  State Withholding (", format(statetaxrate, ".1%"), "): $", format(statewitholding, ".2f"), sep="")
    print("  Total Deduction: $", format(totaldeduction, ".2f"), sep="")
    print("Net Pay: $", format(netpay, ".2f"), sep="")
main()
